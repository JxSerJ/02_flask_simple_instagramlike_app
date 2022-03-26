import json


class BookmarksHandler:

    def __init__(self, path: str):
        self.path = path
        self.data = self.get_posts_all()
        print(f"BookmarksHandler initialized with data from '{path}'\n"
              f"Bookmarks loaded: {len(self.data)}\n")

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

    def get_post_by_pk(self, pk: int) -> dict:

        result_posts = {}

        for post in self.data:
            if post["pk"] == pk:
                result_posts = post
        return result_posts
