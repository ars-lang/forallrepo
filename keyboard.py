from telebot import types
from config import *
from pyqiwip2p import QiwiP2P

p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY)
oplatatest = "https://qiwi.com/payment/form/99?amountInteger=1&amountFraction=0&currency=643&extra%5B%27comment%27%5D=5gh3rh&extra%5B%27account%27%5D=79912690945&blocked%5B0%5D=comment&blocked%5B1%5D=account&blocked%5B2%5D=sum"
oplata100r = "https://qiwi.com/payment/form/99?amountInteger=100&amountFraction=0&currency=643&extra%5B%27comment%27%5D=5gh3rh&extra%5B%27account%27%5D=79912690945&blocked%5B0%5D=comment&blocked%5B1%5D=account&blocked%5B2%5D=sum"
oplata150r = "https://qiwi.com/payment/form/99?amountInteger=150&amountFraction=0&currency=643&extra%5B%27comment%27%5D=5gh3rh&extra%5B%27account%27%5D=79912690945&blocked%5B0%5D=comment&blocked%5B1%5D=account&blocked%5B2%5D=sum"
oplata300r = "https://qiwi.com/payment/form/99?amountInteger=300&amountFraction=0&currency=643&extra%5B%27comment%27%5D=5gh3rh&extra%5B%27account%27%5D=79912690945&blocked%5B0%5D=comment&blocked%5B1%5D=account&blocked%5B2%5D=sum"
oplata1000r = "https://qiwi.com/payment/form/99?amountInteger=1000&amountFraction=0&currency=643&extra%5B%27comment%27%5D=5gh3rh&extra%5B%27account%27%5D=79912690945&blocked%5B0%5D=comment&blocked%5B1%5D=account&blocked%5B2%5D=sum"

menuUser = types.ReplyKeyboardMarkup(True)
menuUser.add("👤Профиль", "⁉Помощь", "🔥Покупка").add("📊О боте", "📕Вопросы").add("⚡️Бесплатный Нож⚡️")

sendReq = types.InlineKeyboardMarkup()
sendReq.add(
    types.InlineKeyboardButton(text="Пополнить", callback_data='send'),
    types.InlineKeyboardButton(text="Промокод", callback_data="promokod")
)

support = types.InlineKeyboardMarkup()
support.add(
    types.InlineKeyboardButton(text="Поддержка", url=f'{helper}')
)

buy = types.InlineKeyboardMarkup()
buy.add(
    types.InlineKeyboardButton(text="200 Голды", callback_data="buytap100"),
    types.InlineKeyboardButton(text="300 Голды", callback_data="buytap150"),
    types.InlineKeyboardButton(text="500 Голды", callback_data="buytap300"),
    types.InlineKeyboardButton(text="5000 Голды", callback_data="buytap1000"),
    types.InlineKeyboardButton(text="Бесплатный нож", callback_data="freeknife")
)

done = types.InlineKeyboardMarkup()
done.add(
    types.InlineKeyboardButton(text="Подтвердить", callback_data="donebuy"),
    types.InlineKeyboardButton(text="Отмена", callback_data="cancelbuy")
)

oplata = types.InlineKeyboardMarkup()
oplata.add(
    types.InlineKeyboardButton(text="100 RUB", callback_data='oplata100'),
    types.InlineKeyboardButton(text="150 RUB", callback_data='oplata150'),
    types.InlineKeyboardButton(text="300 RUB", callback_data='oplata300'),
    types.InlineKeyboardButton(text="1000 RUB", callback_data='oplata1000')
)

oplatalinks100 = types.InlineKeyboardMarkup()
oplatalinks100.add(
    types.InlineKeyboardButton(text="Оплатить", url=oplata100r),
    types.InlineKeyboardButton(text="Проверить оплату", callback_data='check')
)

oplatalinks150 = types.InlineKeyboardMarkup()
oplatalinks150.add(
    types.InlineKeyboardButton(text="Оплатить", url=oplata150r),
    types.InlineKeyboardButton(text="Проверить оплату", callback_data='check')
)

oplatalinks300 = types.InlineKeyboardMarkup()
oplatalinks300.add(
    types.InlineKeyboardButton(text="Оплатить", url=oplata300r),
    types.InlineKeyboardButton(text="Проверить оплату", callback_data='check')
)

oplatalinks1000 = types.InlineKeyboardMarkup()
oplatalinks1000.add(
    types.InlineKeyboardButton(text="Оплатить", url=oplata1000r),
    types.InlineKeyboardButton(text="Проверить оплату", callback_data='check')
)

menuAdmin = types.InlineKeyboardMarkup()
menuAdmin1=types.InlineKeyboardButton(text="Фейк реф", callback_data='fakeref')
menuAdmin2=types.InlineKeyboardButton(text="Для проверки платежки", url=oplatatest)
menuAdmin3=types.InlineKeyboardButton(text="Назад", callback_data='gotostart')
menuAdmin4=types.InlineKeyboardButton(text="Изменить текущий промокод", callback_data='editpromocode')
menuAdmin.row(menuAdmin1,menuAdmin2,menuAdmin4)
menuAdmin.row(menuAdmin3)

cancel = types.InlineKeyboardMarkup()
cancel.add(
    types.InlineKeyboardButton(text="Отмена", callback_data='cancel')
)

freeknifebuttons = types.InlineKeyboardMarkup()
freeknifebutton1 = types.InlineKeyboardButton(text="Подписаться", url=url_channel)
freeknifebutton2 = types.InlineKeyboardButton(text="Проверить", callback_data='link_proverka')
freeknifebuttons.row(freeknifebutton1)
freeknifebuttons.row(freeknifebutton2)
