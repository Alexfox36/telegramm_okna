import telebot
from config import TELEGRAM_BOT_TOKEN
from telebot import types

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
users ={}


@bot.message_handler(commands=['start'])
def menu(message: telebot.types.Message):
    chat_id = message.chat.id
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_glazing = telebot.types.KeyboardButton(text="Остекление окон", )
    button_balcony = telebot.types.KeyboardButton(text="Остекление балкона/лоджии")
    button_contacts = telebot.types.KeyboardButton(text="📞 Контакты")
    button_portfolio = telebot.types.KeyboardButton(text="🖼 Портфолио")
    keyboard1.add(button_glazing, button_balcony, button_contacts, button_portfolio)
    bot.send_message(chat_id,
                     '👋 Здравствуйте!Мы рады помочь вам с остеклением. Пожалуйста, выберите, что вас интересует:',
                     reply_markup=keyboard1)

@bot.message_handler(
    func=lambda message: message.text == 'Остекление окон')
def glazing(message):
    chat_id = message.chat.id
    keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_glazing_kvartira = telebot.types.KeyboardButton(text="Квартира")
    button_glazing_dom = telebot.types.KeyboardButton(text="Дом")
    button_glazing_office = telebot.types.KeyboardButton(text="Офис")
    button_glazing_other = telebot.types.KeyboardButton(text="Другое помещение")
    bot.register_next_step_handler(message, glazing_type)
    button_glazing_back = telebot.types.KeyboardButton(text="Назад")
    keyboard2.add(button_glazing_kvartira, button_glazing_dom, button_glazing_office, button_glazing_other, button_glazing_back )
    bot.send_message(chat_id, 'Куда хотите установить окна?', reply_markup=keyboard2)


@bot.message_handler(content_types=['Квартира'])
def glazing_type(message):
    chat_id = message.chat.id
    keyboard3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_glazing_kv_window = telebot.types.KeyboardButton(text="Квартирное окно")
    button_glazing_balcony_block = telebot.types.KeyboardButton(text="Балконный блок")
    button_glazing_enter_block = telebot.types.KeyboardButton(text="Входная группа")
    button_glazing_back = telebot.types.KeyboardButton(text="Назад")
    keyboard3.add(button_glazing_kv_window, button_glazing_balcony_block, button_glazing_enter_block, button_glazing_back)
    bot.send_message(chat_id, 'Какой тип изделия?', reply_markup=keyboard3)
    bot.register_next_step_handler(message, glazing_profile)

def glazing_profile(message):
    chat_id = message.chat.id
    keyboard4 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_glazing_rehau = telebot.types.KeyboardButton(text="Rehau")
    button_glazing_kbe = telebot.types.KeyboardButton(text="KBE")
    button_glazing_brusbox = telebot.types.KeyboardButton(text="Brusbox")
    button_glazing_consultation = telebot.types.KeyboardButton(text="Нужна консультация")
    button_glazing_profile_back = telebot.types.KeyboardButton(text="Назад")
    keyboard4.add(button_glazing_rehau, button_glazing_kbe, button_glazing_brusbox,button_glazing_consultation, button_glazing_profile_back)
    bot.send_message(chat_id, 'Выберите профиль', reply_markup=keyboard4)
    bot.register_next_step_handler(message, glazing_size)

def glazing_size(message):
    chat_id = message.chat.id
    keyboard5 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_glazing_size_yes = telebot.types.KeyboardButton(text="Да, могу")
    button_glazing_size_no = telebot.types.KeyboardButton(text="Нет, нужен замерщик")
    button_glazing_size_back = telebot.types.KeyboardButton(text="Назад")
    keyboard5.add(button_glazing_size_yes, button_glazing_size_no, button_glazing_size_back )
    bot.send_message(chat_id, ' Можете указать размеры изделий?', reply_markup=keyboard5)
    bot.register_next_step_handler(message, adress)



@bot.message_handler(
    func=lambda message: message.text == 'Остекление балкона/лоджии')
def balcony(message):
    chat_id = message.chat.id
    keyboard6 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_balcony_hot = telebot.types.KeyboardButton(text="Тёплое остекление")
    button_balcony_cold = telebot.types.KeyboardButton(text="Холодное остекление")
    button_balcony_slidors = telebot.types.KeyboardButton(text="Slidors")
    button_balcony_back = telebot.types.KeyboardButton(text="Назад")
    keyboard6.add(button_balcony_hot, button_balcony_cold, button_balcony_slidors,button_balcony_back )
    bot.send_message(chat_id, 'Выберите тип остекления:', reply_markup=keyboard6)
    bot.register_next_step_handler(message, balcony_form)


def balcony_form(message):
    chat_id = message.chat.id
    keyboard7 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_form_1 = telebot.types.KeyboardButton(text="Прямая лоджия")
    button_form_2 = telebot.types.KeyboardButton(text="Лодочка")
    button_form_3 = telebot.types.KeyboardButton(text="Сапожек")
    button_form_4 = telebot.types.KeyboardButton(text="П-образный")
    button_form_5 = telebot.types.KeyboardButton(text="Другое")
    button_form_back = telebot.types.KeyboardButton(text="Назад")
    keyboard7.add(button_form_1, button_form_2, button_form_3, button_form_4, button_form_5, button_form_back )
    bot.send_message(chat_id, 'Какая у вас форма балкона?', reply_markup=keyboard7)
    bot.register_next_step_handler(message, balcony_type)

def balcony_type(message):
    chat_id = message.chat.id
    keyboard8 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_type_1 = telebot.types.KeyboardButton(text="Да")
    button_type_2 = telebot.types.KeyboardButton(text="Нет")
    button_type_3 = telebot.types.KeyboardButton(text="Другое")
    button_type_back = telebot.types.KeyboardButton(text="Назад")
    keyboard8.add(button_type_1, button_type_2, button_type_3, button_type_back )
    bot.send_message(chat_id, 'Нужна ли обшивка?', reply_markup=keyboard8)
    bot.register_next_step_handler(message, balcony_insulation)


def balcony_insulation(message):
    chat_id = message.chat.id
    keyboard9 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_insulation_type_1 = telebot.types.KeyboardButton(text="Да")
    button_insulation_type_2 = telebot.types.KeyboardButton(text="Нет")
    button_insulation_type_3 = telebot.types.KeyboardButton(text="Другое")
    button_insulation_back = telebot.types.KeyboardButton(text="Назад")
    keyboard9.add(button_insulation_type_1, button_insulation_type_2, button_insulation_type_3, button_insulation_back)
    bot.send_message(chat_id, 'Утепление требуется?', reply_markup=keyboard9)
    bot.register_next_step_handler(message, balcony_size)

def balcony_size(message):
    chat_id = message.chat.id
    keyboard10 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_balcony_size_1 = telebot.types.KeyboardButton(text="Да, могу")
    button_balcony_size_2 = telebot.types.KeyboardButton(text="Нет, нужен замерщик")
    button_balcony_size_back = telebot.types.KeyboardButton(text="Назад")
    keyboard10.add(button_balcony_size_1, button_balcony_size_2, button_balcony_size_back)
    bot.send_message(chat_id, 'Указать размеры?', reply_markup=keyboard10)
    bot.register_next_step_handler(message, adress)


@bot.message_handler(
    func=lambda message: message.text == '📞 Контакты')
def contacts(message):
    chat_id = message.chat.id
    keyboard11 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_contacts_back = telebot.types.KeyboardButton(text="🔙 Главное меню")
    keyboard11.add(button_contacts_back )
    bot.send_message(chat_id, '📍 Наши контакты:'
                              'ул. Центральная, д. 10'
                              '📱 +7 (900) 000-00-00'
                              '✉ info@okna.ru'
                              '📲 WhatsApp: https://wa.me/79000000000'
                              '📲 Telegram: https://t.me/okna_manager', reply_markup=keyboard11)
    bot.register_next_step_handler(message, glazing_type)



@bot.message_handler(
    func=lambda message: message.text == '🖼 Портфолио')
def portfolio(message):
    chat_id = message.chat.id
    keyboard12 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_contacts_back = telebot.types.KeyboardButton(text="🔙 Главное меню")
    keyboard12.add(button_contacts_back )
    bot.send_message(chat_id, 'Отправка портфолио'
                              , reply_markup=keyboard12)
    bot.register_next_step_handler(message, glazing_type)



def adress(message):
    chat_id = message.chat.id
    keyboard13 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_contacts_back = telebot.types.KeyboardButton(text="🔙 Назад")
    keyboard13.add(button_contacts_back )
    bot.send_message(chat_id, 'Укажите ваш город/район'
                              , reply_markup=keyboard13)
    bot.register_next_step_handler(message, phone_number)


def phone_number(message):
    chat_id = message.chat.id
    keyboard14 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_contacts_back = telebot.types.KeyboardButton(text="🔙 Назад")
    keyboard14.add(button_contacts_back )
    bot.send_message(chat_id, 'Укажите ваш номер телефона'
                              , reply_markup=keyboard14)
    bot.register_next_step_handler(message, enter_username)


def enter_username(message):
    chat_id = message.chat.id
    keyboard15 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_contacts_back = telebot.types.KeyboardButton(text="🔙 Назад")
    keyboard15.add(button_contacts_back )
    bot.send_message(chat_id, 'Укажите ваше имя'
                              , reply_markup=keyboard15)
    bot.register_next_step_handler(message, glazing_type)




bot.polling()