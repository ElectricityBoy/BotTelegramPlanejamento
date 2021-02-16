from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os

PORT = int(os.environ.get('PORT', 5000))

# LOGGER WITH TOKEN
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
TOKEN= '1620239627:AAFn7BmK9KklQtTr-i7cCeKCqTSBN0FWOyI'

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Olá! Eu sou o bot PlanejamentoPET')

def unknown(update, context):
   update.message.reply_text('Desculpa. Não entendi o seu comando')

unknown_handler = MessageHandler(Filters.command, unknown)

def sendImage(update,context):
    url='https://i.ibb.co/j8q5J85/planej.jpg'
    update.message.reply_photo(chat_id=update.effective_chat.id, photo=url)

def help(update,context):
    update.message.reply_text('Esses são os comandos disponiveis. \n /help  \n /start \n /planej')


def main():
    updater = Updater('1620239627:AAFn7BmK9KklQtTr-i7cCeKCqTSBN0FWOyI', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("planej",sendImage))
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",help))
    dp.add_handler(unknown_handler)

"""START THE BOT"""
updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
updater.bot.setWebhook('https://hidden-inlet-36568.herokuapp.com/' + TOKEN)

updater.idle()

if __name__ == '__main__':
    main()
