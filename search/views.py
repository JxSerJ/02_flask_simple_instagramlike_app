from flask import Blueprint, render_template, request, url_for, current_app


search_module = Blueprint("search_page", __name__, template_folder="search_templates", static_folder="../static")


@search_module.route("/search", methods=["GET"])
def search_page():
    """THIS IS SEARCH PAGE VIEW"""

    with current_app.app_context():
        posts_obj = current_app.config.get('POSTS_OBJ')
        comments_obj = current_app.config.get('COMMENTS_OBJ')

    url_css = url_for("static", filename="css/styles.min.css")
    url_scripts = url_for("static", filename="scripts/scripts.js")

    hashtags = posts_obj.hashtags

    s = request.args.get("s")

    if s == "":
        found_posts = posts_obj.get_posts_all()
    elif s:
        found_posts = posts_obj.search_for_posts(s)
    else:
        found_posts = None

    return render_template("search.html", found_posts=found_posts, comments=comments_obj, url_css=url_css,
                           url_scripts=url_scripts, query=s, hashtags=hashtags)
