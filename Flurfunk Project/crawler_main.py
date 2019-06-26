import flurfunk

crawler = flurfunk.FFCrawler()


crawler.crawl_frontend()
crawler.crawl_deep()
crawler.remove_duplicates()
result = crawler.result

