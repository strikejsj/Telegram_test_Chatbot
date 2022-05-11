from tracemalloc import start
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from pyowm import OWM
from emoji import emojize
import main

# OpenWeatherMap
owm = OWM('YOUR OWN OWM API Key')  # You MUST provide a valid API key
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Seoul, KR') # CITY, COUNTRY
cur_weather = observation.weather

# Updater
updater = Updater(main.api_key)
dispatcher = updater.dispatcher
updater.start_polling()

# Welcome Chat
def hello(bot, update):
    chat_id = update.message.chat_id
    user = update.message.from_user
    bot.sendMessage(chat_id = chat_id, text = str(user.first_name) + '아~ 심심해ㅠㅠ')

# User Guide Message
def helpme(bot, update):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id = chat_id, text = '이런 거 궁금하지 않아?\n1. 뭐하고 있을까?\n2. 애정표현 좋아할까?\n3. 여행 얘기나\n4. 자기 전 인사,\n5. 날씨가 궁금할 때!\n6. 보고 싶다던가\n7. 등등!')
# dispatcher.add_handler(hello)
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', helpme))

# All Reactions!

# Ver 12.0
#def handler(bot, update):

# Ver 13.0
def handler(update, context):
    text = update.message.text
    bot = context.bot
    chat_id = update.message.chat_id

    if '모해' in text:
        #update.message.reply_text('니 생각ㅎㅎ')
        bot.send_message(chat_id = chat_id, text = '니 생각ㅎㅎ')
    elif '뭐해' in text:
        #update.message.reply_text('니 생각ㅎㅎ')
        bot.send_message(chat_id = chat_id, text = '니 생각ㅎㅎ')
    elif '머해' in text:
        bot.send_message(chat_id = chat_id, text = '니 생각ㅎㅎ')
    elif '사랑해' in text:
        bot.send_message(chat_id = chat_id, text = emojize('나도 사랑해:heart:', use_aliases = True))
    elif '여행' in text:
        bot.send_photo(chat_id = chat_id, photo = open('img/profile2.jpg', 'rb'))
        bot.send_message(chat_id = chat_id, text = emojize('여행가서 찍었지롱:ghost:', use_aliases = True))
    elif '보고' in text:
        bot.send_photo(chat_id = chat_id, photo = open('img/IMG_2020.jpg', 'rb'))
        bot.send_message(chat_id = chat_id, text = emojize('짠~', use_aliases = True))
    elif '심심' in text:
        bot.send_message(chat_id = chat_id, text = emojize('집 앞으로 나와:wink:', use_aliases = True))
    elif '아잉' in text:
        bot.send_message(chat_id = chat_id, text = emojize('아잉:heart_eyes:', use_aliases = True))
    elif '잘자' in text:
        bot.send_message(chat_id = chat_id, text = emojize('자기 싫은데:sob:', use_aliases = True))
    elif '꿈 꿔' in text:
        bot.send_message(chat_id = chat_id, text = emojize('내 꿈 꿔야해!!:kissing_smiling_eyes:', use_aliases = True))
    elif '날씨' in text:
        temp = cur_weather.temperature('celsius')["temp"]
        comment = ''
        if temp >= 29:
            comment = emojize('녹아쪄요:rage:', use_aliases = True)
        elif temp >= 15:
            comment = emojize('너랑 같이 놀러가구싶당:blush:', use_aliases = True)
        elif temp >= 5:
            comment = emojize('달달달:open_mouth:', use_aliases = True)
        else:
            comment = emojize('와서 나좀 안아줘:hatched_chick:', use_aliases = True)
        bot.send_message(chat_id = chat_id, text = '지금 ' + str(temp) + '도래! ' + comment)
    else:
        #bot.send_message(chat_id = chat_id, text = '머라구??')
        # Repeat the user's message
        bot.send_message(chat_id = chat_id, text = text)

# Add handler
echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
