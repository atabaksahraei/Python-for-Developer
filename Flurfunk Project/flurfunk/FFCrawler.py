import requests
import json
from bs4 import BeautifulSoup

from .entity.CrawlerResult import CrawlerResult
from .entity.Post import Post
from .entity.Author import Author
from .entity.Tag import Tag

class FFCrawler():

# "html.parser" -> ist nicht das schnellste, aber bereits in python integriert
    def __init__(self, parser = "html.parser"):
        self.result = CrawlerResult()
        self.parser = parser

    def remove_duplicates(self):
        self.result.tags = list(dict.fromkeys(self.result.tags))

    def crawl_frontend(self):
        websiteContent = requests.get("https://www.sdx-ag.de/flurfunk/")
        self.__parse_html(websiteContent.text)

    def crawl_deep(self):
        all_posts = requests.get("https://www.sdx-ag.de/wp-admin/admin-ajax.php?action=load_more_posts")
        all_posts_json = json.loads(all_posts.content)
        for data in all_posts_json["data"]:
            author = self.__parse_author(BeautifulSoup(data["img"], self.Parser))
            author.name = data["author_name"].strip()

            tags = self.__parse_tags(BeautifulSoup(data["tags"], self.Parser))
            
            post = Post()
            post.title = data["title"].strip()
            post.url = data["permalink"].strip()
            post.shortText = data["excerpt"].strip()
            post.published = data["date"].strip()
            post.tags = [name for name in tags]
            post.author = author.name

            self.result.tags.extend(post.tags)
            self.result.posts.append(post)
            self.result.authors.append(author)

    def __parse_html(self, html):
        doc = BeautifulSoup(html, self.Parser)
        for article in doc.find_all("article"):
            author = self.__parse_author(article)
            tags = self.__parse_tags(article)
            post = self.__parse_post(article)
            post.tags = [name for name in tags]
            post.author = author.name

            self.result.tags.extend(post.tags)
            self.result.posts.append(post)
            self.result.authors.append(author)

    def __parse_post(self, article):
        post = Post()
        post.title = article.select_one("h4").text.strip()
        post.url = article.select_one("h4").parent.attrs["href"].strip()
        post.shortText = article.select_one(".excerpt").text.strip()
        post.published = article.select_one(".date").text.strip()
        return post

    def __parse_tags(self, article):
        selector = article.select_one(".tags_news")
        if(selector is None): selector = article

        for content in selector.select("a"):
            yield content.text.strip()

    def __parse_author(self, article):
        author = Author()

        if article.select_one(".author") is not None:
            author.name = article.select_one(".author").text.strip()
        
        if article.select_one(".wp-post-image") is not None:
            author.image = article.select_one(".wp-post-image").attrs["src"]
        elif article.select_one("img") is not None:
            author.image = article.select_one("img").attrs["src"]

        return author