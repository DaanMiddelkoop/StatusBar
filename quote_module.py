from base import Base
from urllib.request import urlopen, Request
from lxml import html
import random


class QuoteModule(Base):


    def __init__(self):
        self.start = True
        self.url = 'https://www.brainyquote.com/quote_of_the_day'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}




    message = ""

    def name(self):
        return "Quotes"

    def full_text(self):
        if random.randint(0, 10000) == 1:
            self.start = True
        if self.start:
            self.start = False
            req = Request(self.url, headers=self.headers)

            response = urlopen(req)
            webContent = response.read().decode('utf-8')

            tree = html.fromstring(webContent)

            data = tree.xpath('//div[@class="clearfix"]/a/text()')
            self.message = "\\\"" + data[0] + "\\\" - " + data[1]
        return self.message

    def color(self):
        return "#FFFFFF"

    def min_width(self):
        return ""

    def backgXxround(self):
        return "#00000"


if __name__ == "__main__":
    module = QuoteModule()
    text = module.full_text()
