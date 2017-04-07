# crawl cook -o op.json
import scrapy
from scrapy.http import Request

from ..items import CookItem



def urlgen():
    urllist = ['http://food.ndtv.com/recipes/accompaniments-recipes/page-1',
                'http://food.ndtv.com/recipes/back-to-basics-recipes/page-1',
                'http://food.ndtv.com/recipes/beverages-recipes/page-1',
                'http://food.ndtv.com/recipes/breads-recipes/page-1',
                'http://food.ndtv.com/recipes/chicken-recipes/page-1',
                'http://food.ndtv.com/recipes/desserts-recipes/page-1',
                'http://food.ndtv.com/recipes/eggs-recipes/page-1',
                'http://food.ndtv.com/recipes/healthy-recipes/page-1',
                'http://food.ndtv.com/recipes/indian-breads-recipes/page-1',
                'http://food.ndtv.com/recipes/indian-desserts-recipes/page-1',
                'http://food.ndtv.com/recipes/kids-recipes/page-1',
                'http://food.ndtv.com/recipes/low-fat-recipes/page-1',
                'http://food.ndtv.com/recipes/meat-recipes/page-1',
                'http://food.ndtv.com/recipes/pasta-and-noodles-recipes/page-1',
                'http://food.ndtv.com/recipes/quick-and-easy-recipes/page-1',
                'http://food.ndtv.com/recipes/rice-recipes/page-1',
                'http://food.ndtv.com/recipes/salads-recipes/page-1',
                'http://food.ndtv.com/recipes/seafood-recipes/page-1',
                'http://food.ndtv.com/recipes/snacks-recipes/page-1',
                'http://food.ndtv.com/recipes/soup-recipes/page-1',
                'http://food.ndtv.com/recipes/vegetarian-recipes/page-1']
    
    return urllist


class Cook(scrapy.Spider):
    name = 'cook'  # spider name
    allowed_domains = ['food.ndtv.com']
    start_urls = urlgen()

    def parse(self, response):
        # f = open('alpha.txt','a')
        # category = str(response.request.headers.get('Referer', None))[-1]
        category = response.url.split('/')[-2]

        # links_category = {}
        links = []
        for sel in response.xpath('//*[@id="recipe_pic_new"]/ul/li'):
            links.append(sel.xpath('a/@href').extract_first())
            # links_category[sel.xpath('a/@href').extract_first()] = category

        for link in links:
            self.category = category
            yield Request(link, callback=self.parse_result)

        NEXT_PAGE_XPATH = '//*[@id="inside_pagination"]/span[last()]/a/@href'
        next_page = response.xpath(NEXT_PAGE_XPATH).extract_first()

        if next_page != response.request.headers.get('Referer', None):
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

    def parse_result(self, response):
        item = CookItem()
        item['category'] = self.category

        item['prep_time'] = response.css('body > div.content_cont > div.content_box > div.lhs_cont > \
            div.mid_cont > div.recp-det-cont > span > div.method-cont > div > div.recipe-details > ul > \
            li:nth-child(2) > div > time::text').extract_first()

        item['cook_time'] = response.css('body > div.content_cont > div.content_box > div.lhs_cont > \
            div.mid_cont > div.recp-det-cont > span > div.method-cont > div > div.recipe-details > ul > \
            li:nth-child(3) > div > time::text').extract_first()

        item['name'] = response.css('body > div.content_cont > div.content_box > div.lhs_cont > div.mid_cont \
         > div.recp-det-cont > span > h1::text').extract_first()

        item['description'] = response.css('body > div.content_cont > div.content_box > div.lhs_cont > div.mid_cont \
         > div.recp-det-cont > span > div.method-cont > div > div.recipe-details > h2::text').extract_first()

        
        x = response.css('body > div.content_cont > div.content_box > div.lhs_cont \
         > div.mid_cont > div.recp-det-cont > span > div.method-cont > div > div.recipe_peocess \
         > div.ingredients > ul > li')

        ingredient_list = []

        for sel in x:
            if sel.xpath('i'):
                ingredient_list.append(sel.xpath('normalize-space(text())').extract_first() + sel.xpath('normalize-space(i/text())').extract_first())
            else:
                ingredient_list.append(sel.xpath('normalize-space(text())').extract_first())

        item['ingredients'] = ingredient_list

        method_list = []

        x =  response.css('body > div.content_cont > div.content_box > div.lhs_cont \
            > div.mid_cont > div.recp-det-cont > span > div.method-cont > div > div.recipe_peocess \
            > div.method > ol > li')
        
        item['method'] = x.xpath('normalize-space(span/text())').extract()

        item['tags'] = response.css('body > div.content_cont > div.content_box > div.lhs_cont \
            > div.mid_cont > div.recp-det-cont > span > div.method-cont > div \
            > div.recptags.recptags_pt > a > strong::text').extract()

        item['image_urls'] = response.css('body > div.content_cont > div.content_box > div.lhs_cont > div.mid_cont > div.recp-det-cont > span > div.method-cont > div > img').xpath('@src').extract()

        yield item