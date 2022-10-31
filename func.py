from pickle import FALSE, TRUE
from telegram import  Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler, CallbackQueryHandler
import logging


ACTION, WORK = range(2)

def start(update, context):
    '''
    Функция приветствует пользователя, создаёт клавиши в телеграмме и предлагает выбрать действие.
    '''
    user = update.message.from_user
    context.bot.send_message(update.effective_chat.id, 'Приветствую вас в калькуляторе.\n' 
    '1 Будем работать.\n' 
    '2 Выход.')
    board = [[InlineKeyboardButton('1. Будем работать.', callback_data = '0')], [InlineKeyboardButton('2. Выход.', callback_data = '1')]]
    update.message.reply_text('Выбери пункт меню:', reply_markup=InlineKeyboardMarkup(board))
    logging.info(f'Бот запущен {user.username} id {user.id}')
    return ACTION

def action(update, context):
    '''
    Функция отслеживает какую клавишу нажал пользователь и направляет выполнение программы.
    '''
    act = update.callback_query.data
    if act == '0':
        context.bot.send_message(update.effective_chat.id, "Введите выражение (пример: 2 + 2) и нажмите ввод: ")
        logging.info('Пользователь выбрал работать')
        return WORK
    elif act == '1':
        context.bot.send_message(update.effective_chat.id, "Пока!")
        logging.info('Пользователь выбрал: Выход.')
        logging.info('Завершение работы.')
        return ConversationHandler.END 

def work(update, context):
    
    data = update.message.text
    print(data)
    item = data.split()
    print(item)
    if len(item) != 3:
        update.message.reply_text('Нужно ввести в формате (2 * 2)')
        return WORK
    
    x = item[0]
    y = item[2]
    znak = item[1]
    
    if type(x) != int or type(y) != int:
        update.message.reply_text('Введены не числа, повторите ввод.')
        return WORK
    
    if znak != '+' or znak != '-' or znak != '*' or znak != '/':
        update.message.reply_text('Введены неверный оператор, повторите ввод.')
        return WORK
    
        
    if znak == '+':
        update.message.reply_text(f'{x} {znak} {y} = {x+y}')        
    elif znak =='-':
        update.message.reply_text(f'{x} {znak} {y} = {x-y}')
    elif znak == '*':
        update.message.reply_text(f'{x} {znak} {y} = {x*y}')
    elif znak == '/':
        update.message.reply_text(f'{x} {znak} {y} = {x/y}')
    context.bot.send_message(update.effective_chat.id, "Введите выражение или команду /cancel для выхода: ")       
    return WORK

def cancel(update, context):
    '''
    Функция принимает от пользователя команду закончить работу и останавливает выполнение программы.
    '''
    context.bot.send_message(update.effective_chat.id, "Пока!")
    logging.info('Завершение работы.')
    return ConversationHandler.END

