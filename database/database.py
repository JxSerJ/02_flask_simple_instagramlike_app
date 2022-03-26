from config import POST_DB, COMMENTS_DB

from classes.post_handler import PostHandler
from classes.comment_handler import CommentHandler

posts_obj = PostHandler(POST_DB)
comments_obj = CommentHandler(COMMENTS_DB)