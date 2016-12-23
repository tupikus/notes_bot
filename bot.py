"""
Бот, с нотами.
"""

import telebot
import config
import os
import db


bot = telebot.TeleBot(config.token)

#считываем локальные расположения файлов

note_C_l = "SELECT local_note FROM notes_local WHERE name_note IS 'C'"
L_C = db.query(note_C_l)

note_D_l = "SELECT local_note FROM notes_local WHERE name_note IS 'D'"
L_D = db.query(note_D_l)

note_E_l = "SELECT local_note FROM notes_local WHERE name_note IS 'E'"
L_E = db.query(note_E_l)

note_F_l = "SELECT local_note FROM notes_local WHERE name_note IS 'F'"
L_F = db.query(note_F_l)

note_G_l = "SELECT local_note FROM notes_local WHERE name_note IS 'G'"
L_G = db.query(note_G_l)

note_A_l = "SELECT local_note FROM notes_local WHERE name_note IS 'A'"
L_A = db.query(note_A_l)

note_B_l = "SELECT local_note FROM notes_local WHERE name_note IS 'B'"
L_B = db.query(note_B_l)

#считываем file_id из нашей таблицы "notes"

note_C = "SELECT file_id FROM notes WHERE NAME_NOTE IS 'C'"
note_C_id = db.query(note_C)

note_D = "SELECT file_id FROM notes WHERE NAME_NOTE IS 'D'"
note_D_id = db.query(note_D)

note_E = "SELECT file_id FROM notes WHERE NAME_NOTE IS 'E'"
note_E_id = db.query(note_E)

note_F = "SELECT file_id FROM notes WHERE NAME_NOTE IS 'F'"
note_F_id = db.query(note_F)

note_G = "SELECT file_id FROM notes WHERE NAME_NOTE IS 'G'"
note_G_id = db.query(note_G)

note_A = "SELECT file_id FROM notes WHERE NAME_NOTE IS 'A'"
note_A_id = db.query(note_A)

note_B = "SELECT file_id FROM notes WHERE NAME_NOTE IS 'B'"
note_B_id = db.query(note_B)



#получаем информацию об обновлениях
upd = bot.get_updates()
last_upd = upd[-1]
message_from_user = last_upd.message
chat_id = str(message_from_user.chat.id)

#указываем корневую директорию
directory = "C:\\Users\\101\\PycharmProjects\\notbl\\Not"
all_files_in_directory = os.listdir(directory)


@bot.message_handler(content_types = ['text'])
def handle_text(message):
    #рабочий вариант с указанием размещения файла вручную в переменной voice
    if message.text == 'C':
        voice = open('Not\\C.ogg','rb')
        bot.send_chat_action(message.chat.id, 'upload_audio')
        bot.send_audio(message.chat.id, voice)
        voice.close()
    elif message.text == 'C#':
        #в доработке
        bot.send_message(message_from_user.chat.id, 'YO!')
    elif message.text == 'D':
        #вариант с file_id прописанным вручную
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, 'BQADAgADCgADHlPoDHw4LKzatQmbAg')
        #voice.close()
    elif message.text == 'D#':
        #в доработке
        bot.send_message(message.chat.id, 'YO!')
    elif message.text == 'E':
        #нерабочий вариант, со считанным расположением файла из базы данных notes
        voice = open(L_E,'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_voice(message.from_user.id, voice)
        voice.close()
    elif message.text == 'F':
        #нерабочий вариант со считанным file_id из базы данных notes
        voice = note_F_id
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_voice(message.from_user.id, voice)
        voice.close()
    elif message.text == 'F#':
        bot.send_message(message.chat.id, 'YO!')
    elif message.text == 'G':
        #далее я не делал.
        directory = "C:\\Not"
        all_files_in_directory = os.listdir(directory)
        voice = open("C:\\Not\\G.ogg",'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_voice(message.from_user.id, voice)
        voice.close()
    elif message.text == 'G#':
        bot.send_message(message.chat.id, 'YO!')
    elif message.text == 'A':
        directory = "C:\\Not"
        all_files_in_directory = os.listdir(directory)
        voice = open("C:\\Not\\A.ogg",'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_voice(message.from_user.id, voice)
        voice.close()
    elif message.text == 'A#':
        bot.send_message(message.chat.id, 'YO!')
    elif message.text == 'B':
        directory = "C:\\Not"
        all_files_in_directory = os.listdir(directory)
        voice = open("C:\\Not\\B.ogg",'rb')
        file_id = "BQADAgADCAADHlPoDDNkmpYrQYhwAg"
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_voice(message.from_user.id, voice)
        voice.close()
    else:
        bot.send_message(message.chat.id, """
        Информация:
        Для проигрывание ноты, вам требуется ввести её название.
        C - ДО;
        С# - ДО ДИЕЗ;
        D - РЕ;
        D# - РЕ ДИЕЗ;
        E - МИ;
        F - ФА;
        F# - ФА ДИЕЗ;
        G - СОЛЬ;
        G# - СОЛЬ ДИЕЗ;
        A - ЛЯ;
        A# - ЛЯ ДИЕЗ;
        B - СИ.
        """)


bot.polling(none_stop=True, interval=0)







