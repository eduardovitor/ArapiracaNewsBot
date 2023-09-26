
# Arapiraca News Bot


## 📖 Descrição

![arapiracanewsbot](arapiracanewsbot.gif)

A ideia por trás do bot é extrair notícias dos principais portais de notícias de Arapiraca: [Diário Arapiraca](https://diarioarapiraca.com.br/), [7 segundos](https://www.7segundos.com.br/arapiraca) e [Já é notícia](https://www.jaenoticia.com.br/). O projeto surgiu da necessidade de facilitar o acesso a notícias de Arapiraca a partir de um único lugar em um formato acessível (mensagens).

## 📁 Estrutura de arquivos

- ```main.py```: arquivo principal do projeto contém todas as funções de funcionamento do bot (funções da API do Telegram e de scraping);

- ```arapiracanews.py```: arquivo que contém todas as funções de scraping;

- ```/test```: diretório que contém testes unitários para funções auxiliares ao scraping;

## 🛠️ Funcionalidades

- Extração de notícias do slideshow do [7 segundos](https://www.7segundos.com.br/arapiraca) por meio do comando ```/7segundos```;
- Extração de notícias do slideshow do [Já é notícia](https://www.jaenoticia.com.br/) por meio do comando ```/jaenoticia```;
- Extração das notícias mais lidas do [Diário Arapiraca](https://diarioarapiraca.com.br/) por meio do comando ```/diarioarapiraca```.



## 📡 Tecnologias utilizadas

<div align="center"> 
<img align="left" height="30" width="30" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"/>
  
</div>
<br/><br/>

## ⏳ Inicialização

Esse projeto foi desenvolvido usando a linguagem de programação [Python](https://www.python.org/) usando as bibliotecas [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) para scraping dos dados dos sites de notícias e a [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/) para execução do bot do Telegram.

O projeto usa testes unitários para garantir a confiabilidade dos dados das notícias por meio das bibliotecas [unittest](https://docs.python.org/3/library/unittest.html) e [validators](https://pypi.org/project/validators/). Além disso, o projeto utiliza um cache TTL (Time to Live) da biblioteca [cachetools](https://pypi.org/project/cachetools/) simples para manter notícias recentes guardadas em memória, evitando assim um consumo excessivo de recursos de rede no servidor onde o bot está executando.

Para detalhes de como contribuir para o projeto, verifique o arquivo [CONTRIBUTING.MD](CONTRIBUTING.MD).

<br/>

## 🤵🤵‍♀️ Colaboradores

No momento, o único colaborador desse projeto sou eu (Eduardo Vítor).

<br/>

## 🔎 Status do Projeto

![Badge em Desenvolvimento](https://img.shields.io/badge/Status-Em%20Desenvolvimento-green)

<br/>

## 📑 Referências

[Python](https://www.python.org/)

[pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)

[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

[unittest](https://docs.python.org/3/library/unittest.html)

[validators](https://pypi.org/project/validators/)

[cachetools](https://pypi.org/project/cachetools/)

[Diário Arapiraca](https://diarioarapiraca.com.br/)

[7 segundos](https://www.7segundos.com.br/arapiraca)

[Já é notícia](https://www.jaenoticia.com.br/)
