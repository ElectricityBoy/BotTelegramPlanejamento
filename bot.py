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
    context.bot.send_message(chat_id=update.effective_chat.id, text='Olá! Eu sou o bot PlanejamentoPET')

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Desculpa. Não entendi o seu comando")

unknown_handler = MessageHandler(Filters.command, unknown)

def sendImage(update,context):
    url='https://i.ibb.co/j8q5J85/planej.jpg'
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)

def help(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Esses são os comandos disponiveis. \n /help  \n /start \n /planej')

"""START THE BOT"""
def main():
    updater = Updater('1620239627:AAFn7BmK9KklQtTr-i7cCeKCqTSBN0FWOyI')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("planej",sendImage))
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",help))
    dp.add_handler(unknown_handler)


updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
updater.bot.setWebhook('https://morning-journey-60251.herokuapp.com/' + TOKEN)

updater.idle()

if __name__ == '__main__':
    main()
