import scrapy
from shop.items import ShopItem
from scrapy_splash import SplashRequest

class Spider(scrapy.Spider):
	name = 'shop'
	page_number = 2
	start_urls = ['https://www.amazon.fr/s?k=python&i=stripbooks&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss']
	#configuring splash 
	def start_requests(self):
		for url in self.start_urls:
			yield SplashRequest(url=url, callback=self.parse, args={"wait":3}, endpoint = 'render.html')

	def parse(self, response):
		item = ShopItem()
		#loop over each item
		for p in response.xpath("//div[@class='sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28']"):
			product_name = p.xpath('.//div[@class="sg-col-inner"]/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span/text()').extract()
			product_price = p.xpath('.//div[@class="sg-col-inner"]/span/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/a/span/span[2]/span[1]/text()').extract()
			product_image = p.xpath('.//div[@class="sg-col-inner"]/span/div/div/div[2]/div[1]/div/div/span/a/div/img/@src').extract()
			#check if the item exist or not
			product_name = product_name if product_name else None
			product_image = product_image if product_image else None
			product_price = product_price if product_price else None
			item["product_name"] = product_name
			item["product_price"] = product_price
			item["product_image"] = product_image
			yield item
