import telebot
from telebot import types


bot = telebot.TeleBot('2084630553:AAHR3H2RbBKh-a3mWhO_4S-_GWB8wbEyxDU')

@bot.message_handler(content_types = ['text'])
def any_msg(message):
    markup = types.InlineKeyboardMarkup()
    item0 = types.InlineKeyboardButton('♻️Далее♻️', callback_data = 'yes')
    markup.add(item0)


    photo = open('./img/three.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, '🤖Привет, это автоматизированный бот по продаже карт с балансом, нажми далее, если понимаешь куда в принципе попал.💁‍♂️', reply_markup = markup)


@bot.callback_query_handler(func = lambda call: True)
def callback(call):
   if call.data == 'yes':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       url_item1 = types.InlineKeyboardButton(text = '❓Вопросы / Продавец🛒', url = 'https://t.me/salecards2021')
       url_item2 = types.InlineKeyboardButton(text = '✍️Отзывы📨', url = 'https://t.me/joinchat/7ACqILeszIc4ZWZi')
       item3 = types.InlineKeyboardButton('💵💳Доступные карты💳💵', callback_data = 'cards')

       keyboard.add(url_item1, url_item2, item3)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = '😁Окей, я тебя понял, что именно интересует?🥸🔎', reply_markup = keyboard)

   elif call.data == 'cards':
       keyboard2 = types.InlineKeyboardMarkup(row_width = 1)
       item3 = types.InlineKeyboardButton('💳Тинькофф | '
                                          'Баланс: 2500-9000₽', callback_data='card1')
       item4 = types.InlineKeyboardButton('💳Сбербанк | '
                                          'Баланс: 2000-6000₽', callback_data = 'card2')
       item5 = types.InlineKeyboardButton('💳Альфа-Банк | '
                                          'Баланс: 3000-10000₽', callback_data = 'card3')
       item6 = types.InlineKeyboardButton('💳ВТБ | '
                                          'Баланс: 1500-5500₽', callback_data = 'card4')
       item7 = types.InlineKeyboardButton('💳Карты с балансом(рандом) | '
                                          'Баланс: 1500-3000₽', callback_data='card5')
       item8 = types.InlineKeyboardButton('Назад↩️', callback_data = 'back')

       keyboard2.add(item3, item4, item5, item6, item7, item8)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'Выберите карту📊💶', reply_markup = keyboard2)

   elif call.data == 'back':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       url_item1 = types.InlineKeyboardButton(text='❓Вопросы / Продавец🛒', url='https://t.me/salecardssupport')
       url_item2 = types.InlineKeyboardButton(text='✍️Отзывы📨', url='https://t.me/joinchat/7ACqILeszIc4ZWZi')
       item3 = types.InlineKeyboardButton('💵💳Доступные карты💳💵', callback_data='cards')

       keyboard.add(url_item1, url_item2, item3)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = '😁Окей, я тебя понял, что именно интересует?🥸🔎', reply_markup = keyboard)

#Тинькофф

   elif call.data == 'card1':
       keyboard3 = types.InlineKeyboardMarkup(row_width = 1)
       button1 = types.InlineKeyboardButton('Баланс: 2500 | Цена: 600', callback_data = 'oneT')
       button2 = types.InlineKeyboardButton('Баланс: 4000 | Цена: 900', callback_data = 'twoT')
       button3 = types.InlineKeyboardButton('Баланс: 6500 | Цена: 1300', callback_data = 'threeT')
       button4 = types.InlineKeyboardButton('Баланс: 9000 | Цена: 2000', callback_data = 'fourT')
       button5 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backTchoice')

       keyboard3.add(button1, button2, button3, button4, button5)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'Выберите баланс карты Тинькофф💳', reply_markup = keyboard3)

   elif call.data == 'backTchoice':
       keyboard2 = types.InlineKeyboardMarkup(row_width = 1)
       item3 = types.InlineKeyboardButton('💳Тинькофф | '
                                          'Баланс: 2500-9000₽', callback_data='card1')
       item4 = types.InlineKeyboardButton('💳Сбербанк | '
                                          'Баланс: 2000-6000₽', callback_data='card2')
       item5 = types.InlineKeyboardButton('💳Альфа-Банк | '
                                          'Баланс: 3000-10000₽', callback_data='card3')
       item6 = types.InlineKeyboardButton('💳ВТБ | '
                                          'Баланс: 1500-5500₽', callback_data='card4')
       item7 = types.InlineKeyboardButton('💳Карты с балансом(рандом) | '
                                          'Баланс: 1500-3000₽', callback_data='card5')
       item8 = types.InlineKeyboardButton('Назад↩️', callback_data='back')

       keyboard2.add(item3, item4, item5, item6, item7, item8)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'Выберите карту📊💶', reply_markup=keyboard2)

   elif call.data == 'oneT':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       url_button = types.InlineKeyboardButton(text = '💰Оплатить💰', url = 'https://t.me/joinchat/_zpaI1Oj5TcxMzgy')
       button1 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backT1')

       keyboard.add(url_button, button1)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'К оплате 600₽📲', reply_markup = keyboard)

   elif call.data == 'backT1':
       keyboard3 = types.InlineKeyboardMarkup(row_width = 1)
       button1 = types.InlineKeyboardButton('Баланс: 2500 | Цена: 600', callback_data='oneT')
       button2 = types.InlineKeyboardButton('Баланс: 4000 | Цена: 900', callback_data='twoT')
       button3 = types.InlineKeyboardButton('Баланс: 6500 | Цена: 1300', callback_data='threeT')
       button4 = types.InlineKeyboardButton('Баланс: 9000 | Цена: 2000', callback_data='fourT')
       button5 = types.InlineKeyboardButton('Назад↩️', callback_data='backTchoice')

       keyboard3.add(button1, button2, button3, button4, button5)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'Выберите баланс карты Тинькофф💳', reply_markup=keyboard3)

   elif call.data == 'twoT':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       url_button = types.InlineKeyboardButton(text = '💰Оплатить💰', url = 'https://t.me/joinchat/_zpaI1Oj5TcxMzgy')
       button1 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backT2')

       keyboard.add(url_button, button1)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'К оплате 900₽📲', reply_markup = keyboard)

   elif call.data == 'backT2':
       keyboard3 = types.InlineKeyboardMarkup(row_width = 1)
       button1 = types.InlineKeyboardButton('Баланс: 2500 | Цена: 600', callback_data='oneT')
       button2 = types.InlineKeyboardButton('Баланс: 4000 | Цена: 900', callback_data='twoT')
       button3 = types.InlineKeyboardButton('Баланс: 6500 | Цена: 1300', callback_data='threeT')
       button4 = types.InlineKeyboardButton('Баланс: 9000 | Цена: 2000', callback_data='fourT')
       button5 = types.InlineKeyboardButton('Назад↩️', callback_data='backTchoice')

       keyboard3.add(button1, button2, button3, button4, button5)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'Выберите баланс карты Тинькофф💳', reply_markup=keyboard3)

   elif call.data == 'threeT':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       url_button = types.InlineKeyboardButton(text = '💰Оплатить💰', url = 'https://t.me/joinchat/_zpaI1Oj5TcxMzgy')
       button1 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backT3')

       keyboard.add(url_button, button1)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'К оплате 1300₽📲', reply_markup = keyboard)

   elif call.data == 'backT3':
       keyboard3 = types.InlineKeyboardMarkup(row_width = 1)
       button1 = types.InlineKeyboardButton('Баланс: 2500 | Цена: 600', callback_data='oneT')
       button2 = types.InlineKeyboardButton('Баланс: 4000 | Цена: 900', callback_data='twoT')
       button3 = types.InlineKeyboardButton('Баланс: 6500 | Цена: 1300', callback_data='threeT')
       button4 = types.InlineKeyboardButton('Баланс: 9000 | Цена: 2000', callback_data='fourT')
       button5 = types.InlineKeyboardButton('Назад↩️', callback_data='backTchoice')

       keyboard3.add(button1, button2, button3, button4, button5)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'Выберите баланс карты Тинькофф💳', reply_markup=keyboard3)

   elif call.data == 'fourT':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       url_button = types.InlineKeyboardButton(text = '💰Оплатить💰', url = 'https://t.me/joinchat/_zpaI1Oj5TcxMzgy')
       button1 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backT4')

       keyboard.add(url_button, button1)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'К оплате 2000₽📲', reply_markup = keyboard)

   elif call.data == 'backT4':
       keyboard3 = types.InlineKeyboardMarkup(row_width = 1)
       button1 = types.InlineKeyboardButton('Баланс: 2500 | Цена: 600', callback_data='oneT')
       button2 = types.InlineKeyboardButton('Баланс: 4000 | Цена: 900', callback_data='twoT')
       button3 = types.InlineKeyboardButton('Баланс: 6500 | Цена: 1300', callback_data='threeT')
       button4 = types.InlineKeyboardButton('Баланс: 9000 | Цена: 2000', callback_data='fourT')
       button5 = types.InlineKeyboardButton('Назад↩️', callback_data='backTchoice')

       keyboard3.add(button1, button2, button3, button4, button5)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'Выберите баланс карты Тинькофф💳', reply_markup=keyboard3)

#Сбербанк

   elif call.data == 'card2':
       keyboard3 = types.InlineKeyboardMarkup(row_width = 1)
       button1 = types.InlineKeyboardButton('Баланс: 2000 | Цена: 400', callback_data='oneS')
       button2 = types.InlineKeyboardButton('Баланс: 3500 | Цена: 750', callback_data='twoS')
       button3 = types.InlineKeyboardButton('Баланс: 6000 | Цена: 1100', callback_data='threeS')
       button4 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backSchoice')

       keyboard3.add(button1, button2, button3, button4)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'Выберите баланс карты Сбербанк💳', reply_markup=keyboard3)

   elif call.data == 'backSchoice':
       keyboard2 = types.InlineKeyboardMarkup(row_width = 1)
       item3 = types.InlineKeyboardButton('💳Тинькофф | '
                                          'Баланс: 2500-9000₽', callback_data='card1')
       item4 = types.InlineKeyboardButton('💳Сбербанк | '
                                          'Баланс: 2000-6000₽', callback_data='card2')
       item5 = types.InlineKeyboardButton('💳Альфа-Банк | '
                                          'Баланс: 3000-10000₽', callback_data='card3')
       item6 = types.InlineKeyboardButton('💳ВТБ | '
                                          'Баланс: 1500-5500₽', callback_data='card4')
       item7 = types.InlineKeyboardButton('💳Карты с балансом(рандом) | '
                                          'Баланс: 1500-3000₽', callback_data='card5')
       item8 = types.InlineKeyboardButton('Назад↩️', callback_data='back')

       keyboard2.add(item3, item4, item5, item6, item7, item8)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'Выберите карту📊💶', reply_markup=keyboard2)

   elif call.data == 'oneS':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       url_button = types.InlineKeyboardButton(text = '💰Оплатить💰', url = 'https://t.me/joinchat/_zpaI1Oj5TcxMzgy')
       button1 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backS1')

       keyboard.add(url_button, button1)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'К оплате 400₽📲', reply_markup = keyboard)

   elif call.data == 'backS1':
       keyboard3 = types.InlineKeyboardMarkup(row_width = 1)
       button1 = types.InlineKeyboardButton('Баланс: 2000 | Цена: 400', callback_data='oneS')
       button2 = types.InlineKeyboardButton('Баланс: 3500 | Цена: 750', callback_data='twoS')
       button3 = types.InlineKeyboardButton('Баланс: 6000 | Цена: 1100', callback_data='threeS')
       button4 = types.InlineKeyboardButton('Назад↩️', callback_data='backSchoice')

       keyboard3.add(button1, button2, button3, button4)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'Выберите баланс карты Сбербанк💳', reply_markup=keyboard3)

   elif call.data == 'twoS':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       url_button = types.InlineKeyboardButton(text = '💰Оплатить💰', url = 'https://t.me/joinchat/_zpaI1Oj5TcxMzgy')
       button1 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backS2')

       keyboard.add(url_button, button1)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'К оплате 750₽📲', reply_markup = keyboard)

   elif call.data == 'backS2':
       keyboard3 = types.InlineKeyboardMarkup(row_width = 1)
       button1 = types.InlineKeyboardButton('Баланс: 2000 | Цена: 400', callback_data='oneS')
       button2 = types.InlineKeyboardButton('Баланс: 3500 | Цена: 750', callback_data='twoS')
       button3 = types.InlineKeyboardButton('Баланс: 6000 | Цена: 1100', callback_data='threeS')
       button4 = types.InlineKeyboardButton('Назад↩️', callback_data='backSchoice')

       keyboard3.add(button1, button2, button3, button4)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'Выберите баланс карты Сбербанк💳', reply_markup=keyboard3)

   elif call.data == 'threeS':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       url_button = types.InlineKeyboardButton(text = '💰Оплатить💰', url = 'https://t.me/joinchat/_zpaI1Oj5TcxMzgy')
       button1 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backS3')

       keyboard.add(url_button, button1)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'К оплате 1100₽📲', reply_markup = keyboard)

   elif call.data == 'backS3':
       keyboard3 = types.InlineKeyboardMarkup(row_width = 1)
       button1 = types.InlineKeyboardButton('Баланс: 2500 | Цена: 400', callback_data='oneS')
       button2 = types.InlineKeyboardButton('Баланс: 4500 | Цена: 750', callback_data='twoS')
       button3 = types.InlineKeyboardButton('Баланс: 6000 | Цена: 1100', callback_data='threeS')
       button4 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backSchoice')

       keyboard3.add(button1, button2, button3, button4)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'Выберите баланс карты Сбербанк💳', reply_markup=keyboard3)

#Альфа-Банк

   elif call.data == 'card3':
       keyboard3 = types.InlineKeyboardMarkup(row_width = 1)
       button1 = types.InlineKeyboardButton('Баланс: 3000 | Цена: 600', callback_data='oneA')
       button2 = types.InlineKeyboardButton('Баланс: 4500 | Цена: 900', callback_data='twoA')
       button3 = types.InlineKeyboardButton('Баланс: 7000 | Цена: 1400', callback_data='threeA')
       button4 = types.InlineKeyboardButton('Баланс: 10000 | Цена: 2100', callback_data='fourA')
       button5 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backAchoice')

       keyboard3.add(button1, button2, button3, button4, button5)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'Выберите баланс карты Альфа-Банк💳', reply_markup=keyboard3)

   elif call.data == 'backAchoice':
       keyboard2 = types.InlineKeyboardMarkup(row_width = 1)
       item3 = types.InlineKeyboardButton('💳Тинькофф | '
                                          'Баланс: 2500-9000₽', callback_data='card1')
       item4 = types.InlineKeyboardButton('💳Сбербанк | '
                                          'Баланс: 2000-6000₽', callback_data='card2')
       item5 = types.InlineKeyboardButton('💳Альфа-Банк | '
                                          'Баланс: 3000-10000₽', callback_data='card3')
       item6 = types.InlineKeyboardButton('💳ВТБ | '
                                          'Баланс: 1500-5500₽', callback_data='card4')
       item7 = types.InlineKeyboardButton('💳Карты с балансом(рандом) | '
                                          'Баланс: 1500-3000₽', callback_data='card5')
       item8 = types.InlineKeyboardButton('Назад↩️', callback_data='back')

       keyboard2.add(item3, item4, item5, item6, item7, item8)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'Выберите карту📊💶', reply_markup=keyboard2)

   elif call.data == 'oneA':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       url_button = types.InlineKeyboardButton(text = '💰Оплатить💰', url = 'https://t.me/joinchat/_zpaI1Oj5TcxMzgy')
       button1 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backA1')

       keyboard.add(url_button, button1)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'К оплате 600₽📲', reply_markup = keyboard)

   elif call.data == 'backA1':
       keyboard3 = types.InlineKeyboardMarkup(row_width=1)
       button1 = types.InlineKeyboardButton('Баланс: 3000 | Цена: 600', callback_data='oneA')
       button2 = types.InlineKeyboardButton('Баланс: 4500 | Цена: 900', callback_data='twoA')
       button3 = types.InlineKeyboardButton('Баланс: 7000 | Цена: 1400', callback_data='threeA')
       button4 = types.InlineKeyboardButton('Баланс: 10000 | Цена: 2100', callback_data='fourA')
       button5 = types.InlineKeyboardButton('Назад↩️', callback_data='backAchoice')

       keyboard3.add(button1, button2, button3, button4, button5)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите баланс карты Альфа-Банк💳', reply_markup=keyboard3)

   elif call.data == 'twoA':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       url_button = types.InlineKeyboardButton(text = '💰Оплатить💰', url = 'https://t.me/joinchat/_zpaI1Oj5TcxMzgy')
       button1 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backA2')

       keyboard.add(url_button, button1)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'К оплате 900₽📲', reply_markup = keyboard)

   elif call.data == 'backA2':
       keyboard3 = types.InlineKeyboardMarkup(row_width=1)
       button1 = types.InlineKeyboardButton('Баланс: 3000 | Цена: 600', callback_data='oneA')
       button2 = types.InlineKeyboardButton('Баланс: 4500 | Цена: 900', callback_data='twoA')
       button3 = types.InlineKeyboardButton('Баланс: 7000 | Цена: 1400', callback_data='threeA')
       button4 = types.InlineKeyboardButton('Баланс: 10000 | Цена: 2100', callback_data='fourA')
       button5 = types.InlineKeyboardButton('Назад↩️', callback_data='backAchoice')

       keyboard3.add(button1, button2, button3, button4, button5)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите баланс карты Альфа-Банк💳', reply_markup=keyboard3)

   elif call.data == 'threeA':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       url_button = types.InlineKeyboardButton(text = '💰Оплатить💰', url = 'https://t.me/joinchat/_zpaI1Oj5TcxMzgy')
       button1 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backA3')

       keyboard.add(url_button, button1)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'К оплате 1400₽📲', reply_markup = keyboard)

   elif call.data == 'backA3':
       keyboard3 = types.InlineKeyboardMarkup(row_width=1)
       button1 = types.InlineKeyboardButton('Баланс: 3000 | Цена: 600', callback_data='oneA')
       button2 = types.InlineKeyboardButton('Баланс: 4500 | Цена: 900', callback_data='twoA')
       button3 = types.InlineKeyboardButton('Баланс: 7000 | Цена: 1400', callback_data='threeA')
       button4 = types.InlineKeyboardButton('Баланс: 10000 | Цена: 2100', callback_data='fourA')
       button5 = types.InlineKeyboardButton('Назад↩️', callback_data='backAchoice')

       keyboard3.add(button1, button2, button3, button4, button5)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите баланс карты Альфа-Банк💳', reply_markup=keyboard3)

   elif call.data == 'fourA':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       url_button = types.InlineKeyboardButton(text = '💰Оплатить💰', url = 'https://t.me/joinchat/_zpaI1Oj5TcxMzgy')
       button1 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backA4')

       keyboard.add(url_button, button1)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'К оплате 2100₽📲', reply_markup = keyboard)

   elif call.data == 'backA4':
       keyboard3 = types.InlineKeyboardMarkup(row_width=1)
       button1 = types.InlineKeyboardButton('Баланс: 3000 | Цена: 600', callback_data='oneA')
       button2 = types.InlineKeyboardButton('Баланс: 4500 | Цена: 900', callback_data='twoA')
       button3 = types.InlineKeyboardButton('Баланс: 7000 | Цена: 1400', callback_data='threeA')
       button4 = types.InlineKeyboardButton('Баланс: 10000 | Цена: 2100', callback_data='fourA')
       button5 = types.InlineKeyboardButton('Назад↩️', callback_data='backAchoice')

       keyboard3.add(button1, button2, button3, button4, button5)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите баланс карты Альфа-Банк💳', reply_markup=keyboard3)

#ВТБ

   elif call.data == 'card4':
       keyboard3 = types.InlineKeyboardMarkup(row_width = 1)
       button1 = types.InlineKeyboardButton('Баланс: 1500 | Цена: 400', callback_data='oneV')
       button2 = types.InlineKeyboardButton('Баланс: 3000 | Цена: 650', callback_data='twoV')
       button3 = types.InlineKeyboardButton('Баланс: 5500 | Цена: 1200', callback_data='threeV')
       button4 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backVchoice')

       keyboard3.add(button1, button2, button3, button4)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id = call.message.message_id, text = 'Выберите баланс карты ВТБ💳', reply_markup=keyboard3)

   elif call.data == 'backVchoice':
       keyboard2 = types.InlineKeyboardMarkup(row_width = 1)
       item3 = types.InlineKeyboardButton('💳Тинькофф | '
                                          'Баланс: 2500-9000₽', callback_data='card1')
       item4 = types.InlineKeyboardButton('💳Сбербанк | '
                                          'Баланс: 2000-6000₽', callback_data='card2')
       item5 = types.InlineKeyboardButton('💳Альфа-Банк | '
                                          'Баланс: 3000-10000₽', callback_data='card3')
       item6 = types.InlineKeyboardButton('💳ВТБ | '
                                          'Баланс: 1500-5500₽', callback_data='card4')
       item7 = types.InlineKeyboardButton('💳Карты с балансом(рандом) | '
                                          'Баланс: 1500-3000₽', callback_data='card5')
       item8 = types.InlineKeyboardButton('Назад↩️', callback_data='back')

       keyboard2.add(item3, item4, item5, item6, item7, item8)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id = call.message.message_id, text = 'Выберите карту📊💶', reply_markup=keyboard2)

   elif call.data == 'oneV':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       url_button = types.InlineKeyboardButton(text = '💰Оплатить💰', url = 'https://t.me/joinchat/_zpaI1Oj5TcxMzgy')
       button1 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backV1')

       keyboard.add(url_button, button1)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'К оплате 400₽📲', reply_markup = keyboard)

   elif call.data == 'backV1':
       keyboard3 = types.InlineKeyboardMarkup(row_width = 1)
       button1 = types.InlineKeyboardButton('Баланс: 1500 | Цена: 400', callback_data='oneV')
       button2 = types.InlineKeyboardButton('Баланс: 3000 | Цена: 650', callback_data='twoV')
       button3 = types.InlineKeyboardButton('Баланс: 5500 | Цена: 1200', callback_data='threeV')
       button4 = types.InlineKeyboardButton('Назад↩️', callback_data='backVchoice')

       keyboard3.add(button1, button2, button3, button4)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'Выберите баланс карты ВТБ💳', reply_markup=keyboard3)

   elif call.data == 'twoV':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       url_button = types.InlineKeyboardButton(text = '💰Оплатить💰', url = 'https://t.me/joinchat/_zpaI1Oj5TcxMzgy')
       button1 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backV2')

       keyboard.add(url_button, button1)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'К оплате 650₽📲', reply_markup = keyboard)

   elif call.data == 'backV2':
       keyboard3 = types.InlineKeyboardMarkup(row_width = 1)
       button1 = types.InlineKeyboardButton('Баланс: 1500 | Цена: 400', callback_data='oneV')
       button2 = types.InlineKeyboardButton('Баланс: 3000 | Цена: 650', callback_data='twoV')
       button3 = types.InlineKeyboardButton('Баланс: 5500 | Цена: 1200', callback_data='threeV')
       button4 = types.InlineKeyboardButton('Назад↩️', callback_data='backVchoice')

       keyboard3.add(button1, button2, button3, button4)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'Выберите баланс карты ВТБ💳', reply_markup=keyboard3)

   elif call.data == 'threeV':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       url_button = types.InlineKeyboardButton(text = '💰Оплатить💰', url = 'https://t.me/joinchat/_zpaI1Oj5TcxMzgy')
       button1 = types.InlineKeyboardButton('Назад↩️', callback_data = 'backV3')

       keyboard.add(url_button, button1)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'К оплате 1200₽📲', reply_markup = keyboard)

   elif call.data == 'backV3':
       keyboard3 = types.InlineKeyboardMarkup(row_width = 1)
       button1 = types.InlineKeyboardButton('Баланс: 1500 | Цена: 400', callback_data='oneV')
       button2 = types.InlineKeyboardButton('Баланс: 3000 | Цена: 650', callback_data='twoV')
       button3 = types.InlineKeyboardButton('Баланс: 5500 | Цена: 1200', callback_data='threeV')
       button4 = types.InlineKeyboardButton('Назад↩️', callback_data='backVchoice')

       keyboard3.add(button1, button2, button3, button4)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'Выберите баланс карты ВТБ💳', reply_markup=keyboard3)

#Рандом

   elif call.data == 'card5':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       button1 = types.InlineKeyboardButton('Баланс: 1500-3000 | Цена: 400', callback_data = 'prise')
       button2 = types.InlineKeyboardButton('Назад↩', callback_data = 'backand')

       keyboard.add(button1, button2)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = '🎲Рандомная карта с рандомным балансом🎲', reply_markup = keyboard)

   elif call.data == 'backand':
       keyboard2 = types.InlineKeyboardMarkup(row_width = 1)
       item3 = types.InlineKeyboardButton('💳Тинькофф | '
                                          'Баланс: 2500-9000₽', callback_data='card1')
       item4 = types.InlineKeyboardButton('💳Сбербанк | '
                                          'Баланс: 2000-6000₽', callback_data='card2')
       item5 = types.InlineKeyboardButton('💳Альфа-Банк | '
                                          'Баланс: 3000-10000₽', callback_data='card3')
       item6 = types.InlineKeyboardButton('💳ВТБ | '
                                          'Баланс: 1500-5500₽', callback_data='card4')
       item7 = types.InlineKeyboardButton('💳Карты с балансом(рандом) | '
                                          'Баланс: 1500-3000₽', callback_data='card5')
       item8 = types.InlineKeyboardButton('Назад↩️', callback_data='back')

       keyboard2.add(item3, item4, item5, item6, item7, item8)

       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите карту📊💶', reply_markup=keyboard2)

   elif call.data == 'prise':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       url_button = types.InlineKeyboardButton(text = '💰Оплатить💰', url = 'https://t.me/joinchat/_zpaI1Oj5TcxMzgy')
       button = types.InlineKeyboardButton('Назад↩', callback_data = 'backand2')

       keyboard.add(url_button, button)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'К оплате 400₽📲', reply_markup = keyboard)

   elif call.data == 'backand2':
       keyboard = types.InlineKeyboardMarkup(row_width = 1)
       button1 = types.InlineKeyboardButton('Баланс: 1500-3000 | Цена: 400', callback_data = 'prise')
       button2 = types.InlineKeyboardButton('Назад↩', callback_data = 'backand')

       keyboard.add(button1, button2)

       bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = '🎲Рандомная карта с рандомным балансом🎲', reply_markup = keyboard)

bot.polling()