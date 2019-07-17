import utils
import flurfunk
from flask import Flask, escape, request, json

app = Flask(__name__)

with app.app_context():
    pass # warming up

@app.route("/")
def hello():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)}!"

@app.route("/tags")
def crawl_tags():
    response = process_crawler()
    return ok_response(response.tags)

@app.route("/authors")
def crawl_authors():
    response = process_crawler()
    return ok_response(response.authors)


@app.route("/posts")
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
    return app.response_class(
        response=json.dumps(obj, default=lambda x: x.__dict__),
        mimetype="application/json",
        content_type="application/json",
        status=200
    )