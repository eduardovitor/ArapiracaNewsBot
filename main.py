import telebot
import os
import arapiracanews

API_KEY = os.environ["API_TELEGRAM_BOT"]
bot = telebot.TeleBot(API_KEY)
msg='Olá, eu sou o ArapiracaNewsBot'
msg2='Criado por Eduardo Vítor, meu objetivo é fornecer as principais notícias dos jornais de Arapiraca de forma simples e sem esforço',
msg3='Você têm 4 comandos nesse bot:\n/7segundos: mostra as notícias do slideshow do site 7segundos\n/diarioArapiraca: mostra as notícias mais lidas do site Diário Arapiraca\n/jaenoticia: mostra as notícias do slideshow do site Já é notícia\n/help: mostra novamente essa ajuda\n\nÉ isso, se mantenha informado! :)'

@bot.message_handler(commands=['start'])
def welcome(message):
  bot.send_message(message.chat.id, msg)
  bot.send_message(message.chat.id, msg2)
  bot.send_message(message.chat.id, msg3)

@bot.message_handler(commands=['help'])
def help(message):
  bot.send_message(message.chat.id, msg3)

@bot.message_handler(commands=['diarioArapiraca'])
def abrir_noticias_diario(message):
  response=arapiracanews.comando_news("Diário Arapiraca News\n\n")
  bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['7segundos'])
def abrir_noticias_7segundos(message):
  response=arapiracanews.comando_news("7 segundos News\n\n")
  bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['jaenoticia'])
def abrir_noticias_ja_e_noticia(message):
  response=arapiracanews.comando_news("Já é notícia News\n\n")
  bot.send_message(message.chat.id, response)

bot.infinity_polling(50)

