from telegram.ext import Updater, InlineQueryHandler, TypeHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent

updater = Updater(token='575993431:AAGeenfDy2sqHNc0V-Upn3RFejK95D43TN8')
dispatcher = updater.dispatcher
cross_icon = "http://images.vfl.ru/ii/1530208114/c3634acc/22286620.png"


def strike(text):
    result = ''
    for c in text:
        result = result + '\u0336' + c + '\u0336'
    return result


def cross_out(text):
    output = ''
    for word in text.split(' '):
        if word[0] == '~' and word[-1] == '~':
            word = word[1:-1]
            output = output + ' ' + strike(word) + '  '
        else:
            output = output + word + ' '
    return output


def inline_cross(bot, update):
    query = update.inline_query.query

    if not query:
        return
    results = list()

    results.append(
        InlineQueryResultArticle(
            id=query,
            title='Зачеркнуть', align=center,
            input_message_content=InputTextMessageContent(cross_out(query)),
            thumb_url=cross_icon, thumb_width=48, thumb_height=48

        )
    )

    bot.answer_inline_query(update.inline_query.id, results)


inline_cross_handler = InlineQueryHandler(inline_cross)
dispatcher.add_handler(inline_cross_handler)

updater.start_polling(clean=True)

updater.idle()
