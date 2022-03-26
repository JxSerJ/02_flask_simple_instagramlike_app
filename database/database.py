from config import POST_DB, COMMENTS_DB, BOOKMARKS_DB

from classes.posts_handler import PostsHandler
from classes.comments_handler import CommentsHandler
from classes.bookmarks_handler import BookmarksHandler

posts_obj = PostsHandler(POST_DB)
comments_obj = CommentsHandler(COMMENTS_DB)
bookmarks_obj = BookmarksHandler(BOOKMARKS_DB)
