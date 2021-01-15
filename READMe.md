# Resume

This is a spider that allow you to get from a page in amazon web-app the product name, product price and product image.

## Tools used 

For this project, i used i lot of tools (see requirement file).

## How does web scraping work ?

To see how the spider collect the data from amazon website, you should follow the unstrunction bellow :

### First step : Splash & Docker

In order to install **Splash**, you should have  **Docker** already installed. If you haven’t, install it now with pip:

		`sudo apt install docker.io`

Using docker you can install Splash:

		`sudo docker pull scrapinghub/splash`

Now you can test if Splash is installed properly you have to start Splash server every time you want to use it :

		`sudo docker run -p 8050:8050 scrapinghub/splash`

This command will start **Splash** service on  [http://localhost:8050](http://localhost:8050/)

### Second step : Run Spider

To scrap the data, there are two commandline that you can you them :

```sh
To run only the spider, go to the spiders folder and run :
$ scrapy runspider pspider.py
To run the whole project (All Spiders), go to the shop folder where there are a scrapy.cfg file and run :
$ scrapy crawl myspider
```

## Ressources

Some resources that helped me :

* https://docs.scrapy.org/en/latest/topics/commands.html
* http://scrapingauthority.com/scrapy-javascript





