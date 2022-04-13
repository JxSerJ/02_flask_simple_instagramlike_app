from flask import Blueprint, jsonify, current_app

api_module = Blueprint("api", __name__)


@api_module.route("/api/posts")
def posts_api():

    with current_app.app_context():
        posts_obj = current_app.config.get('POSTS_OBJ')

    posts = posts_obj.get_posts_all()
    return jsonify(posts)


@api_module.route("/api/post/<int:post_id>")
def post_api(post_id):

    with current_app.app_context():
        posts_obj = current_app.config.get('POSTS_OBJ')

    post = posts_obj.get_post_by_pk(post_id)
    return jsonify(post)
