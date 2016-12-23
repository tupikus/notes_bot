import telebot
import config
import os
import db

bot = telebot.TeleBot(config.token)

directory = "C:\\Users\\101\\PycharmProjects\\notbl\\Not"
all_files_in_directory = os.listdir(directory)

@bot.message_handler(type=['text'])
def find_file_ids(message):
    if message.text == 'yo':
        directory = "C:\\Users\\101\\PycharmProjects\\notbl\\Not"
        all_files_in_directory = os.listdir(directory)
        c = open('Not\\C.ogg', 'rb')
        c_res = bot.send_voice(message.chat.id, c, None)
        print(c_res)
        d = open('Not\\D.ogg', 'rb')
        d_res = bot.send_voice(message.chat.id, d, None)
        print(d_res)
        e = open('Not\\E.ogg', 'rb')
        e_res = bot.send_voice(message.chat.id, e, None)
        print(e_res)
        f = open('Not\\F.ogg', 'rb')
        f_res = bot.send_voice(message.chat.id, f, None)
        print(f_res)
        g = open('Not\\G.ogg', 'rb')
        g_res = bot.send_voice(message.chat.id, g, None)
        print(g_res)
        a = open('Not\\A.ogg', 'rb')
        a_res = bot.send_voice(message.chat.id, a, None)
        print(a_res)
        b = open('Not\\B.ogg', 'rb')
        b_res = bot.send_voice(message.chat.id, b, None)
        print(b_res)

bot.polling(none_stop=True)