from flask import Blueprint, render_template, request, url_for, redirect
import logging

from colorama import Fore

from database.database import posts_obj, comments_obj, bookmarks_obj

bookmarks_module = Blueprint("bookmarks_module", __name__, template_folder="bookmarks_templates",
                             static_folder="../static")


@bookmarks_module.route("/bookmarks", methods=["GET"])
def bookmarks_page():
    url_css = url_for("static", filename="css/styles.min.css")
    url_scripts = url_for("static", filename="scripts/scripts.js")

    bookmarks_ids = bookmarks_obj.get_ids_all()
    hashtags = posts_obj.hashtags

    bookmarks = posts_obj.get_posts_by_bookmarks_db(bookmarks_ids)
    return render_template("bookmarks.html", url_css=url_css, url_scripts=url_scripts, bookmarks=bookmarks,
                           comments=comments_obj, hashtags=hashtags)


@bookmarks_module.route("/bookmarks/add/<int:post_id>", methods=['GET'])
def bookmarks_add(post_id: int):

    redirect_target = request.args.get("rt")

    logging.info(f"{Fore.MAGENTA}Analyzing bookmarks DB{Fore.RESET}")

    if bookmarks_obj.is_post_in_db(post_id):

        logging.info(f"{Fore.MAGENTA}Post ID:{post_id} found in bookmarks DB. Removing post by redirecting to "
                     f"'/bookmarks/remove'{Fore.RESET}")

        return redirect(f"/bookmarks/remove/{post_id}?rt={redirect_target}", code=302)

    logging.info(f"{Fore.MAGENTA}Adding post ID:{post_id} into bookmarks DB{Fore.RESET}")

    bookmarks_obj.add_post_into_db(post_id)
    bookmarks_obj.upload_into_json_file()

    logging.info(f"{Fore.MAGENTA}Post ID:{post_id} added into bookmarks DB{Fore.RESET}")

    return redirect(f"{redirect_target}", code=302)


@bookmarks_module.route("/bookmarks/remove/<int:post_id>", methods=['GET'])
def bookmarks_remove(post_id):

    redirect_target = request.args.get("rt")

    logging.info(f"{Fore.MAGENTA}Removing post ID:{post_id} from bookmarks DB{Fore.RESET}")

    bookmarks_obj.data.pop(bookmarks_obj.get_index_by_pk(post_id))
    bookmarks_obj.upload_into_json_file()

    logging.info(f"{Fore.MAGENTA}Post ID:{post_id} removed from bookmarks DB{Fore.RESET}")

    return redirect(f"{redirect_target}", code=302)
