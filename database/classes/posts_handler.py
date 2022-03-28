import json


class PostsHandler:

    def __init__(self, path: str):
        self.path = path
        self.data = self.get_posts_all()
        self.max_post_id = self.get_max_post_id()

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

    def get_posts_by_pks(self, pk: list) -> list:

        result_posts = []
        bookmraks_pks = []
        for bookmark in pk:
            bookmraks_pks.append(bookmark["pk"])

        for post in self.data:
            if post["pk"] in bookmraks_pks:
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

    def add_post(self, data: dict) -> dict:

        data["pk"] = self.max_post_id + 1
        self.data.append(data)
        return data
