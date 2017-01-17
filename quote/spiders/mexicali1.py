# -*- coding: utf-8 -*-
import scrapy


class Mexicali1Spider(scrapy.Spider):
    name = "mexicali1"
    allowed_domains = ["comitedevinculacion.com"]
    start_urls = ['http://www.comitedevinculacion.com.mx/directorio.php']
    start_url = 'http://www.comitedevinculacion.com.mx/directorio.php'

    def parse(self, response):
        empresa_html = '//table[contains(@class,"datagrid")]//tr'
        for empresa in response.xpath(empresa_html):

            name = empresa.xpath('./td[1]/text()').extract_first()
            if name is None:
            	continue
            name = name.strip()

            company = empresa.xpath('./td[2]/text()').extract_first().strip()
            position = empresa.xpath('./td[3]/text()').extract_first().strip()
            phone = empresa.xpath('./td[4]/text()').extract_first().strip()
            email = empresa.xpath('./td[5]/text()').extract_first().strip()
            print name, ",", company,",", position, ",",phone,",", email

        url_next = ""
        url = response.xpath('//*[@id="paginador"]//p/a[contains(@href,"page")]/text()').extract()
        url = response.xpath('//*[@id="paginador"]//p/a[contains(@href,"page")]').extract()
        url = response.xpath('//*[@id="paginador"]//p/a/@href').extract()

        url_last = -1
        for url_item in url:
        	previo = url_last
        	url_last = url_item
#        	print url_item

#        print "URL: ", previo, ", ", url_last
        if url_last == previo:
        	print "END OF INFORMATION"
#        	return None
    	else:
    		start_url = 'http://www.comitedevinculacion.com.mx'
    		url_next =  start_url + url_last
#    		print "URL_NEXT: ", url_next
#    		return url_next
    		yield scrapy.Request(url=url_next, callback=self.parse, dont_filter=True)
#            break
    ## End parse

#     def start_requests(self):
# 	    url = 'http://www.comitedevinculacion.com.mx/directorio.php'
# 	    while url != None:
# #	    	yield scrapy.Request(url=url, callback=self.parse)
# 			url = parse(self, url)

