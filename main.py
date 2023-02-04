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
def abrirNoticiasDiario(message):
  response=arapiracanews.comandoNews("Diário Arapiraca News\n\n")
  bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['7segundos'])
def abrirNoticias7segundos(message):
  response=arapiracanews.comandoNews("7 segundos News\n\n")
  bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['jaenoticia'])
def abrirNoticiasJaeNoticia(message):
  response=arapiracanews.comandoNews("Já é notícia News\n\n")
  bot.send_message(message.chat.id, response)

bot.infinity_polling(50)

