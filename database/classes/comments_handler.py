import json


class CommentsHandler:

    def __init__(self, path: str):
        self.path = path
        self.data = self.get_comments_all()
        self.max_comment_id = self.get_max_comment_id()
        print(f"CommentsHandler initialized with data from '{path}'\n"
              f"Comments loaded: {len(self.data)}\n"
              f"Last comment id: {self.max_comment_id}\n")

    def __repr__(self):
        return f"Comments loaded: {len(self.data)}"

    def get_comments_all(self) -> list:

        with open(self.path, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
        return self.data

    def upload_into_json_file(self) -> None:
        """
        JSON Data uploader
        """
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

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

