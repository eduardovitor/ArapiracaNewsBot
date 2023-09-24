import telebot
import os
import arapiracanews
from cachetools import TTLCache

cache = TTLCache(maxsize=10, ttl=1800)

API_KEY = os.environ["API_TELEGRAM_BOT"]
bot = telebot.TeleBot(API_KEY)
msg = 'Olá, eu sou o ArapiracaNewsBot'
msg2 = 'Criado por Eduardo Vítor, meu objetivo é fornecer as principais notícias dos jornais de Arapiraca de forma simples e sem esforço',
msg3 = 'Você têm 4 comandos nesse bot:\n/7segundos: mostra as notícias do slideshow do site 7segundos\n/diarioarapiraca: mostra as notícias mais lidas do site Diário Arapiraca\n/jaenoticia: mostra as notícias do slideshow do site Já é notícia\n/help: mostra novamente essa ajuda\n\nÉ isso, se mantenha informado! :)'

@bot.message_handler(commands=['start'])
def welcome(message):
  bot.send_message(message.chat.id, msg)
  bot.send_message(message.chat.id, msg2)
  bot.send_message(message.chat.id, msg3)

@bot.message_handler(commands=['help'])
def help(message):
  bot.send_message(message.chat.id, msg3)

@bot.message_handler(commands=['diarioarapiraca'])
def abrir_noticias_diario(message):
  if "noticias_diario" in cache:
        noticias = cache["noticias_diario"]
        response = arapiracanews.formatar_msg(noticias,"Diário Arapiraca News\n\n")
  else:
        noticias = arapiracanews.diario_arapiraca_news()
        cache["noticias_diario"] = noticias
        response = arapiracanews.formatar_msg(noticias,"Diário Arapiraca News\n\n")
  bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['7segundos'])
def abrir_noticias_7segundos(message):
  if "noticias_7segundos" in cache:
        noticias = cache["noticias_7segundos"]
        response = arapiracanews.formatar_msg(noticias,"7 segundos News\n\n")
  else:
        noticias = arapiracanews.site_sete_segundos_news()
        cache["noticias_7segundos"] = noticias
        response = arapiracanews.formatar_msg(noticias,"7 segundos News\n\n")
  bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['jaenoticia'])
def abrir_noticias_ja_e_noticia(message):
  if "noticias_jaenoticia" in cache:
        noticias = cache["noticias_jaenoticia"]
        response = arapiracanews.formatar_msg(noticias,"Já é notícia News\n\n")
  else:
        noticias = arapiracanews.ja_e_noticia_news()
        cache["noticias_jaenoticia"] = noticias
        response = arapiracanews.formatar_msg(noticias,"Já é notícia News\n\n")
  bot.send_message(message.chat.id, response)

bot.infinity_polling(50)

