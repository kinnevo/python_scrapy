import scrapy


class MexicaliSpider(scrapy.Spider):
    name = "mexicali"
    allowed_domains = ["comitedevinculacion.com"]
    start_urls = ['http://www.comitedevinculacion.com.mx/directorio.php']
    start_url = 'http://www.comitedevinculacion.com.mx/directorio.php'

    def parse(self, response):
        empresa_html = '//table/td'
        print "Empresa: ", empresa_html
        print "Response: ", response.xpath(empresa_html)
        for empresa in response.xpath(empresa_html):
            print "XXXXX"
            name = empresa.xpath('text()').extract_first()
#            author_link = individual_autor.xpath('./a/@href').extract_first()
            print "Name: ", name
            yield scrapy.Request(start_url, self.parse)
            break
    ## End parse
