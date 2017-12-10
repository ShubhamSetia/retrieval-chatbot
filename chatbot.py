from __future__ import print_function
from nltk.chat.util import Chat, reflections

pairs = (
	(r'hi*',
		('Hello','Hey')),
	(r'I am feeling (.*)',
		('What happened?','Why are you feeling %1 ?')),
	(r'I am (.*)',
		('Why do you think you are %1?','Can i help?')),
	(r'No',
		('Ok')),
	(r'Yes',
		('Ok')),
	
)

chatbot =  Chat(pairs, reflections)

def bot_chat():
	print("Welcome")
	chatbot.converse()


if __name__ == '__main__':
	bot_chat()


