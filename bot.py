import telebot
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    bot.reply_to(message, "မင်္ဂလာပါ။ ကျွန်တော် အခု မအားလို့ပါ။ နောက်မှ ပြန်လည် ဆက်သွယ်ပေးပါမယ်။")

print("Bot စတင် အလုပ်လုပ်နေပါပြီ...")
bot.infinity_polling()
