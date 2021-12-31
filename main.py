import telebot
import requests
from pwntools import *
from funcs import *
from pydub import AudioSegment
import pyaudio
import wave
API_TOKEN = 'YOUR_TOKEN_SHOULD_BE_HERE'  # TODO: Вставьте сюда API_TOKEN вашего бота
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, """Привет! Это бот шифровальщик, мне можно написать все, что угодно, после чего указать кодировку, список будет выдан позже.
    В планах добавить работу в чатах, кодировки с ключом и ассиметричные кодировки, но вряд-ли я правда буду им заниматься в ближайшее время, поэтому это на долго.""")
    list1 = ['b64', 'b32', 'b16', 'hex', 'rot13']
    bot.send_message(message.from_user.id, """список указателей на шифровку{}, их надо писать примерно так " b64" в конце сообщения.""".format(list1))

@bot.message_handler(content_types=['text'])
def start(message):
    dict1 = {'b64':'base64', 'b32':'base32', 'b16':'base16', 'hex':'hex', 'rot13':'rot13'}
    try:
        text1 = list(map(message.text.split()))
        xax = dict1[text1[-1]](*text1[0:len(text1) - 1], sep = ' ')
        #encoding = list(map(message.text.split()))[-1]
        #encoded = dict1[list(map(message.text.split()))[-1]](*list(map(message.text.split()))[0:len(list(map(message.text.split())))-1], sep = ' ')
        bot.send_message(message.from_user.id, xax)
    except:
        bot.send_message(message.from_user.id, 'no pwn please')

@bot.message_handler(content_types=['voice'], update: Update, context: CallbackContext)
def start_message(message):
    #bot.send_message(message.from_user.id, "не работает")
    file = context.bot.getFile(update.message.voice.file_id)
    file.download('./voice.ogg')
    sound = AudioSegment.from_ogg('./voice.ogg')
    sound.export('./voice.wav', format='wav')
    wavefile_name = 'voice.wav'
    wf = wave.open(wavefile_name, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format =
                    p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True)
    full_data = []
    data = wf.readframes(1024)
    while data:
        full_data.append(data)
        data = wf.readframes(1024)
    data = ''.join(full_data)[::-1]
    for i in range(0, len(data), 1024):
        stream.write(data[i:i+1024])

@bot.message_handler(content_types=['document'])
def start_message(message):
    bot.send_message(message.from_user.id, "не работает")


bot.polling()
