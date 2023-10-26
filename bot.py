from bs4 import BeautifulSoup
from scrapingant_client import ScrapingAntClient

# Define URL with a dynamic web content
url = "https://cursos.intelbras.com.br/portal/layout/927/intelbras/home.asp?V29ya3NwYWNlSUQ9MTI2NSZjRmlsdHJvPSRNb2RvPWdyaWQmRmlsdHJvcyRQYWdpbmE6MSZQb3JQYWdpbmE6MjAmQ2F0ZWdvcmlhc0ZpbHRyYWRhc0AkaWQ9MTImbm9tZT1Db211bmljYSVDMyVBNyVDMyVBM28mY2F0ZWdvcmlhX2lkPTcmY2F0ZWdvcmlhX25vbWU9VW5pZGFkZSZxdGQ9Nzc7JiRpZD05NyZub21lPUdyYXR1aXRvJmNhdGVnb3JpYV9pZD0xNCZjYXRlZ29yaWFfbm9tZT1Db25kaSVDMyVBNyVDMyVBM28mcXRkPTM0OzsmQnVzY2FUZXJtbzpudWxsJlRpcG9GaWx0cmFkbz1Ub2RvcyZXb3Jrc3BhY2VJRDoxMjY1Jmt0X2RpZGF4aXM9dG9w#"

# Create a ScrapingAntClient instance
client = ScrapingAntClient(token='1d88dcb8f53f4f47954683c1a583177f')

# Get the HTML page rendered content
page_content = client.general_request(url).content

# Parse content with BeautifulSoup
soup = BeautifulSoup(page_content)
print(soup.find_all("a"))