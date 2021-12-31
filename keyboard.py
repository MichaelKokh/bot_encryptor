from telebot import types

button_1 = types.KeyboardButton('base based')
button_2 = types.KeyboardButton('voice encodings')
button_3 = types.KeyboardButton('other')
main_kb = types.ReplyKeyboardMarkup()
main_kb.add(button_1).add(button_2).add(button_3)

button_4 = types.KeyboardButton('base64')
button_5 = types.KeyboardButton('base32')
button_6 = types.KeyboardButton('base16')
button_7 = types.KeyboardButton('base85')
base_kb = types.ReplyKeyboardMarkup()
base_kb.add(button_4).add(button_5).add(button_6).add(button_7)

button_8 = types.KeyboardButton('reverse')
button_9 = types.KeyboardButton('reverse')
button_10 = types.KeyboardButton('reverse')
voice_kb = types.ReplyKeyboardMarkup()
voice_kb.add(button_8).add(button_9).add(button_10)

button_11 = types.KeyboardButton('rot13')
other_kb = types.ReplyKeyboardMarkup()
other_kb.add(button_11)
