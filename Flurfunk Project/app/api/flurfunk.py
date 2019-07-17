# Import flask dependencies
from app import utils, flurfunk
from flask import Blueprint, request, json, Response

bp = Blueprint("flurfunk", __name__)

@bp.route("/tags")
def crawl_tags():
    response = process_crawler()
    return ok_response(response.tags)

@bp.route("/authors")
def crawl_authors():
    response = process_crawler()
    return ok_response(response.authors)


@bp.route("/posts")
def crawl_posts():
    response = process_crawler()
    return ok_response(response.posts)

def process_crawler():
    deep = request.args.get("deep", "False")
    deep = utils.str2bool(deep)

    crawler = flurfunk.FFCrawler()
    if deep: crawler.crawl_deep()
    else: crawler.crawl_frontend()

    crawler.remove_duplicates()
    return crawler.result

def ok_response(obj):
    return Response(
        response=json.dumps(obj, default=lambda x: x.__dict__),
        mimetype="application/json",
        content_type="application/json",
        status=200
    )

