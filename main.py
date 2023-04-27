import os

import logging



from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

import responses

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext

from dotenv import load_dotenv

# Getiing bot token from env file

load_dotenv()

Bot_Token = os.getenv('Bot_Token')

'''

💡Use this version if you deploying it on repl.it

Add the bot token in secretes section

# Getiing bot token from env file

  Bot_Token = os.environ['Bot_Token']

'''

logging.basicConfig(

    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logging.info('Starting Bot...')

# We defined this fuction to use as commands

# all update.message are reply from bots to user

def start(update, context):

    update.message.reply_text(

        "Merhaba ben geveze 😂 \n Grup içinde sizinle sohbet ederim❤️ \n Beni gruba al sizlede sohbet edeyim😝")
         

def cmd(update, context):

    update.message.reply_text(

        '/tldr - TLDR tech news\n/devto-Devto todays popular artical\n/quotes - Random quotest')

def quote(update, context):

    data = get_quote()

    update.message.reply_text(data)

# tldr new

def tldr(update, context):

    keyboard = [

        [

            InlineKeyboardButton("tech", callback_data='tech'),

            InlineKeyboardButton("science", callback_data='science'),

            InlineKeyboardButton("programming", callback_data='programming'),

            InlineKeyboardButton("ship", callback_data='ship'),

            InlineKeyboardButton(

                "miscellaneous", callback_data='miscellaneous')

        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(

        '💡Choose a category from the list below.', reply_markup=reply_markup)

# devto News

def devTo(update: Update, context: CallbackContext) -> None:

    """Sends a message with three inline buttons attached."""

    keyboard = [

        [

            InlineKeyboardButton(

                "Top Articles of the day", callback_data='topArticles'),

            InlineKeyboardButton(

                "Latest Articles", callback_data='latestArticles'),

        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('What would you like to have?',

                              reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:

    """Parses the CallbackQuery and updates the message text."""

    query = update.callback_query

    query.answer()

    # Now we can use context.bot, context.args and query.message

    if query.data == 'topArticles':

        data = devtoTop()

        query.edit_message_text(text=data)

    elif query.data == 'latestArticles':

        data = devtoLatest()

        query.edit_message_text(text=data)

    elif query.data == 'tech':

        tech, science, programming, miscellaneous = get_tldr()

        query.edit_message_text(text=tech)

    elif query.data == 'science':

        tech, science, programming, miscellaneous = get_tldr()

        query.edit_message_text(text=science)

    elif query.data == 'programming':

        tech, science, programming, miscellaneous = get_tldr()

        query.edit_message_text(text=programming)

    elif query.data == 'miscellaneous':

        tech, science, programming, miscellaneous = get_tldr()

        query.edit_message_text(text=miscellaneous)

# Medium Articles

def medium(update, context):

    data = get_medium()

    print(data)

    if len(data) != 0:

        update.message.reply_text(data)

    else:

        update.message.reply_text("try clicking the command again \n /medium")

# Tech Crunch Articles

def techcrunch(update, context):

    start, mid, last = get_techcrunch()

    update.message.reply_text(start)

    update.message.reply_text(mid)

    update.message.reply_text(last)

# HackerNews

def hackerNews(update, context):

    top, more = get_hackerNews()

    update.message.reply_text(top)

    update.message.reply_text(more)

# there two methods to crete functions to get repond from bot this is 2nd one

def socials(update, context):

    context.bot.send_message(chat_id=update.effective_chat.id,

                             text="List of Socails are down below:\n {Github} https://github.com/amrohan\n\n {Twitter} https://twitter.com/rohansalunkhe_\n\n {Instagram} https://www.instagram.com/amrohann\n\n {Email} amrohanx@gmail.com")

def source_code(update, context):

    context.bot.send_message(chat_id=update.effective_chat.id,

                             text="the source code can be accessed here\n {Replit}\n https://replit.com/@amrohan/chatbot")

def handle_message(update, context):

    text = str(update.message.text).lower()

    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response

    response = responses.get_response(text)

    update.message.reply_text(response)

def error(update, context):

    # Logs errors

    logging.error(f'Update {update} caused error {context.error}')

# Run the programms from here

if __name__ == '__main__':

    updater = Updater(Bot_Token, use_context=True)

    dp = updater.dispatcher

    # Commands handler which callback our commands when user ask for it

    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(CommandHandler('help', help))

    dp.add_handler(CommandHandler('cmd', cmd))

    dp.add_handler(CommandHandler('socials', socials))

    dp.add_handler(CommandHandler('source_code', source_code))

    dp.add_handler(CommandHandler('quotes', quote))

    # tldr handler

    dp.add_handler(CommandHandler('tldr', tldr))

    # Dev To

    dp.add_handler(CommandHandler('devto', devTo))

    # Medium

    dp.add_handler(CommandHandler('medium', medium))

    # Tech Crunch Articles

    dp.add_handler(CommandHandler('techcrunch', techcrunch))

    # Hacker News

    dp.add_handler(CommandHandler('hackerNews', hackerNews))

    # Messages

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # CallbackQueryHandler

    dp.add_handler(CallbackQueryHandler(button))

    # Log all errors

    dp.add_error_handler(error)


dp.add_handler(CommandHandler('ship', ship))
async def couple(client, message: Message):
    if message.chat.type == "private":
        await message.reply_text("Grupta Çalıştır.")
        return
    try:
        m = await message.reply("Shipliyom...")
        await asyncio.sleep(1.0)
        humay = get_text(message)
        if not humay:
            humay = "Aşk ❤️:"
        mentions = ""
        list_of_users = []
        async for mentions in client.iter_chat_members(message.chat.id):  
            if not mentions.user.is_bot: 
                list_of_users.append(mentions.user.id)
        if len(list_of_users) < 2:
            await message.reply_text("Yeterli birey yok.")
            return
        m1_id = random.choice(list_of_users)
        m2_id = random.choice(list_of_users)
        while m1_id == m2_id:
            m1_id = random.choice(list_of_users)
        m1_mention = (await client.get_users(m1_id)).mention
        m2_mention = (await client.get_users(m2_id)).mention
        h = f"{humay}\n\n{m1_mention} + {m2_mention} = ❤️"
        await client.send_message(message.chat.id, h)
        await m.delete()
    except Exception as e:
        print(e)
        await message.reply_text(f"Hata: {e}\n\n@mmagneto'ya bildir!")


    

    # Run the bot

    updater.start_polling(1.0)

    # Idle state give bot time to go in idle

    updater.idle()
