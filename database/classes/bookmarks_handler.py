import json
from typing import Type

from database.classes.posts_handler import PostsHandler


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
            json.dump(self.data, file, ensure_ascii=False, indent=4)

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

    def get_index_by_pk(self, pk: int) -> int:
        """Return index of bookmark by id"""

        for i, dictionary in enumerate(self.data):
            if dictionary["pk"] == pk:
                return i
        return -1

    def is_post_in_db(self, pk: int) -> bool:

        for post in self.data:
            if post["pk"] == pk:
                return True
        return False

    def add_post_into_db(self, post_db: Type[PostsHandler], pk: int) -> None:

        post = post_db.get_post_by_pk(pk)
        self.data.insert(0, post)
