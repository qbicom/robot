#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from telegram import (InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, ReplyKeyboardRemove, InputMediaPhoto)
from telegram.ext import (Updater, CommandHandler, InlineQueryHandler, MessageHandler, Filters)
import logging
import pdb

updater = Updater(token='')
dispatcher = updater.dispatcher

def inserter(query):
    conn = mysql.connector.connect(user='root', passwd=' ', host='127.0.0.1', database='databot')
    cursor = conn.cursor()
    query_string = (query)
    cursor.execute(query_string)
    conn.commit()
    cursor.close()

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Yoo Men!')

def admins_list(bot, update):
    admins = bot.getChatAdministrators(chat_id=update.message.chat_id)
    for a in admins:
        bot.send_message(chat_id=update.message.chat_id, text = ("admin list:\n%s" % a.user.username))
        print(type(a.user))

    

    
if __name__ == "__main__":
    # query = "insert into users (username) value ('Andrey')"
    # inserter(query)
    start_handler = CommandHandler('start', start)
    admins_handler = CommandHandler('admins', admins_list)

    dispatcher.add_handler(admins_handler)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
