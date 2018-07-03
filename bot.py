from telegram.ext import Updater, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent

updater = Updater(token='575993431:AAGeenfDy2sqHNc0V-Upn3RFejK95D43TN8')

dispatcher = updater.dispatcher
cross_icon = "http://images.vfl.ru/ii/1530208114/c3634acc/22286620.png"


def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result


def cross_out(text):
    tilde = '~'
    output = ''
    for word in text.split():
        if word[0] == tilde and word[-1] == tilde:
            word = word[1:-1]
            output = output + strike(word) + ' '
        elif word[0] == tilde and word[-1] != tilde:
            seq = ''
            y = text.find(tilde)
            z = text.find(tilde, y + 1)
            seq = seq + strike(text[y + 1:z])
            output = output + seq + ' '
        elif word[-1] == tilde:
            pass
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
            title=cross_out('Зачеркнуть'),
            input_message_content=InputTextMessageContent(cross_out(query)),
            thumb_url=cross_icon, thumb_width=48, thumb_height=48
        )
    )

    bot.answer_inline_query(update.inline_query.id, results)


inline_cross_handler = InlineQueryHandler(inline_cross)
dispatcher.add_handler(inline_cross_handler)

updater.start_polling(clean=True)

updater.idle()
