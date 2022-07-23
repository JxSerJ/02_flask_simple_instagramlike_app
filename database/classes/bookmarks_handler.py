from database.classes.file_handler import JsonFileHandler


class BookmarksHandler(JsonFileHandler):
    """Bookmarks Handler. Loads, writes and process bookmarks from and in DB"""

    def __init__(self, path: str):
        super().__init__(path)
        self.path = path
        self.data = self.load_json_file()
        print(f"BookmarksHandler initialized with data from '{path}'\n"
              f"Bookmarks loaded: {len(self.data)}\n")

    def __repr__(self):
        return f"Posts loaded: {len(self.data)}"

    def reload_data(self):
        """To ensure stable data flow in more than one thread"""
        self.data = self.load_json_file()

    def get_ids_all(self) -> list:
        self.reload_data()
        return self.data

    def get_index_by_pk(self, pk: int) -> int:
        """Return index of bookmark by id"""

        for i, dictionary in enumerate(self.data):
            if dictionary["pk"] == pk:
                return i
        return -1

    def is_post_in_db(self, pk: int) -> bool:

        self.reload_data()
        for post in self.data:
            return post["pk"] == pk

    def add_post_into_db(self, pk: int) -> None:

        self.reload_data()
        data_to_add = {"pk": pk}
        self.data.insert(0, data_to_add)
