from bs4 import BeautifulSoup
import requests

HEADERS={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.59'}


def removerAspasEspeciais(link):
  aspas_especial="‘"
  aspas_especial2="’"
  aspas="'"
  link_list=list(link)
  for i in range(0,len(link_list)):
      if link_list[i]==aspas_especial:
          link_list[i]=aspas
      if link_list[i]==aspas_especial2:
          link_list[i]=aspas
  fixed_link="".join(link_list)
  return fixed_link

def diarioArapiracaNews():
  url='https://diarioarapiraca.com.br'
  doc_html=requests.get(url,headers=HEADERS)
  soup_html=BeautifulSoup(doc_html.content,'html.parser')
  noticias_ids=soup_html.findAll('i',class_='numero')
  pacotes=[]
  dict={}
  for noticia_id in noticias_ids:
    link=noticia_id.parent["href"]
    link=removerAspasEspeciais(link)
    titulo=noticia_id.parent.findChild('span').text
    dict={'link':link,'titulo':titulo}
    pacotes.append(dict)
  return pacotes


def site_sete_segundos_News():
  url='https://www.7segundos.com.br/arapiraca'
  doc_html=requests.get(url,headers=HEADERS)
  soup_html=BeautifulSoup(doc_html.content,'html.parser')
  noticias=soup_html.find('div',class_='hero-banner-slider')
  tag_links=noticias.find_all('a')
  dict={}
  pacotes=[]
  for tag in tag_links:
    link=tag['href']
    link=link[2:]
    link=removerAspasEspeciais(link)
    titulo=tag.findChild('h1').text
    dict={'link':link,'titulo':titulo}
    pacotes.append(dict)
  return pacotes


def jaenoticiaNews():
  url='https://www.jaenoticia.com.br'
  doc_html=requests.get(url,headers=HEADERS)
  soup_html=BeautifulSoup(doc_html.content,'html.parser')
  noticias=soup_html.find('section',class_='section hero-banner')
  slides=noticias.find('div',class_='col-12 col-sm-12 col-md-7')
  tag_links=slides.find_all('a')
  dict={}
  pacotes=[]
  for tag in tag_links:
    link=tag['href']
    link=removerAspasEspeciais(link)
    titulo=tag.findChild('h1').text
    dict={'link':link,'titulo':titulo}
    pacotes.append(dict)
  return pacotes


def comandoNews(site):
  if site=="Já é notícia News\n\n":
    pacotes=jaenoticiaNews()
  elif site=="7 segundos News\n\n":
    pacotes=site_sete_segundos_News()
  elif site=="Diário Arapiraca News\n\n":
    pacotes=diarioArapiracaNews()

  dic_length=len(pacotes)
  i=0
  news_report=[]
  news_report.append(site)
  while(i<dic_length):
    news_report.append("{}\n\n{}\n\n".format(pacotes[i]['titulo'],pacotes[i]['link']))
    i+=1
  msg="".join(news_report)
  return msg
