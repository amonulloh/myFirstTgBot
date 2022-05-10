from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from googletrans import Translator
from googletrans.constants import LANGUAGES
import keyboard
from keyboard import kb_user
from keyboard import kb_lang
from keyboard import kb_lang0
from wiki import Football
from config import TOKEN

tr = Translator()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

leng = 'ru'

active = False


@dp.message_handler(commands=['start', 'back', 'language'])
async def command_start(message: types.Message):
    """
    This async function for command of [/start], [/back], [/language].
    :param message: messenger.text
    :return: message to user
    """
    global active
    active = False
    await bot.send_message(
        message.from_user.id, 'Hi!  Plaese change the language:\n '
                              'Example:  <b><i>en</i></b>', parse_mode='HTML',
        reply_markup=kb_lang)


@dp.message_handler()
async def leagues(message: types.Message):
    """
    This async function responsible for every message from user.
    Bot will read and answer to user
    :param message:
    :return:messege
    """

    # these condition for choosing language
    global leng, active
    for i in kb_lang0:
        if message.text == i:
            message.text = message.text[:2]
    if not active and LANGUAGES.__contains__(message.text):
        leng = message.text
        active = True
        await bot.send_message(
            message.from_user.id, tr.translate('Choose the League:', dest=leng).text,
            reply_markup=kb_user)
    elif not active and not LANGUAGES.__contains__(message.text):
        active = False
        await bot.send_message(
            message.from_user.id, "Wrong language input.\n "
                                  'Example:  <b><i>en</i></b>', parse_mode='HTML',
            reply_markup=kb_lang)

    # this condition for EPL table
    elif active and message.text == keyboard.EPL:
        f = Football('https://en.wikipedia.org/wiki/2021%E2%80%9322_Premier_League', leng)
        f.update()
        await bot.send_message(
            message.from_user.id, tr.translate('Таблица АПЛ🏴󠁧󠁢󠁥󠁮󠁧󠁿:', dest=leng).text,
            reply_markup=kb_user)
        await bot.send_message(message.from_user.id, f.get_rank(),
                               parse_mode='HTML', reply_markup=kb_user)

    # this condition for La Liga table
    elif active and message.text == keyboard.LaLiga:
        f = Football('https://en.wikipedia.org/wiki/2021%E2%80%9322_La_Liga', leng)
        f.update()
        await bot.send_message(
            message.from_user.id, tr.translate('Таблица Ла Лиги🇪🇸:', dest=leng).text,
            reply_markup=kb_user)
        await bot.send_message(message.from_user.id, f.get_rank(),
                               parse_mode='HTML', reply_markup=kb_user)

    # this condition for Seria A table
    elif active and message.text == keyboard.SerieA:
        f = Football('https://en.wikipedia.org/wiki/2021%E2%80%9322_Serie_A', leng)
        f.update()
        await bot.send_message(
            message.from_user.id, tr.translate('Serie A table🇮🇹:', dest=leng).text,
            reply_markup=kb_user)
        await bot.send_message(message.from_user.id, f.get_rank(),
                               parse_mode='HTML', reply_markup=kb_user)

    # this condition for Bunliga table
    elif active and message.text == keyboard.BunLiga:
        f = Football('https://en.wikipedia.org/wiki/2021%E2%80%9322_Bundesliga', leng)
        f.update()
        await bot.send_message(
            message.from_user.id, tr.translate('Bundesligs table🇩🇪:', dest=leng).text,
            reply_markup=kb_user)
        await bot.send_message(message.from_user.id, f.get_rank(),
                               parse_mode='HTML', reply_markup=kb_user)

    # this condition for Ligue 1 table
    elif active and message.text == keyboard.Ligue1:
        f = Football('https://en.wikipedia.org/wiki/2021%E2%80%9322_Ligue_1', leng)
        f.update()
        await bot.send_message(
            message.from_user.id, tr.translate('Ligue 1 table🇫🇷:', dest=leng).text,
            reply_markup=kb_user)
        await bot.send_message(message.from_user.id, f.get_rank(),
                               parse_mode='HTML', reply_markup=kb_user)

    # this condition for status of active after command [/back]
    elif active and message.text == '/back':
        active = False

    # this condition every wrong message from user
    else:
        f = Football('https://en.wikipedia.org/wiki/2021%E2%80%9322_Ligue_1', leng)
        f.update()
        await bot.send_message(message.from_user.id, f.get_error(),
                               parse_mode='HTML', reply_markup=kb_user)


# running bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
