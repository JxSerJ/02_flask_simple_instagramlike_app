from database.classes.file_handler import JsonFileHandler


class PostsHandler(JsonFileHandler):
    """Posts Handler. Loads, writes and process posts from and in DB"""

    def __init__(self, path: str):
        super().__init__(path)
        self.path = path
        self.data = self.load_json_file()
        self.max_post_id = self.get_max_post_id()
        self.hashtags = self.get_hashtags()

        print(f"PostsHandler initialized with data from '{path}'\n"
              f"Posts loaded: {len(self.data)}\n"
              f"Last post id: {self.max_post_id}\n")

    def __repr__(self):
        return f"Posts loaded: {len(self.data)}"

    def reload_data(self):
        """To ensure stable data flow in more than one thread"""
        self.data = self.load_json_file()
        self.max_post_id = self.get_max_post_id()
        self.hashtags = self.get_hashtags()

    def get_posts_all(self) -> list:

        self.reload_data()
        return self.data

    def get_posts_by_user(self, user_name) -> list:

        self.reload_data()
        result_posts = []

        for post in self.data:
            if post["poster_name"] == user_name:
                result_posts.append(post)
        return result_posts

    def search_for_posts(self, query: str) -> list:

        self.reload_data()
        result_posts = []

        for post in self.data:
            if query.lower() in post["content"].lower():
                result_posts.append(post)
        return result_posts

    def get_post_by_pk(self, pk: int) -> dict:

        self.reload_data()
        result_posts = []

        for post in self.data:
            if post["pk"] == pk:
                result_posts = post
        return result_posts

    def get_posts_by_bookmarks_db(self, bookmarks_db: list[dict]) -> list:

        self.reload_data()
        result_posts = []
        bookmarks_pks = []
        for bookmark in bookmarks_db:
            bookmarks_pks.append(bookmark["pk"])

        for post in self.data:
            if post["pk"] in bookmarks_pks:
                result_posts.append(post)
        return result_posts

    def get_max_post_id(self) -> int:

        max_post_id = 0
        for entry in self.data:
            if entry["pk"] > max_post_id:
                max_post_id = entry["pk"]
            else:
                pass
        return max_post_id

    def add_post(self, data: dict) -> tuple[dict, int]:

        self.reload_data()
        data["pk"] = self.max_post_id + 1
        self.data.append(data)
        self.hashtags = self.get_hashtags()
        return data, self.max_post_id + 1

    def get_hashtags(self) -> dict:

        hashtags_index = {}

        for post in self.data:
            hashtags = []
            content = post["content"].replace(',', '').replace('!', '').split(" ")
            for word in content:
                if '#' in word:
                    hashtags.append(word.replace('#', ''))

            hashtags_index[post["pk"]] = hashtags

        return hashtags_index

    def get_hashtags_by_pk(self, pk: int) -> list:

        self.reload_data()
        for entry in self.hashtags:
            if entry == pk:
                return self.hashtags[pk]

    def get_pks_by_hashtags(self, hashtag) -> list:

        self.reload_data()
        pks = []
        for key, value in self.hashtags.items():
            if hashtag in value:
                pks.append(key)
        return pks

    def get_posts_by_pks(self, pks: list):

        self.reload_data()
        result_posts = []

        for post in self.data:
            if post["pk"] in pks:
                result_posts.append(post)
        return result_posts
