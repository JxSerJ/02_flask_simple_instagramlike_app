from flask import Flask, redirect, request, render_template

from search.views import search

from database.database import posts_obj, comments_obj


application = Flask(__name__)

application.register_blueprint(search)


@application.route("/", methods=['GET'])
def main_page():
    posts = posts_obj.data
    bookmarks = [3, 1]  # bookmarks_obj
    return render_template("index.html", posts_list=posts, comments=comments_obj, bookmarks=bookmarks)


@application.route("/posts/<int:post_id>", methods=['GET'])
def post_page(post_id: int):
    post = posts_obj.get_post_by_pk(post_id)
    comments = comments_obj.get_comments_by_post_id(post_id)
    return render_template("post.html", post=post, comments=comments)


@application.route("/users/<user_name>", methods=['GET'])
def user_page(user_name):
    posts = posts_obj.get_posts_by_user(user_name)
    return render_template("user-feed.html", user_name=user_name, posts=posts, comments=comments_obj)


# api1

# api2


@application.route("/tag/<tag_name>", methods=['GET'])
def tag_page(tag_name):
    pass


@application.route("/bookmarks/", methods=['GET'])
def bookmarks_page():
    return render_template("bookmarks.html")


@application.route("/bookmarks/add/<int:post_id>", methods=['GET'])
def bookmarks_add(post_id: int):
    return redirect("/", code=302)


@application.route("/bookmarks/remove/<post_id>", methods=['POST'])
def bookmarks_remove(post_id):
    return redirect("/bookmarks", code=302)


application.run(debug=True)
