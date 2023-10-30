from bs4 import BeautifulSoup
from scrapingant_client import ScrapingAntClient
import os, xlsxwriter, cleantext

def criaplanilha(nomes, links):
    arquivo = os.path.exists("cursos.xlsx")
    if arquivo == False:
        workbook = xlsxwriter.Workbook("teste.xlsx")
        worksheet = workbook.add_worksheet()
        row = 0
        column = 0
        tempstring = ""
        print(nomes)
        
        for i, l in enumerate(nomes):
            tempstring = ""
            for j, col in enumerate(l):
                tempstring += str(nomes[i][j])
                tempstring += " "
            tempstring = tempstring.split("=")
            worksheet.write(i, column, str(tempstring[1]))
        #for i in range(len(links)):
         #   for j in range(len(links[i])):
          #      worksheet.write(row, col + 1, links[i][j])
           # row += 1
        #worksheet.write(row, 0, 'Total')
        #worksheet.write(row, 1, '=SUM(B1:B4)')
        workbook.close()
    
# Define a url para buscar o conteudo do site
url = "https://cursos.intelbras.com.br/portal/layout/927/intelbras/home.asp?V29ya3NwYWNlSUQ9MTI2NSZjRmlsdHJvPSRNb2RvPWdyaWQmRmlsdHJvcyRQYWdpbmE6MSZQb3JQYWdpbmE6MjAmQ2F0ZWdvcmlhc0ZpbHRyYWRhc0AkaWQ9MTImbm9tZT1Db211bmljYSVDMyVBNyVDMyVBM28mY2F0ZWdvcmlhX2lkPTcmY2F0ZWdvcmlhX25vbWU9VW5pZGFkZSZxdGQ9Nzc7JiRpZD05NyZub21lPUdyYXR1aXRvJmNhdGVnb3JpYV9pZD0xNCZjYXRlZ29yaWFfbm9tZT1Db25kaSVDMyVBNyVDMyVBM28mcXRkPTM0OzsmQnVzY2FUZXJtbzpudWxsJlRpcG9GaWx0cmFkbz1Ub2RvcyZXb3Jrc3BhY2VJRDoxMjY1Jmt0X2RpZGF4aXM9dG9w#"

# cria uma instacia de scaping com api
client = ScrapingAntClient(token='1d88dcb8f53f4f47954683c1a583177f')

# renderiza conteudo da web
page_content = client.general_request(url).content

# redige conteudo para texto com BeautifulSoup
soup = BeautifulSoup(page_content, features= "html5lib")
#encontre todos elementos da pagina com tag <a> e classe "link-produto", corresponde as grades dos cursos
textoHTML = soup.find_all("a" ,class_="link-produto")
#itera entre elementos da pagina, cada elemento corresponde a um curso mostrado na pagina, cada um possui link e nome
listaresultado = []
fim = False
j = 0
listanomes = []
listalinks = []
for i in range(len(textoHTML)):
    
    fixedstring = str(textoHTML[i])
    fixedstring = fixedstring.replace("<", "").replace(">", "").replace("*", "").replace("?", "")
    fixedstring = fixedstring.split()
    n = 3
    tempnomelist = []
    templinklist = []
    
    x = range(n, len(fixedstring))
    for n in x:
        if "href" not in fixedstring[n]:
            
            tempnomelist.append(fixedstring[n])
        else:
            
            templinklist.append(fixedstring[n])
            break
        n += 1
    listanomes.append(tempnomelist)
    listalinks.append(templinklist)
    
    #listaresultado.append(fixedstring[])
    #listaresultado.append(fixedstring[3])

listanomesfix = [] 
for i in listanomes: 
    if i not in listanomesfix: 
        listanomesfix.append(i) 

listalinksfix = [] 
for i in listalinks: 
    if i not in listalinksfix: 
        listalinksfix.append(i) 
        

criaplanilha(listanomesfix, listalinksfix)



