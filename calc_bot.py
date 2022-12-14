from telegram import  Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler, CallbackQueryHandler
from config import TOKEN
import logging
from func import*

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher



logging.basicConfig(level=logging.INFO, filename="py_log_book.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s", datefmt="%Y/%m/%d, %H:%M:%S", encoding='UTF-8')

logger = logging.getLogger(__name__)

ACTION, WORK = range(2)

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={ACTION: [CallbackQueryHandler(action)],            
            WORK: [MessageHandler(Filters.text & ~Filters.command, work)],
            },
    fallbacks=[CommandHandler('cancel', cancel)])

dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()

# def message(update, context):
#     text = update.message.text
#     if text.lower() == 'привет':
#         context.bot.send_message(update.effective_chat.id, 'Привет..')
#     else:
#         context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю')


# def unknown(update, context):
#     context.bot.send_message(update.effective_chat.id, f'Шо сказал, не пойму')


# def add(update, context):
#     context.bot.send_message(update.effective_chat.id,
#                              f'введите заголовок задачи')
#     return TITLE#говорит иди дальше

# # entry_points=[CommandHandler('add', add)],
# #     states={

# #


# #TITLE: [MessageHandler(Filters.text, add_title),CommandHandler('no', exit_add)],
# def add_title(update, context):
#     global one_task
#     text = update.message.text
#     if abs(len(text)) > 30:
#         context.bot.send_message(
#             update.effective_chat.id, f'Слишком длинный заголовок')
#         return
#     one_task['title'] = text
#     add_to_temp_file(text)
#     context.bot.send_message(
#             update.effective_chat.id, f'Обновлен заголовок. Сейчас словарь выглядит так: {one_task}')
#     context.bot.send_message(
#             update.effective_chat.id, f'А теперь, товарищ, жду описание')
#     return TASK
# #         TASK: [MessageHandler(Filters.text, add_task),CommandHandler('no', exit_add)]
# def add_task(update, context):
#     global one_task
#     text = update.message.text
#     if abs(len(text)) > 50:
#         context.bot.send_message(
#             update.effective_chat.id, f'Слишком длинный текст задачи')
#     one_task['description'] = text
#     add_to_temp_file(text)
#     write_to_database(one_task)
#     clear_temp_file()
#     context.bot.send_message(
#             update.effective_chat.id, f'Обновлена задача. Сейчас словарь выглядит так: {one_task}')
#     context.bot.send_message(
#             update.effective_chat.id, f'Задача добавлена в базу данных')
#     return ConversationHandler.END

# def exit_add(update,context):
#     context.bot.send_message(
#             update.effective_chat.id, f'Операция прервана')
#     return ConversationHandler.END


# start_handler = CommandHandler('start', start)
# info_handler = CommandHandler('info', info)
# sum_handler = CommandHandler('+', sum)
# conv_handler = ConversationHandler(
#     entry_points=[CommandHandler('add', add)],
#     states={

#         TITLE: [MessageHandler(Filters.text, add_title),CommandHandler('no', exit_add)],
#         TASK: [MessageHandler(Filters.text, add_task),CommandHandler('no', exit_add)]

#         },
#     fallbacks=[CommandHandler('no', exit_add)]
# )

# message_handler = MessageHandler(Filters.text, message)
# unknown_handler = MessageHandler(Filters.command, unknown)  # /game


# dispatcher.add_handler(start_handler)
# dispatcher.add_handler(info_handler)
# dispatcher.add_handler(sum_handler)
# # dispatcher.add_handler(conv_handler)
# # dispatcher.add_handler(unknown_handler)
# # dispatcher.add_handler(message_handler)


# print('server started')
# updater.start_polling()
# updater.idle()
