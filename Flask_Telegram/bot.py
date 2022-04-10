import telegram
import os
from decouple import config, Csv
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from black_telegram import get_info

telegram_bot_token = config("telegram_bot_token") 

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher



# set up the introductory statement for the bot when the /start command is invoked
def subchats(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Black@ Subchats:\nNFTs: https://t.me/+ZIPHvgLOolI0NTkx\nDevs: https://t.me/+k41i3dRF6Q1iZmFh\nINTROS: https://t.me/+87_rYST1DDpjMWIx\n101: https://t.me/+CrhrvUDrM8g2MjIx")


# set up the introductory statement for the bot when the /start command is invoked
def resources(update, context):
    chat_id = update.effective_chat.id
    if len(update.message.text) > 1:
        # use update message as filter 
        pass
    else:
        # return all resources summarized 
        pass
    context.bot.send_message(chat_id=chat_id, text="Black@NFTs Subchat: https://t.me/+ZIPHvgLOolI0NTkx")


# obtain the information of the word provided and format before presenting.
def get_word_info(update, context):
    word_info =  update.message.text
    word_info = word_info.replace('/', "")
    word_info = word_info.replace('wtf ', "")
    wtfWord = get_info(word_info)
    word = wtfWord['word']
    definition = wtfWord['definition']
    # format the data into a string
    message = f"Word: {word}\n\ndefinition: \n{definition}"

    update.message.reply_text(message)

# run the start function when the user invokes the /start command 
dispatcher.add_handler(CommandHandler("subchats", subchats))


# run the start function when the user invokes the /start command 
#dispatcher.add_handler(CommandHandler("resources", resources))


# run the start function when the user invokes the /start command 
dispatcher.add_handler(CommandHandler("wtf", get_word_info))


updater.start_webhook(listen="0.0.0.0",
                      port=int(os.environ.get('PORT', 5000)),
                      url_path=telegram_bot_token,
                      webhook_url= 'https://blackatbot.herokuapp.com/' + telegram_bot_token
                      )