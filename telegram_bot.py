import telegram.ext
import requests

Token = '6375038405:AAH6yYP0ERs9VeIRgDnhWbvrpNestWDJPE0'

def api(response):
    response = response.json()[0]
    final = f'Coin = {response.get("coin")}\nName = {response.get("name")}\nPrice = {response.get("price")}\nVolume = {response.get("volume")}'
    return final



updater = telegram.ext.updater.Updater('6375038405:AAH6yYP0ERs9VeIRgDnhWbvrpNestWDJPE0', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Hello welcome to Crypto_Online!")

def help(update, context):
    update.message.reply_text("/start -> Welcome to the bot\n/help -> This message\n/bitcoin -> Shows bitcoin current info\n/dogecoin -> Shows dogecoin current info")

def bitcoin(update, context):
    update.message.reply_text(api(requests.get('https://api.minerstat.com/v2/coins?list=BTC')))

def dogecoin(update, context):
    update.message.reply_text(api(requests.get('https://api.minerstat.com/v2/coins?list=DOGE')))


dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.CommandHandler('bitcoin', bitcoin))
dispatcher.add_handler(telegram.ext.CommandHandler('dogecoin', dogecoin))


updater.start_polling()
updater.idle()