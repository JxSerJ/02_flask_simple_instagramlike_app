from flask import Blueprint, render_template, request, url_for

from database.database import posts_obj, comments_obj


search_module = Blueprint("search_page", __name__, template_folder="search_templates", static_folder="../static")


@search_module.route("/search", methods=["GET"])
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

    return render_template("search.html", found_posts=found_posts, comments=comments_obj, url_css=url_css, url_scripts=url_scripts, query=s)
