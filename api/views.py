from flask import Blueprint, jsonify

from database.database import posts_obj

api_module = Blueprint("api", __name__)


@api_module.route("/api/posts")
def posts_api():
    posts = posts_obj.get_posts_all()
    return jsonify(posts)


@api_module.route("/api/post/<int:post_id>")
def post_api(post_id):
    post = posts_obj.get_post_by_pk(post_id)
    return jsonify(post)
