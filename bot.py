from bs4 import BeautifulSoup
from scrapingant_client import ScrapingAntClient
import os, xlsxwriter

def criaplanilha(nomes, links, currrow, colrow, currpag, worksheet, workbook):
    print("Escrevendo a planilha")
    arquivo = os.path.exists("cursos.xlsx")
    if arquivo == False:
        workbook = xlsxwriter.Workbook("cursos.xlsx")
        worksheet = workbook.add_worksheet()
        column = 0
        tempstring = ""
    else:                       
        novoarq = False                                                                             
        num = 1 
        while novoarq == False:
            arquivo = os.path.exists(f"cursos{num}.xlsx")
            if arquivo == False:
                novoarq = True
                if currpag == 0:
                    workbook = xlsxwriter.Workbook(f"cursos{num}.xlsx")
                    worksheet = workbook.add_worksheet()
                    worksheet.write(0, 0, "Cursos")
                    worksheet.write(0, 1, "Links")
                    currrow = 1
                    colrow = 1
                row = 1
                column = 0
                tempstring = ""
            else:
                num += 1
    for i, l in enumerate(nomes):
        tempstring = ""
        for j, col in enumerate(l):
            tempstring += str(nomes[i][j])
            tempstring += " "
        tempstring = tempstring.split("=")
        
        worksheet.write(currrow, column, str(tempstring[1]))
        currrow += 1

    for i, l in enumerate(links):
        tempstring = ""
        for j, col in enumerate(l):
            tempstring += str(links[i][j])
            tempstring += " "
        tempstring = tempstring.split("=")
        tempstring = str(tempstring[1])
        tempstring = tempstring.split('"')
        if i % 2 != 0:
            linkstr = "https://cursos.intelbras.com.br/portal/layout/927/intelbras/"
            linkstr += tempstring[1]
            worksheet.write(colrow, column + 1, str(linkstr))
            colrow += 1
        
        
    print("Pagina extraida com sucesso!")
    return worksheet, workbook, currrow, colrow

# cria uma instacia de scraping com api      
client = ScrapingAntClient(token='1d88dcb8f53f4f47954683c1a583177f')
pages = int(input("Insira a quantidade de paginas da pesquisa de cursos: "))
# Define a url para buscar o conteudo do site
#url = "https://cursos.intelbras.com.br/portal/layout/927/intelbras/home.asp?V29ya3NwYWNlSUQ9MTI2NSZjRmlsdHJvPSRNb2RvPWdyaWQmRmlsdHJvcyRQYWdpbmE6MSZQb3JQYWdpbmE6MjAmQ2F0ZWdvcmlhc0ZpbHRyYWRhc0AkaWQ9MTImbm9tZT1Db211bmljYSVDMyVBNyVDMyVBM28mY2F0ZWdvcmlhX2lkPTcmY2F0ZWdvcmlhX25vbWU9VW5pZGFkZSZxdGQ9Nzc7JiRpZD05NyZub21lPUdyYXR1aXRvJmNhdGVnb3JpYV9pZD0xNCZjYXRlZ29yaWFfbm9tZT1Db25kaSVDMyVBNyVDMyVBM28mcXRkPTM0OzsmQnVzY2FUZXJtbzpudWxsJlRpcG9GaWx0cmFkbz1Ub2RvcyZXb3Jrc3BhY2VJRDoxMjY1Jmt0X2RpZGF4aXM9dG9w#"
worksheet = ""
workbook = ""
currrow = 1
colrow = 0
for i in range(int(pages)):
    url = input(f"Insira a url da pagina {i + 1} de pesquisa de cursos: ")
    print("Inicializando API")
    # renderiza conteudo da web
    print("Extraindo dados da pagina")
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
    currpag = i
    for i in range(len(textoHTML)):
        
        fixedstring = str(textoHTML[i])
        fixedstring = fixedstring.replace("<", "").replace(">", "").replace("*", "")
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
        
    listanomesfix = [] 
    for i in listanomes: 
        if i not in listanomesfix: 
            listanomesfix.append(i) 

    listalinksfix = [] 
    for i in listalinks: 
        if i not in listalinksfix: 
            listalinksfix.append(i) 
            

    worksheet, workbook, currrow, colrow = criaplanilha(listanomesfix, listalinksfix, currrow, colrow, currpag, worksheet, workbook)

workbook.close()
print("Arquivo salvo com sucesso!")


