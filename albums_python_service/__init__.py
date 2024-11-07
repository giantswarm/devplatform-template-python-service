import http
from http import HTTPStatus

from flask import Flask, render_template, redirect, url_for, request
from prometheus_flask_exporter import PrometheusMetrics

from albums_python_service.album import InMemoryStore, AlbumNotFound, Album
from albums_python_service.version import version, commit, release_date


def create_app(test_config=None):
    # create and configure the app
    flask_app = Flask(__name__, instance_relative_config=True)
    metrics = PrometheusMetrics(flask_app, group_by="endpoint")  # noqa: F841

    store = InMemoryStore()

    @flask_app.context_processor
    def inject_build_info():
        return dict(version=version, commit=commit, date=release_date)

    @flask_app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    @flask_app.route("/ping", methods=["GET"])
    def hello():
        return "pong"

    @flask_app.route("/albums", methods=["GET"])
    def list_albums():
        return render_template("albums.html", albums=store.list())

    @flask_app.route("/albums/<int:aid>", methods=["GET"])
    def get_album(aid: int):
        try:
            a = store.get(aid)
            return render_template("album.html", album=a)
        except AlbumNotFound:
            return (
                render_template("error.html", error="Album not found"),
                HTTPStatus.NOT_FOUND,
            )

    @flask_app.route("/albums/<int:aid>", methods=["DELETE"])
    def delete_album(aid: int):
        try:
            store.remove(aid)
            return redirect(url_for("list_albums")), http.HTTPStatus.FOUND
        except AlbumNotFound:
            return (
                render_template("error.html", error="Album not found"),
                HTTPStatus.NOT_FOUND,
            )

    @flask_app.route("/addalbum", methods=["GET"])
    def add_album_form():
        return render_template("addalbum.html")

    @flask_app.route("/albums", methods=["POST"])
    def add_album():
        new_album_json = request.json
        new_album = Album(
            0,
            new_album_json["title"],
            new_album_json["artist"],
            new_album_json["price"],
        )
        store.add(new_album)
        return render_template("albums.html", albums=store.list())

    @flask_app.route("/albums/<int:aid>", methods=["PUT"])
    def update_album(aid: int):
        album_json = request.json
        a = Album(
            album_json["id"],
            album_json["title"],
            album_json["artist"],
            album_json["price"],
        )
        store.update(a)
        return render_template("albums.html", albums=store.list())

    return flask_app


app = create_app()
