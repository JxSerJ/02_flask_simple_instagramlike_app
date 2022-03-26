from flask import Blueprint, render_template, request, url_for, redirect

from database.database import posts_obj, comments_obj, bookmarks_obj

bookmarks_module = Blueprint("bookmarks_module", __name__, template_folder="bookmarks_templates",
                             static_folder="../static")


@bookmarks_module.route("/bookmarks", methods=["GET"])
def bookmarks_page():
    url_css = url_for("static", filename="css/styles.min.css")
    url_scripts = url_for("static", filename="scripts/scripts.js")

    bookmarks = bookmarks_obj.get_posts_all()
    return render_template("bookmarks.html", url_css=url_css, url_scripts=url_scripts, bookmarks=bookmarks,
                           comments=comments_obj)


@bookmarks_module.route("/bookmarks/add/<int:post_id>", methods=['GET'])
def bookmarks_add(post_id: int):
    return redirect("/bookmarks", code=302)


@bookmarks_module.route("/bookmarks/remove/<post_id>", methods=['GET'])
def bookmarks_remove(post_id):
    return redirect("/bookmarks", code=302)

