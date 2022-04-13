from config import POST_DB, COMMENTS_DB, BOOKMARKS_DB

from database.classes.posts_handler import PostsHandler
from database.classes.comments_handler import CommentsHandler
from database.classes.bookmarks_handler import BookmarksHandler

POSTS_OBJ = PostsHandler(POST_DB)
COMMENTS_OBJ = CommentsHandler(COMMENTS_DB)
BOOKMARKS_OBJ = BookmarksHandler(BOOKMARKS_DB)
