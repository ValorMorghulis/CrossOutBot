from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import re
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token='575993431:AAGeenfDy2sqHNc0V-Upn3RFejK95D43TN8')
dispatcher = updater.dispatcher

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

def start(bot, update):
     bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query,
            title='зачеркнуть',
            input_message_content=InputTextMessageContent(strike(query))

        )
    )
    bot.answer_inline_query(update.inline_query.id, results)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

updater.start_polling(clean=True)

updater.idle()

cross_out_pattern = re.compile(r'^/~~ [0-9]+$', re.MULTILINE)
