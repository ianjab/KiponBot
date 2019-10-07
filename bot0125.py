# coding: UTF-8

import requests, urllib2
import urllib2

def geraLinkImagem(content):
	for line in content.split():
		if "images/pt/ARC/" in line:
			return "https://dailyverses.net/"+line[5:-1]

def getConteudoPagina(url):
	return requests.get(url)

#Encontra a parte da pagina com a imagem
pagina = getConteudoPagina("https://dailyverses.net/pt/versiculo-aleatorio-imagem")

print pagina
#Pega html da pagina da imagem
link_imagem = geraLinkImagem(pagina.content)
print link_imagem
#Pega a imagem
img_data = getConteudoPagina(link_imagem).content
#Salva a imagem
with open('imagem_proverbio.jpg', 'wb') as handler:
    handler.write(img_data)
    
print "Imagem de versículo salva!"
