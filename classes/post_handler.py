import json


class PostHandler:

    def __init__(self, path: str):
        self.path = path
        self.data = self.get_posts_all()
        print(f"PostHandler initialized with data from '{path}'\n"
              f"Posts loaded: {len(self.data)}\n")

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
            json.dump(self.data, file, ensure_ascii=False)

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

    # def get_comments_by_post_id(self, post_id) -> list:
    #
    #     return comments_obj.get_comments_by_post_id(post_id)

    def search_for_posts(self, query: str) -> list:

        result_posts = []

        for post in self.data:
            if query.lower() in post["content"].lower():
                result_posts.append(post)
        return result_posts

    def get_post_by_pk(self, pk: int) -> dict:

        result_posts = {}

        for post in self.data:
            if post["pk"] == pk:
                result_posts = post
        return result_posts
