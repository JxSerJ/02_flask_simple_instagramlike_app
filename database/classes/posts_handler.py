import json


class PostsHandler:

    def __init__(self, path: str):
        self.path = path
        self.data = self.get_posts_all()
        self.max_post_id = self.get_max_post_id()
        self.hashtags = self.get_hashtags()

        print(f"PostsHandler initialized with data from '{path}'\n"
              f"Posts loaded: {len(self.data)}\n"
              f"Last post id: {self.max_post_id}\n")

    def __repr__(self):
        return f"Posts loaded: {len(self.data)}"

    def load_json_file(self) -> list:
        """
        JSON Data loader
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
        return self.data

    def upload_into_json_file(self) -> None:
        """
        JSON Data uploader
        """
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def get_posts_all(self) -> list:
        with open(self.path, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
        return self.data

    def get_posts_by_user(self, user_name) -> list:

        result_posts = []

        for post in self.data:
            if post["poster_name"] == user_name:
                result_posts.append(post)
        return result_posts

    def search_for_posts(self, query: str) -> list:

        result_posts = []

        for post in self.data:
            if query.lower() in post["content"].lower():
                result_posts.append(post)
        return result_posts

    def get_post_by_pk(self, pk: int) -> dict:

        result_posts = []

        for post in self.data:
            if post["pk"] == pk:
                result_posts = post
        return result_posts

    def get_posts_by_bookmarks_db(self, bookmarks_db: list[dict]) -> list:

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

        for entry in self.hashtags:
            if entry == pk:
                return self.hashtags[pk]

    def get_pks_by_hashtags(self, hashtag) -> list:

        pks = []
        for key, value in self.hashtags.items():
            if hashtag in value:
                pks.append(key)
        return pks

    def get_posts_by_pks(self, pks: list):

        result_posts = []

        for post in self.data:
            if post["pk"] in pks:
                result_posts.append(post)
        return result_posts
