from bs4 import BeautifulSoup
from scrapingant_client import ScrapingAntClient

# Define a url para buscar o conteudo do site
url = "https://cursos.intelbras.com.br/portal/layout/927/intelbras/home.asp?V29ya3NwYWNlSUQ9MTI2NSZjRmlsdHJvPSRNb2RvPWdyaWQmRmlsdHJvcyRQYWdpbmE6MSZQb3JQYWdpbmE6MjAmQ2F0ZWdvcmlhc0ZpbHRyYWRhc0AkaWQ9MTImbm9tZT1Db211bmljYSVDMyVBNyVDMyVBM28mY2F0ZWdvcmlhX2lkPTcmY2F0ZWdvcmlhX25vbWU9VW5pZGFkZSZxdGQ9Nzc7JiRpZD05NyZub21lPUdyYXR1aXRvJmNhdGVnb3JpYV9pZD0xNCZjYXRlZ29yaWFfbm9tZT1Db25kaSVDMyVBNyVDMyVBM28mcXRkPTM0OzsmQnVzY2FUZXJtbzpudWxsJlRpcG9GaWx0cmFkbz1Ub2RvcyZXb3Jrc3BhY2VJRDoxMjY1Jmt0X2RpZGF4aXM9dG9w#"

# cria uma instacia de scaping com api
client = ScrapingAntClient(token='1d88dcb8f53f4f47954683c1a583177f')

# renderiza conteudo da web
page_content = client.general_request(url).content

# redige conteudo para texto com BeautifulSoup
soup = BeautifulSoup(page_content, features= "html5lib")
textoHTML = soup.find_all("a" ,class_="link-produto")
#adicionar loop for, para loopear entre cada instancia do catalogo de cursos, cada indice possui link do curso e nome
for i in range(len(textoHTML)):
    print(textoHTML[i], i)


