import telegram
import myHandler

# telegram BotFather에서 새 봇 생성 후 발급되는 api key
api_key = 'YOUR OWN BotFather\'s API Key'

bot = telegram.Bot(token = api_key)

# chat_id = bot.get_updates()[-1].message.chat_id
#chat_id  = 1234567890

# print(chat_id)
