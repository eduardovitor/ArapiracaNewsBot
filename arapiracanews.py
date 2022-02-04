from bs4 import BeautifulSoup
import requests

def diarioArapiracaNews():
  url='https://diarioarapiraca.com.br'
  headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.175 Safari/537.36'}
  doc_html=requests.get(url,headers=headers)
  soup_html=BeautifulSoup(doc_html.content,'html.parser')
  noticias_ids=soup_html.findAll('i',class_='numero')
  tags_links_noticias=[]
  pacotes=[]
  dict={}
  for noticia_id in noticias_ids:
    tags_links_noticias.append(noticia_id.parent)
  for tag in tags_links_noticias:
    link=tag['href']
    titulo=tag.findChild('span').text
    dict={'link':link,'titulo':titulo}
    pacotes.append(dict)
  return pacotes


def site_sete_segundos_News():
  url='https://www.7segundos.com.br/arapiraca'
  headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.175 Safari/537.36'}
  doc_html=requests.get(url,headers=headers)
  soup_html=BeautifulSoup(doc_html.content,'html.parser')
  noticias=soup_html.find('div',class_='hero-banner-slider')
  tag_links=noticias.find_all('a')
  dict={}
  pacotes=[]
  for tag in tag_links:
    link=tag['href']
    link=link[2:]
    titulo=tag.findChild('h1').text
    dict={'link':link,'titulo':titulo}
    pacotes.append(dict)
  return pacotes


def jaenoticiaNews():
  url='https://www.jaenoticia.com.br'
  headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.175 Safari/537.36'}
  doc_html=requests.get(url,headers=headers)
  soup_html=BeautifulSoup(doc_html.content,'html.parser')
  noticias=soup_html.find('section',class_='section hero-banner')
  slides=noticias.find('div',class_='col-12 col-sm-12 col-md-7')
  tag_links=slides.find_all('a')
  dict={}
  pacotes=[]
  for tag in tag_links:
    link=tag['href']
    titulo=tag.findChild('h1').text
    dict={'link':link,'titulo':titulo}
    pacotes.append(dict)
  return pacotes


def comandoNews(site):
  if site=='Já é notícia News\n\n':
    pacotes=jaenoticiaNews()
  elif site=='7 segundos News\n\n':
    pacotes=site_sete_segundos_News()
  elif site=='Diário Arapiraca News\n\n':
    pacotes=diarioArapiracaNews()

  dic_length=len(pacotes)
  i=0
  news_report=[]
  news_report.append(site)
  while(i<dic_length):
    news_report.append('{}\n\n{}\n\n'.format(pacotes[i]['titulo'],pacotes[i]['link']))
    i+=1
  msg="".join(news_report)
  return msg
