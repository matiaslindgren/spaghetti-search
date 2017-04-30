from scrapy.exceptions import DropItem

class DuplicatesPipeline:
    def __init__(self):
        self.processed_urls = set()

    def process_item(self, item, spider):
        item_url = item['url']
        if item_url in self.processed_urls:
            raise DropItem("Section {} already parsed".format(item_url))
        self.processed_urls.add(item_url)
        return item

