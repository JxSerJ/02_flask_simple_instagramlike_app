import logging
from colorama import Fore

from flask import Blueprint, render_template, url_for, request, redirect
from datetime import datetime

from database.database import posts_obj, comments_obj
from config import UPLOAD_FOLDER
from loader.config import ALLOWED_EXTENSIONS

post_loader = Blueprint("post_loader", __name__, static_folder="../static", template_folder="loader_templates")


@post_loader.route("/post", methods=["GET"])
def loader_page():
    url_css = url_for("static", filename="css/styles.min.css")
    return render_template("load_post.html", url_css=url_css)


@post_loader.route("/post", methods=["POST"])
def upload_post():
    url_css = url_for("static", filename="css/styles.min.css")

    error = None

    picture = request.files.get("picture")
    user_name = request.form.get("user_name")
    post_content = request.form.get("content")

    if picture:
        file_name_extension = picture.filename.split(".")[-1]
        if file_name_extension in ALLOWED_EXTENSIONS:
            picture_name = picture.filename[:-len(file_name_extension) - 1]
            file_full_name = f"{picture_name}_{datetime.now().strftime('%d%m%Y_%H%M%S')}.{file_name_extension}"

            url_pic = f"{UPLOAD_FOLDER}/{file_full_name}"

            try:
                picture.save(url_pic)
            except FileNotFoundError:
                error = "Данные не загружены"
                return render_template("loader_error.html", url_css=url_css, error=error)
            else:
                data_to_add = {"poster_name": user_name,
                               "poster_avatar": url_for("static", filename="img/ava_default.jpg"),
                               "pic": f"/{url_pic}", "content": post_content, "views_count": 1, "likes_count": 0}
                post_uploaded, post_id = posts_obj.add_post(data_to_add)
                posts_obj.upload_into_json_file()
                hashtags = posts_obj.get_hashtags_by_pk(post_id)
                return render_template("post.html", url_css=url_css, post=post_uploaded, hashtags=hashtags)
        else:
            error = f"Тип файла недопустим. Допустимые типы файлов: {', '.join(ALLOWED_EXTENSIONS)}"
    else:
        error = "Файл не загружен"

    return render_template("loader_error.html", url_css=url_css, error=error)


@post_loader.route("/post/add_comment", methods=["POST"])
def upload_comment():
    url_css = url_for("static", filename="css/styles.min.css")

    user_name = request.form.get("user_name")
    comment_content = request.form.get("content")
    post_id = request.form.get("post_id")

    if comment_content:

        data_to_add = {"post_id": int(post_id), "commenter_name": user_name, "comment": comment_content}
        comments_obj.add_comment(data_to_add)
        comments_obj.upload_into_json_file()
        logging.info(f"{Fore.MAGENTA}Comment added into DB. Reloading page.{Fore.RESET}")
        return redirect(f"/posts/{post_id}", code=302)

    else:
        logging.info(f"{Fore.MAGENTA}Empty comment. Skipping uploading. Reloading page.{Fore.RESET}")
        return redirect(f"/posts/{post_id}", code=302)

