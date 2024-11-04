from typing import Final
from telegram import Update 
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN: Final = '8005365456:AAFSCdjB3JmbUXDvnpqb2Ip37EG_WEIh6Dw'
BOT_USERNAME: Final = '@gojo989bot'

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Yokozo! Thank you for visiting my grave! I am Gojo Satoru...')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Type something or I will attack you..')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')

#Responses 

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'get lost' in processed:
        return 'No you get lost!'

    if 'hello' in processed:
        return 'Hey There!'
    
    if 'i hate you' in processed:
        return 'I am going to attack you!'
    
    if 'i love you' in processed:
        return 'I love you too!'
    
    return 'Please type something I can understand..'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type : str = update.message.chat.type
    text: str =  update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:',response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    #Errors
    app.add_error_handler(error)

    #Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)