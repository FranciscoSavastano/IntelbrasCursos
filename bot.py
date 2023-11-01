from bs4 import BeautifulSoup
from scrapingant_client import ScrapingAntClient
import os, pandas as pd, jinja2, logging

def scraping(pages=1, url=""):
    def criaplanilha(nomes, links, currrow, colrow, currpag, worksheet, workbook, cursoslist, linkslist):
        logging.basicConfig(filename="logfilename.log", level=logging.INFO)
        print("Escrevendo a planilha")
        for i, l in enumerate(nomes):
            tempstring = ""
            for j, col in enumerate(l):
                tempstring += str(nomes[i][j])
                tempstring += " "
            tempstring = tempstring.split("=")
            cursoslist.append(tempstring[1])
            logging.info(f"escrita linha {tempstring[1]} na linha {currrow}")
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
                linkslist.append(linkstr)
                colrow += 1
            

        print("Pagina extraida com sucesso!")
        return worksheet, workbook, currrow, colrow, cursoslist, linkslist

    # cria uma instacia de scraping com api      
    client = ScrapingAntClient(token='1d88dcb8f53f4f47954683c1a583177f')
    #pages = int(input("Insira a quantidade de paginas da pesquisa de cursos: "))
    # Define a url para buscar o conteudo do site
    #url = "https://cursos.intelbras.com.br/portal/layout/927/intelbras/home.asp?V29ya3NwYWNlSUQ9MTI2NSZjRmlsdHJvPSRNb2RvPWdyaWQmRmlsdHJvcyRQYWdpbmE6MSZQb3JQYWdpbmE6MjAmQ2F0ZWdvcmlhc0ZpbHRyYWRhc0AkaWQ9MTImbm9tZT1Db211bmljYSVDMyVBNyVDMyVBM28mY2F0ZWdvcmlhX2lkPTcmY2F0ZWdvcmlhX25vbWU9VW5pZGFkZSZxdGQ9Nzc7JiRpZD05NyZub21lPUdyYXR1aXRvJmNhdGVnb3JpYV9pZD0xNCZjYXRlZ29yaWFfbm9tZT1Db25kaSVDMyVBNyVDMyVBM28mcXRkPTM0OzsmQnVzY2FUZXJtbzpudWxsJlRpcG9GaWx0cmFkbz1Ub2RvcyZXb3Jrc3BhY2VJRDoxMjY1Jmt0X2RpZGF4aXM9dG9w#"
    worksheet = ""
    workbook = ""
    currrow = 1
    colrow = 0
    cursoslist = []
    linkslist = []
    for i in range(int(pages)):
        #url = input(f"Insira a url da pagina {i + 1} de pesquisa de cursos: ")
        print("Inicializando API")
        # renderiza conteudo da web
        print("Extraindo dados da pagina")
        page_content = client.general_request(url).content

        # redige conteudo para texto com BeautifulSoup
        soup = BeautifulSoup(page_content, features= "html5lib")
        #encontre todos elementos da pagina com tag <a> e classe "link-produto", corresponde as grades dos cursos
        textoHTML = soup.find_all("a" ,class_="link-produto")
        segHTML = soup.find_all("h4", class_= "pull-left filtros-aplicados margin-right-10")
        pags = soup.find_all("ul", class_="pagination")
        print(pags)
        for i in range(len(segHTML)):
            segHTMLstr = str(segHTML[i])
            segHTMLstr = segHTMLstr.replace("<", "").replace(">", "").replace("*", "")
            segHTMLstr = segHTMLstr.split()
            print(segHTMLstr[5], segHTMLstr[6])
            if "Gratuito" in segHTMLstr[5]:
                if '"' in segHTMLstr[6]:
                    segstr = str(segHTMLstr[6])
                    segstr = segstr.split('"')
                    segstr = str(segstr[0])
                    print(segstr)
                else:
                    
                    segstr = str(segHTMLstr[6])
            else:
                
                segstr = str(segHTMLstr[5])
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
                

        worksheet, workbook, currrow, colrow, cursoslist, linkslist = criaplanilha(listanomesfix, listalinksfix, currrow, colrow, currpag, worksheet, workbook, cursoslist, linkslist)

    seglist = []
    for i in range(currrow):
        seglist.append(segstr)
    columns=['Segmento','Cursos', 'Links']
    df = pd.DataFrame(list(zip(seglist, cursoslist,linkslist)), columns=columns)
    df.style.hide(axis="index")
    logging.info(df)
    num = 1
    novoarq = False
    while novoarq == False:
        arquivo = os.path.exists(f"{segstr}{num}.xlsx")
        if arquivo == False:
            novoarq = True
            df.to_excel(f'{segstr}{num}.xlsx')
        else:
            num += 1
    print("Arquivo salvo com sucesso!")
    print(f"salvo em {os.getcwd()} nome: {segstr}{num}.xlsx")


if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   scraping()
