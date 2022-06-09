# -*- coding: utf-8 -*-
import telebot
import time
import random
import config
import sqlite3
from telebot import types

# bot
bot = telebot.TeleBot(config.token)
# other
joinedFile = open("All/id.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()

print('Бот начал свою работу..')


@bot.message_handler(commands=['start'])
def welcome(message):
    people_id = message.chat.id
    ref = message.text[7:]
    if ref:
        with sqlite3.connect('ref.db') as con:
            cur = con.cursor()
            cur.execute(
                "UPDATE users SET ref_to = ref_to + 1, ref_proc = ref_proc + 10 WHERE id_user=?", (ref,))
            con.commit()
            name = message.from_user.first_name
            bot.send_message(ref, str(
                name) + ", перешел по вашей реферальной ссылке.\nВы получите бонус 10% за следующую покупку.")
    else:
        pass
    people_id = message.chat.id
    with open('All/id.txt') as f:
        found = False
        for line in f:
            # Key line: check if `w` is in the line.
            if str(people_id) in str(line):
                found = True
        if not found:
            joinedFile = open("All/id.txt", "a")
            joinedFile.write(str(message.chat.id) + "\n")
            joinedUsers.add(message.chat.id)
    connect = sqlite3.connect('ref.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
		id_user INTEGER,
		ref_to INTEGER,
		ref_proc INTEGER
	)
	""")

    connect.commit()
    people_id = message.chat.id
    cursor.execute(f"SELECT id_user FROM users WHERE id_user = {people_id}")
    data = cursor.fetchone()
    if data is None:
        # add values in fields
        refer = 0
        refer2 = 0
        user_id = message.chat.id
        users_list = [user_id, refer, refer2]
        cursor.execute("INSERT INTO users VALUES (?,?,?);", users_list)
        connect.commit()
    else:
        pass

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    menu1 = types.KeyboardButton("Купить валюту💸")
    menu2 = types.KeyboardButton("Тех. Поддержка👨‍💻")
    menu3 = types.KeyboardButton("Реф. Система👥")

    markup.row(menu1)
    markup.row(menu2, menu3)

    bot.send_message(message.chat.id, "Привет,{0.first_name}.Ты зашел в бота для покупки виртов на разных проектах GTA5 RP\nЯ вывел тебе клавиатуру для удобства".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['Admin', 'admin', 'Adminka', 'AdminMenu'])
def adminka(message):
    if message.from_user.id == config.admin_id:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(
            text="Рассылка 💎", callback_data='Rassilka'))
        keyboard.add(types.InlineKeyboardButton(
            text="Посчитать кол-во пользователей 🗽", callback_data='AllUsers'))
        adminmessage = bot.send_message(
            message.chat.id, "Админ меню успешно открыто! 🗡", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, 'У вас нет доступа')


@bot.message_handler(content_types=['text'])
def main(message):
    if message.chat.type == 'private':
        if message.text == 'Тех. Поддержка👨‍💻':
            bot.send_message(message.chat.id, "Часто задаваемые вопросы:\n\n*Q:* Каким способ передаются вирты?\n*A:* Вирты передаются приватным способом через багажник машины. Так они теряются и отследить их невозможно.\n\n*Q:* Часто ли банят людей за покупку виртов?\n*A:* У нас очень много покупателей и пока ни одной жалобы на бан не было\n\n*Q:* Я оплатил счет, что мне делать дальше?\n*A:* С вами свяжутся по ,указанным вами, контактами\n\nЕсли у вас возникли вопросы/проблемы, вы можете обратиться по контактам: TG: " + config.support)
        if message.text == 'Купить валюту💸':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("GTA5RP | 200р")
            menu2 = types.KeyboardButton("Majestic | 70р")
            menu3 = types.KeyboardButton("RedAge | 40р")
            menu4 = types.KeyboardButton("Arizona RP | 30р")
            menu5 = types.KeyboardButton("Radmir RP | 10р")
            menu6 = types.KeyboardButton("FiveLive | 40р")

            markup.row(menu1, menu2, menu3)
            markup.row(menu4, menu5, menu6)

            bot.send_message(message.chat.id, "Выбери игровой проект, используя клавиатуру.\n`Рядом указана цена за 100k`",
                             reply_markup=markup, parse_mode="Markdown")
        if message.text == 'Реф. Система👥':
            connect = sqlite3.connect('ref.db')
            cursor = connect.cursor()
            user_id = message.chat.id
            cursor.execute("SELECT * FROM users WHERE id_user=?", (user_id,))
            result_ref = cursor.fetchone()
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton(
                "У вас " + str(result_ref[1]) + " рефералов")
            menu2 = types.KeyboardButton(
                "Ваш бонус - " + str(result_ref[2]) + "%")
            markup.row(menu1, menu2)
            id_ = message.chat.id
            bot.send_message(message.chat.id, "У нас действует реферальная система.\nЗа каждого приведенного человека вы будете\nполучать 10% виртов от покупки\nВот Ваша персональная ссылка:\nhttps://t.me/" +
                             str(config.bot_name) + "?start=" + str(id_), reply_markup=markup)
        if message.text == 'GTA5RP | 200р':
            global cena
            cena = ("200")
            global project
            project = ("GTA5RP")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("Downtown")
            menu2 = types.KeyboardButton("StrawBerry")
            menu3 = types.KeyboardButton("VineWood")
            menu4 = types.KeyboardButton("BlackBerry")
            menu5 = types.KeyboardButton("InSquad")
            menu6 = types.KeyboardButton("Sunrise")
            menu7 = types.KeyboardButton("Richman")
            menu8 = types.KeyboardButton("Eclipse")
            menu9 = types.KeyboardButton("LaMesa")

            markup.row(menu1, menu2, menu3)
            markup.row(menu4, menu5, menu6)
            markup.row(menu7, menu8, menu9)

            bot.send_message(message.chat.id, "Выбери сервер проекта *GTA5RP*, на котором Вы играете.",
                             reply_markup=markup, parse_mode="Markdown")
        if message.text == 'Downtown':
            global ServerInfa
            ServerInfa = "Downtown"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("100000")
            menu2 = types.KeyboardButton("500000")
            menu3 = types.KeyboardButton("1000000")
            markup.row(menu1, menu2, menu3)
            bot.send_message(
                message.chat.id, "Введите количество виртов,которое вы хотите купить или воспользуйтесь клавиатурой.", reply_markup=markup)
        if message.text == 'StrawBerry':
            ServerInfa = "StrawBerry"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("100000")
            menu2 = types.KeyboardButton("500000")
            menu3 = types.KeyboardButton("1000000")
            markup.row(menu1, menu2, menu3)
            bot.send_message(
                message.chat.id, "Введите количество виртов,которое вы хотите купить или воспользуйтесь клавиатурой.", reply_markup=markup)
        if message.text == 'VineWood':
            ServerInfa = "VineWood"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("100000")
            menu2 = types.KeyboardButton("500000")
            menu3 = types.KeyboardButton("1000000")
            markup.row(menu1, menu2, menu3)
            bot.send_message(
                message.chat.id, "Введите количество виртов,которое вы хотите купить или воспользуйтесь клавиатурой.", reply_markup=markup)
        if message.text == 'BlackBerry':
            ServerInfa = "BlackBerry"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("100000")
            menu2 = types.KeyboardButton("500000")
            menu3 = types.KeyboardButton("1000000")
            markup.row(menu1, menu2, menu3)
            bot.send_message(
                message.chat.id, "Введите количество виртов,которое вы хотите купить или воспользуйтесь клавиатурой.", reply_markup=markup)
        if message.text == 'InSquad':
            ServerInfa = "InSquad"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("100000")
            menu2 = types.KeyboardButton("500000")
            menu3 = types.KeyboardButton("1000000")
            markup.row(menu1, menu2, menu3)
            bot.send_message(
                message.chat.id, "Введите количество виртов,которое вы хотите купить или воспользуйтесь клавиатурой.", reply_markup=markup)
        if message.text == 'Sunrise':
            ServerInfa = "Sunrise"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("100000")
            menu2 = types.KeyboardButton("500000")
            menu3 = types.KeyboardButton("1000000")
            markup.row(menu1, menu2, menu3)
            bot.send_message(
                message.chat.id, "Введите количество виртов,которое вы хотите купить или воспользуйтесь клавиатурой.", reply_markup=markup)
        if message.text == 'Richman':
            ServerInfa = "Richman"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("100000")
            menu2 = types.KeyboardButton("500000")
            menu3 = types.KeyboardButton("1000000")
            markup.row(menu1, menu2, menu3)
            bot.send_message(
                message.chat.id, "Введите количество виртов,которое вы хотите купить или воспользуйтесь клавиатурой.", reply_markup=markup)
        if message.text == 'Eclipse':
            ServerInfa = "Eclipse"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("100000")
            menu2 = types.KeyboardButton("500000")
            menu3 = types.KeyboardButton("1000000")
            markup.row(menu1, menu2, menu3)
            bot.send_message(
                message.chat.id, "Введите количество виртов,которое вы хотите купить или воспользуйтесь клавиатурой.", reply_markup=markup)
        if message.text == 'LaMesa':
            ServerInfa = "LaMesa"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("100000")
            menu2 = types.KeyboardButton("500000")
            menu3 = types.KeyboardButton("1000000")

            markup.row(menu1, menu2, menu3)

            bot.send_message(
                message.chat.id, "Введите количество виртов,которое вы хотите купить или воспользуйтесь клавиатурой.", reply_markup=markup)
        if message.text == 'Majestic | 70р':
            cena = ("70")
            project = ("Majestic")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("Server #1")
            menu2 = types.KeyboardButton("Server #2")
            menu3 = types.KeyboardButton("Server #3")
            menu4 = types.KeyboardButton("Server #4")

            markup.row(menu1, menu2, menu3)
            markup.row(menu4)

            bot.send_message(message.chat.id, "Выбери сервер проекта *Majestic*, на котором Вы играете.",
                             reply_markup=markup, parse_mode="Markdown")
        if message.text == 'Server #1':
            ServerInfa = "Server #1"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("100000")
            menu2 = types.KeyboardButton("500000")
            menu3 = types.KeyboardButton("1000000")

            markup.row(menu1, menu2, menu3)

            bot.send_message(
                message.chat.id, "Введите количество виртов,которое вы хотите купить или воспользуйтесь клавиатурой.", reply_markup=markup)
        if message.text == 'Server #2':
            ServerInfa = "Server #2"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("100000")
            menu2 = types.KeyboardButton("500000")
            menu3 = types.KeyboardButton("1000000")

            markup.row(menu1, menu2, menu3)

            bot.send_message(
                message.chat.id, "Введите количество виртов,которое вы хотите купить или воспользуйтесь клавиатурой.", reply_markup=markup)
        if message.text == 'Server #3':
            ServerInfa = "Server #3"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("100000")
            menu2 = types.KeyboardButton("500000")
            menu3 = types.KeyboardButton("1000000")

            markup.row(menu1, menu2, menu3)

            bot.send_message(
                message.chat.id, "Введите количество виртов,которое вы хотите купить или воспользуйтесь клавиатурой.", reply_markup=markup)
        if message.text == 'Server #4':
            ServerInfa = "Server #4"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("100000")
            menu2 = types.KeyboardButton("500000")
            menu3 = types.KeyboardButton("1000000")

            markup.row(menu1, menu2, menu3)

            bot.send_message(
                message.chat.id, "Введите количество виртов,которое вы хотите купить или воспользуйтесь клавиатурой.", reply_markup=markup)
        if message.text == 'RedAge | 40р':
            cena = ("40")
            project = ("RedAge")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("Classic")

            markup.row(menu1)

            bot.send_message(message.chat.id, "Выбери сервер проекта *RedAge*, на котором Вы играете.",
                             reply_markup=markup, parse_mode="Markdown")
        if message.text == 'Classic':
            ServerInfa = "Classic"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("100000")
            menu2 = types.KeyboardButton("500000")
            menu3 = types.KeyboardButton("1000000")

            markup.row(menu1, menu2, menu3)

            bot.send_message(
                message.chat.id, "Введите количество виртов,которое вы хотите купить или воспользуйтесь клавиатурой.", reply_markup=markup)
        if message.text == 'Arizona RP | 30р':
            cena = ("30")
            project = ("ArizonaRP")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton('ArizonaV')

            markup.row(menu1)

            bot.send_message(message.chat.id, "Выбери сервер проекта *Arizona RP*, на котором Вы играете.",
                             reply_markup=markup, parse_mode="Markdown")
        if message.text == 'ArizonaV':
            ServerInfa = "ArizonaV"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("100000")
            menu2 = types.KeyboardButton("500000")
            menu3 = types.KeyboardButton("1000000")

            markup.row(menu1, menu2, menu3)

            bot.send_message(
                message.chat.id, "Введите количество виртов,которое вы хотите купить или воспользуйтесь клавиатурой.", reply_markup=markup)
        if message.text == 'Radmir RP | 10р':
            cena = ("10")
            project = ("Radmir RP")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("Server #1")
            menu2 = types.KeyboardButton("Server #2")
            menu3 = types.KeyboardButton("Server #3")

            markup.row(menu1, menu2, menu3)

            bot.send_message(message.chat.id, "Выбери сервер проекта *Radmir RP*, на котором Вы играете.",
                             reply_markup=markup, parse_mode="Markdown")
        if message.text == 'FiveLive | 40р':
            cena = ("40")
            project = ("FiveLive")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("Portland")
            menu2 = types.KeyboardButton("California")
        if message.text == 'Portland':
            ServerInfa = "Portland"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("100000")
            menu2 = types.KeyboardButton("500000")
            menu3 = types.KeyboardButton("1000000")

            markup.row(menu1, menu2, menu3)

            bot.send_message(
                message.chat.id, "Введите количество виртов,которое вы хотите купить или воспользуйтесь клавиатурой.", reply_markup=markup)
        if message.text == 'California':
            ServerInfa = "California"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            menu1 = types.KeyboardButton("100000")
            menu2 = types.KeyboardButton("500000")
            menu3 = types.KeyboardButton("1000000")

            markup.row(menu1, menu2, menu3)

            bot.send_message(
                message.chat.id, "Введите количество виртов,которое вы хотите купить или воспользуйтесь клавиатурой.", reply_markup=markup)
        if message.text == '100000':
            global Colvo
            Colvo = (" 100000 + бонус 10000")
            msg = bot.send_message(
                message.chat.id, "Введите свой игровой ник в формате Имя_Фамилия.", reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, decyatka1)
        if message.text == '500000':
            Colvo = (" 500000 + бонус 50000")
            msg = bot.send_message(
                message.chat.id, "Введите свой игровой ник в формате Имя_Фамилия.", reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, decyatka1)
        if message.text == '1000000':
            Colvo = (" 1000000 + бонус 100000")
            msg = bot.send_message(
                message.chat.id, "Введите свой игровой ник в формате Имя_Фамилия.", reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, decyatka1)


def decyatka1(message):
    global Name_Surname
    Name_Surname = message.text
    msg = bot.send_message(
        message.chat.id, 'Введите свои контакты для связи с вами (Discord, Telegram, Vk и тд)')
    bot.register_next_step_handler(msg, decyatka2)


def decyatka2(message):
    Svyaz = message.text
    zaen = random.randint(100000000, 999999999)
    zaen2 = random.randint(10000, 99999)
    markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Быстрая оплата", url="https://qiwi.com/payment/form/99?extra%5B%27account%27%5D=" + str(config.number_qiwi) + "&amountInteger=" + str(
        cena) + "&amountFraction=0&currency=643&extra%5B%27comment%27%5D=" + str(Name_Surname) + " [ " + str(zaen) + " ]%20|%20" + str(zaen2) + "&blocked[0]=sum&blocked[1]=account&blocked[2]=comment")
    ProverkaPlatejki = types.InlineKeyboardButton(
        text="Проверить платеж", callback_data='Platejka')
    markup.add(url_button)
    markup.add(ProverkaPlatejki)
    bot.send_message(message.chat.id, "*Проект*: " + project + "\n*Сервер*: " + ServerInfa + "\n*Игровой ник*: " + Name_Surname + "\n*Кол-во валюты*: " + Colvo +
                     "\n*Контакты для связи*: " + Svyaz + "\n*Сумма к оплате*: " + cena + "\nОплата счета сбросится через 15 минут", reply_markup=markup, parse_mode="Markdown")
    time.sleep(900)
    bot.send_message(message.chat.id, message.from_user.first_name +
                     " , Не обнаружили поступления на счет. Если это ошибка, обратитесь по контактам.")


def RassAll(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(
        text="Рассылка 💎", callback_data='Rassilka'))
    keyboard.add(types.InlineKeyboardButton(
        text="Посчитать кол-во пользователей 🗽", callback_data='AllUsers'))
    text = message.text
    for user in joinedUsers:
        bot.send_message(user, text)
    bot.send_message(
        config.admin_id, "Рассылка была успешно закончена! 💎", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def platejka(call):
    if call.data == 'Platejka':
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                  text="Средства еще не дошли до нас!\nЕсли в течении часа средства не поступят на ваш счет, обратитесь по контактам 🙈")
    if call.data == 'Rassilka':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        msg = bot.send_message(call.message.chat.id,
                               "Введите текст рассылки! 🍫")
        bot.register_next_step_handler(msg, RassAll)
    if call.data == 'AllUsers':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(
            text="Рассылка 💎", callback_data='Rassilka'))
        keyboard.add(types.InlineKeyboardButton(
            text="Посчитать кол-во пользователей 🗽", callback_data='AllUsers'))
        bot.delete_message(call.message.chat.id, call.message.message_id)
        # Opens the file and puts the content of it in the "fhand" variable
        fhand = open('All/id.txt')
        count = 0  # Creates new variable "count" and sets it to 0
        for line in fhand:
            count = count+1  # Increase count by 1 for every line in the file

        bot.send_message(
            call.message.chat.id, "Кол-во пользователей в боте: " + str(count), reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)
