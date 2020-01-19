from chatterbot import ChatBot

bot = ChatBot(  'Norman',
			    storage_adapter='chatterbot.storage.SQLStorageAdapter',
			    database_uri='sqlite:///database.sqlite3')


#Response from you chatBot
while True:
	try:
		bot_input = bot.get_response(input())
		print(bot_input)

	except(KeyboardInterrupt,EOFError,SystemExit):
		break

from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train([ 'How are you?',
			    'I am good.',
			    'That is good to hear.',
			    'Thank you',
			    'You are welcome.'
				])