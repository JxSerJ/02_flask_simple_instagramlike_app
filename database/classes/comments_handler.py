from database.classes.file_handler import JsonFileHandler


class CommentsHandler(JsonFileHandler):
    """Обработчик комментариев из БД"""

    def __init__(self, path: str):
        super().__init__(path)
        self.data = self.load_json_file()
        self.max_comment_id = self.get_max_comment_id()
        print(f"CommentsHandler initialized with data from '{path}'\n"
              f"Comments loaded: {len(self.data)}\n"
              f"Last comment id: {self.max_comment_id}\n")

    def __repr__(self):
        return f"Comments loaded: {len(self.data)}"

    def get_comments_all(self) -> list:
        return self.data

    def get_comments_by_post_id(self, post_id: int) -> list:

        result_comments = []

        for comment in self.data:
            if comment["post_id"] == post_id:
                result_comments.append(comment)
        return result_comments

    def get_max_comment_id(self) -> int:
        max_comment_id = 0
        for entry in self.data:
            if entry["pk"] > max_comment_id:
                max_comment_id = entry["pk"]
            else:
                pass
        return max_comment_id

    def add_comment(self, data: dict) -> None:

        data["pk"] = self.max_comment_id + 1
        self.data.append(data)
