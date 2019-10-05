import requests
import urllib2

def cria_link(content):
    links = []
    for line in content.split():
        if "images/pt/ARC/" in line:
			return "https://dailyverses.net/"+line[5:-1]

pagina = requests.get("https://dailyverses.net/pt/versiculo-aleatorio-imagem")
link = cria_link(pagina.content)

img_data = requests.get(link).content
with open('imagem_proverbio.jpg', 'wb') as handler:
    handler.write(img_data)
    
print "bot0125 feito"
