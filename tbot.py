from telegram import update
from telegram.ext import Updater, CommandHandler, MessageHandler
import wikipedia
import os
PORT = int(os.environ.get('PORT', 5000))



def wiki_summary(update, context):
	try:
	#get message from text and give search
		search = wikipedia.summary(update.message.text[12:])
		update.message.reply_text(search)
	except (Exception,wikipedia.exceptions.HTTPTimeoutError, wikipedia.exceptions.PageError, wikipedia.exceptions.RedirectError, wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.WikipediaException) as e:
		print('Error: ', e)

def wiki_page(update, context):
	try:
	#get message from text and give search
		search = wikipedia.page(update.message.text[9:])
		content = search.content
		update.message.reply_text(search.title)
		for x in search.images:
			update.message.reply_text(x)
		if len(content) > 4096:
			for i in range(0, len(content), 4096):
				update.message.reply_text(content[i:i+4096])

		else:
			update.message.reply_text(content)
		for x in search.references[:10]:
			update.message.reply_text(x)


	except (Exception, wikipedia.exceptions.HTTPTimeoutError, wikipedia.exceptions.PageError, wikipedia.exceptions.RedirectError, wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.WikipediaException) as e:
		print('Error: ', e)


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi, i am a bot built by @BandersnatchX64 \n type /help for a list of commands')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('''help: \n/wiki_summary [search query](summary of the search query) \n/wiki_page [search query(full result)]''')


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1441958925:AAGFc8_o25zl23bDLxWMLknordLlPDqZN7M", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("wiki_summary", wiki_summary))
    dp.add_handler(CommandHandler("wiki_page", wiki_page))

    # on noncommand i.e message - echo the message on Telegram

    # log all errors

    # Start the Bot
    updater.start_polling(listen="0.0.0.0",
                          port=int(PORT),
                          url_path="1441958925:AAGFc8_o25zl23bDLxWMLknordLlPDqZN7M")
    updater.bot.setWebhook('https://that-wiki-bot.herokuapp.com/' + "1441958925:AAGFc8_o25zl23bDLxWMLknordLlPDqZN7M")
	# Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
