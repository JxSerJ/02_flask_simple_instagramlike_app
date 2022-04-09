from flask import Flask, render_template, send_from_directory

from database.database import posts_obj, comments_obj, bookmarks_obj

from search.views import search_module
from bookmarks.views import bookmarks_module
from loader.views import post_loader
from api.views import api_module

import logging

application = Flask(__name__)

application.config['JSON_AS_ASCII'] = False

logging.basicConfig(level=logging.INFO)

application.register_blueprint(search_module)
application.register_blueprint(bookmarks_module)
application.register_blueprint(post_loader)
application.register_blueprint(api_module, follow_redirects=True)


@application.route("/", methods=['GET'])
def main_page():
    posts = posts_obj.data
    hashtags = posts_obj.hashtags
    bookmarks_count = len(bookmarks_obj.get_ids_all())
    return render_template("index.html", posts_list=posts, comments=comments_obj, bookmarks_count=bookmarks_count,
                           hashtags=hashtags)


@application.route("/posts/<int:post_id>", methods=['GET'])
def post_page(post_id: int):
    post = posts_obj.get_post_by_pk(post_id)
    hashtags = posts_obj.get_hashtags_by_pk(post_id)
    comments = comments_obj.get_comments_by_post_id(post_id)
    return render_template("post.html", post=post, comments=comments, hashtags=hashtags)


@application.route("/users/<user_name>", methods=['GET'])
def user_page(user_name):
    posts = posts_obj.get_posts_by_user(user_name)
    hashtags = posts_obj.hashtags
    return render_template("user-feed.html", user_name=user_name, posts=posts, comments=comments_obj, hashtags=hashtags)


@application.route("/data/img/<path:path>", methods=['GET'])
def dynamic_dir(path):
    return send_from_directory("data/img", path)


@application.route("/tag/<tag_name>", methods=['GET'])
def tag_page(tag_name):
    posts_ids = posts_obj.get_pks_by_hashtags(tag_name)
    posts_for_view = posts_obj.get_posts_by_pks(posts_ids)
    hashtags = posts_obj.hashtags
    return render_template("tag.html", posts=posts_for_view, tag=tag_name, comments=comments_obj, hashtags=hashtags)


if __name__ == "__main__":
    application.run(debug=False)
