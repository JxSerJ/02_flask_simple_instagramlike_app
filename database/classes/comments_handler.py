import json


class CommentsHandler:

    def __init__(self, path: str):
        self.path = path
        self.data = self.get_comments_all()
        print(f"CommentsHandler initialized with data from '{path}'\n"
              f"Comments loaded: {len(self.data)}\n")

    def __repr__(self):
        return f"Comments loaded: {len(self.data)}"

    def get_comments_all(self) -> list:

        with open(self.path, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
        return self.data

    def upload_into_json_file(self, data_to_add: dict) -> None:
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
