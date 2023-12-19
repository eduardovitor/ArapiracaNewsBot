from bs4 import BeautifulSoup
import requests
import validators

HEADERS = {'User-Agent': """Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
           AppleWebKit/537.36 (KHTML, like Gecko) \
           Chrome/109.0.0.0 Safari/537.36"""}


def remover_aspas_especiais(link):
    """Essa função existe para remover padrões esquisitos de aspas existentes
    em alguns links dos sites de notícias"""
    aspas_especial = "‘"
    aspas_especial2 = "’"
    aspas = "'"
    link_list = list(link)
    for i in range(0, len(link_list)):
        if link_list[i] == aspas_especial:
            link_list[i] = aspas
        if link_list[i] == aspas_especial2:
            link_list[i] = aspas
    fixed_link = "".join(link_list)
    return fixed_link


def diario_arapiraca_news():
    """Scraping de notícias do portal Diário Arapiraca"""
    url = 'https://diarioarapiraca.com.br'
    doc_html = requests.get(url, headers=HEADERS)
    soup_html = BeautifulSoup(doc_html.content, 'lxml')
    noticias_ids = soup_html.findAll('i', class_='numero')
    pacotes = []
    dict = {}
    for noticia_id in noticias_ids:
        link = noticia_id.parent["href"]
        link = remover_aspas_especiais(link)
        titulo = noticia_id.parent.findChild('span').text
        if validar_dados(link, titulo):
            dict = {'link': link, 'titulo': titulo}
            pacotes.append(dict)
    return pacotes if len(pacotes) > 0 else """As notícias mais lidas não estão
                                              disponíveis no site agora.
                                              Tente novamente mais tarde"""


def site_sete_segundos_news():
    """Scraping de notícias do portal 7 segundos"""
    url = 'https://www.7segundos.com.br/arapiraca'
    doc_html = requests.get(url, headers=HEADERS)
    soup_html = BeautifulSoup(doc_html.content, 'lxml')
    noticias = soup_html.find('div', class_='hero-banner-slider')
    tag_links = noticias.find_all('a')
    dict = {}
    pacotes = []
    for tag in tag_links:
        link = tag['href']
        link = link[2:]
        link = remover_aspas_especiais(link)
        titulo = tag.findChild('h1').text
        if validar_dados("https://www.{}".format(link), titulo):
            dict = {'link': link, 'titulo': titulo}
            pacotes.append(dict)
    return pacotes if len(pacotes) > 0 else """Não há notícias no slideshow \
                                            do 7segundos"""


def ja_e_noticia_news():
    """Scraping de notícias do portal Já é notícia"""
    url = 'https://www.jaenoticia.com.br'
    doc_html = requests.get(url, headers=HEADERS)
    soup_html = BeautifulSoup(doc_html.content, 'lxml')
    noticias = soup_html.find('section', class_='section hero-banner')
    slides = noticias.find('div', class_='col-12 col-sm-12 col-md-7')
    tag_links = slides.find_all('a')
    dict = {}
    pacotes = []
    for tag in tag_links:
        link = tag['href']
        link = remover_aspas_especiais(link)
        titulo = tag.findChild('h1').text
        if validar_dados(link, titulo):
            dict = {'link': link, 'titulo': titulo}
            pacotes.append(dict)
    return pacotes if len(pacotes) > 0 else """Não há notícias no slideshow \
                                            do Já é notícia"""


def formatar_msg(pacotes, site):
    if isinstance(pacotes, str):
        return pacotes
    else:
        dic_length = len(pacotes)
        i = 0
        news_report = []
        news_report.append(site)
        while (i < dic_length):
            f_news = f"{pacotes[i]['titulo']}\n\n{pacotes[i]['link']}\n\n"
            news_report.append(f_news)
            i += 1
        msg = "".join(news_report)
    return msg


def validar_dados(link, titulo):
    return validators.url(link) and len(titulo) > 0
