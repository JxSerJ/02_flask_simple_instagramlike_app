from flask import Blueprint, render_template, request, url_for

from config import POST_DB, COMMENTS_DB

from classes.post_handler import PostHandler
from classes.comment_handler import CommentHandler

posts_obj = PostHandler(POST_DB)
comments_obj = CommentHandler(COMMENTS_DB)

search = Blueprint("search_page", __name__, template_folder="search_templates", static_folder="../static")


@search.route("/search", methods=["GET"])
def search_page():

    url_css = url_for("static", filename="css/styles.min.css")
    url_scripts = url_for("static", filename="scripts/scripts.js")
    error = None

    # posts_list = posts_obj.get_posts_all()
    s = request.args.get("s")

    if s == "":
        found_posts = posts_obj.get_posts_all()
    elif s:
        found_posts = posts_obj.search_for_posts(s)
    else:
        found_posts = None

    return render_template("search.html", found_posts=found_posts, comments=comments_obj, url_css=url_css, url_scripts=url_scripts)
