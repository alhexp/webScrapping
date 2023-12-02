import scrapy
import pandas
from fake_useragent import UserAgent
from scrapy.linkextractors import LinkExtractor
from urllib import robotparser
import logging

class GithubSpider(scrapy.Spider):
  name = 'github'
  #allowed_domains = ['github.com']
  # con la funcion UserAgent() se obtiene el ultimo user-agent de Chrome
  #user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 uacq'
  user_agent = UserAgent().random
  start_urls = ['https://github.com/search?q=python']
  robots = 'https://github.com/robots.txt'
  error_file = 'error_log.txt'
  data_file = 'data.txt'

  def start_requests(self):
    logging.getLogger('scrapy').setLevel(logging.WARNING)
    yield scrapy.Request(url=self.robots, callback=self.parse_robots)

  def parse_robots(self, response):
    parser = robotparser.RobotFileParser()
    parser.parse(str(response.text).splitlines())
        
    if not parser.can_fetch(self.user_agent, response.url[0]):
      self.logger.warning(f"Crawling is not allowed for {response.url}")
      return
                
    headers = {'User-Agent': self.user_agent}
    for url in self.start_urls:
      yield scrapy.Request(url=url, headers=headers, callback=self.parse)

  def parse(self, response):
    #xll = LinkExtractor()
    #for xl in xll.extract_links(response):
      #print(xl)
    
    for public in response.xpath("//div[@class='repo-list']//ul/li").extract()[:10]:
      # se muestra el nombre
      print("nombre>>>>>", public.css(".mb-1").xpath(".//p/text()").extract())
      # se muestra el numero de estrellas
      print("estrellas>>", public.css(".Link--muted").xpath(".//a/text()").extract())
      # se muestra el numero de issues
      print("issues>>>>>", public.css(".Link--muted.f6").xpath(".//a/text()").extract())
      # se obtiene el href del repositorio
      #print("href>>>>>>>", public.css(".v-align-middle").xpath(".//a/text()").extract())
      href = public.css(".v-align-middle").xpath(".//a/@href").get()
      if href:
        # para mostrar el numero de forks se debe navegar a la pagina del repositorio
        # para obtener el numero de forks
        repo_url = response.urljoin(href)
        yield response.follow(repo_url, self.parse_repository)        

  def parse_repository(self, response):
    # se muestra el número de forks
    print("forks>>>>>>", response.css("span[id='repo-network-counter']::text").get())

