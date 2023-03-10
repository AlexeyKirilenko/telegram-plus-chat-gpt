import telegram.ext
import openai
import os

# Set up the OpenAI API
openai.api_key = os.environ['OPENAI_API_KEY']

# Listen for incoming messages
def respond(update, context):
    message = update.message.text
    response = openai.Completion.create(engine='davinci', prompt=message, max_tokens=100).choices[0].text
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Set up the Telegram bot
updater = telegram.ext.Updater(token=os.environ['TELEGRAM_BOT_TOKEN'], use_context=True)
updater.dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, respond))
updater.start_polling()
updater.idle()
