from flask import Flask, redirect, request, render_template, send_from_directory

from search.views import search_module
from bookmarks.views import bookmarks_module

from database.database import posts_obj, comments_obj, bookmarks_obj

import logging


application = Flask(__name__)

logging.basicConfig(level=logging.INFO)

application.register_blueprint(search_module)
application.register_blueprint(bookmarks_module)


@application.route("/", methods=['GET'])
def main_page():
    posts = posts_obj.data
    bookmarks_count = len(bookmarks_obj.get_posts_all())
    return render_template("index.html", posts_list=posts, comments=comments_obj, bookmarks_count=bookmarks_count)


@application.route("/posts/<int:post_id>", methods=['GET'])
def post_page(post_id: int):
    post = posts_obj.get_post_by_pk(post_id)
    comments = comments_obj.get_comments_by_post_id(post_id)
    return render_template("post.html", post=post, comments=comments)


@application.route("/users/<user_name>", methods=['GET'])
def user_page(user_name):
    posts = posts_obj.get_posts_by_user(user_name)
    return render_template("user-feed.html", user_name=user_name, posts=posts, comments=comments_obj)


@application.route("/uploads/<path:path>", methods=['GET'])
def dynamic_dir(path):
    return send_from_directory("data/img", path)

# api1

# api2


@application.route("/tag/<tag_name>", methods=['GET'])
def tag_page(tag_name):
    pass


if __name__ == "__main__":
    application.run(debug=True)
