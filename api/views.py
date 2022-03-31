from flask import Blueprint, jsonify

from database.classes.posts_handler import PostsHandler
from database.classes.comments_handler import CommentsHandler
from config import POST_DB, COMMENTS_DB

api_module = Blueprint("api", __name__)

post_obj = PostsHandler(POST_DB)
comment_obj = CommentsHandler(COMMENTS_DB)


@api_module.route("/api/posts")
def posts_api():
    posts = post_obj.get_posts_all()
    return jsonify(posts)


@api_module.route("/api/post/<int:post_id>")
def post_api(post_id):
    post = post_obj.get_post_by_pk(post_id)
    return jsonify(post)
