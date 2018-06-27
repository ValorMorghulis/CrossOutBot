from telegram.ext import Updater, InlineQueryHandler, TypeHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import re
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token='575993431:AAGeenfDy2sqHNc0V-Upn3RFejK95D43TN8')
dispatcher = updater.dispatcher

cross_icon = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyYYkxtmc2xOm4oP0UTlXpRCWDshPKzDUWYuwSxXnPO06RUl4nDw"


def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result


def inline_cross(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query,
            title='зачеркнуть',
            input_message_content=InputTextMessageContent(strike(query)),
            thumb_url=cross_icon, thumb_width=48, thumb_height=48

        )
    )
    bot.answer_inline_query(update.inline_query.id, results)


inline_cross_handler = InlineQueryHandler(inline_cross)
dispatcher.add_handler(inline_cross_handler)

updater.start_polling(clean=True)

updater.idle()

# cross_out_pattern = re.compile(r'^/~~ [0-9]+$', re.MULTILINE)
