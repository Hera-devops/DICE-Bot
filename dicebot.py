import telebot 
from telebot import types
import random 

bot = telebot.TeleBot('REPLACE IT WITH YOUR TOKEN', parse_mode=None)
markup_d6 = types.ReplyKeyboardMarkup(row_width=2)
roll_d6 = types.KeyboardButton('ROLL_DICE')
markup_d6.add(roll_d6)
markup_2d6 = types.ReplyKeyboardMarkup(row_width=2)
roll_2d6 = types.KeyboardButton('ROLL_TWO_DICE')
markup_2d6.add(roll_2d6)
img1 = 0
img2 = 0
photo = ['pics/image1.jpg', 'pics/image2.jpg', 'pics/image3.jpg',
		 'pics/image4.jpg', 'pics/image5.jpg', 'pics/image6.jpg'
		 ]

@bot.message_handler(commands=['start', 'help'])
def start(message):
	bot.send_message(message.chat.id, 'Hello\nAll the types of dice:\nD6-(six sided dice) = /d6\n2D6-(two six sided dice) = /2d6')

@bot.message_handler(commands=['d6'])
def dice_six(message):
	bot.send_message(message.chat.id, 'SIX SIDED DICE', reply_markup=markup_d6)

@bot.message_handler(commands=['2d6'])
def two_dice_six(message):
	bot.send_message(message.chat.id, 'TWO SIX SIDED DICE', reply_markup=markup_2d6)

@bot.message_handler(func=lambda m: True)
def answer(message):
	if message.text.lower() == 'roll_dice':
		img1 = open(photo[random.randint(0,5)], 'rb')
		bot.send_photo(message.chat.id, img1)
	elif message.text.lower() == 'roll_two_dice':
		img1 = open(photo[random.randint(0,5)], 'rb')
		img2 = open(photo[random.randint(0,5)], 'rb')
		bot.send_photo(message.chat.id, img1)
		bot.send_photo(message.chat.id, img2)

bot.polling()
