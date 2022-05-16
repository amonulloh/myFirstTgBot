from aiogram.types import ReplyKeyboardMarkup as Button
from aiogram.types import KeyboardButton as addButton

from googletrans import Translator

tr = Translator()

EPL = ('EPL🏴󠁧󠁢󠁥󠁮󠁧󠁿')
LaLiga = ('La Liga󠁧󠁢󠁥󠁮󠁧󠁿🇪🇸')
SerieA = ('Serie A🇮🇹')
BunLiga = ('Bundesliga🇩🇪')
Ligue1 = ('Ligue 1🇫🇷')
Back = ('/back')

# 🏴󠁧󠁢󠁥󠁮󠁧󠁿 🇪🇸 🇮🇹 🇩🇪 🇫🇷 🇷🇺

b1 = addButton('en🏴󠁧󠁢󠁥󠁮󠁧󠁿')
b2 = addButton('ru🇷🇺')
b3 = addButton('es🇪🇸')
b4 = addButton('de🇩🇪')
b5 = addButton('fr🇫🇷')

btn1 = addButton(EPL)
btn2 = addButton(LaLiga)
btn3 = addButton(SerieA)
btn4 = addButton(BunLiga)
btn5 = addButton(Ligue1)
btn6 = addButton(Back)


kb_user = Button(resize_keyboard=True)
kb_user.row(btn1, btn2).row(btn3, btn4).row(btn5, btn6)

kb_lang = Button(resize_keyboard=True)
kb_lang.row(b1, b2, b3, b4, b5)
kb_lang0 = ['en🏴󠁧󠁢󠁥󠁮󠁧󠁿', 'ru🇷🇺', 'es🇪🇸', 'de🇩🇪', 'fr🇫🇷']





