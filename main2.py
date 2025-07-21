from typing import TypedDict, NotRequired, Callable, Dict
import telebot
from telebot import types
from config import TELEGRAM_BOT_TOKEN
# from oauth2client.service_account import ServiceAccountCredentials

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

BACK = "🔙 Назад"
MAIN_MENU = "main_menu"
# TO_CHAT_ID = ... добавляем id нужного чата, куда будем пересылать итоговое сообщение


# Данные для доступа к Google Таблице
# SERVICE_ACCOUNT_FILE = 'path/to/your/credentials.json'
# SCOPE = ['https://spreadsheets.google.com/feeds',
#          'https://www.googleapis.com/auth/drive']
# SPREADSHEET_ID = 'id гугл таблицы'


# Функция для авторизации в Google Таблицах
# def get_sheet():
#     creds = ServiceAccountCredentials.from_json_keyfile_name(
#         SERVICE_ACCOUNT_FILE, SCOPE)
#     client = gspread.authorize(creds)
#     sheet = client.open_by_key(SPREADSHEET_ID).sheet1
#     return sheet


# Итоговое сообщение пользователю о заказе
def send_summary(user_id: int):
    session = get_session(user_id)
    data = session.data
    if not data:
        bot.send_message(user_id, "Пока нет собранных данных.")
        return
    text = "📋 Ваша заявка:\n"
    for key, value in data.items():
        text += f"•  {value}\n"
    bot.send_message(user_id, text)
    # Отправляем данные в группу
    #bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)

    # Сохранение данных в Google Таблицу
    # sheet = get_sheet()
    # sheet.append_row([name, telegram_id])
    session.reset()

# Состояние бота. текс, переходы, кнопки и хэндлер
class State(TypedDict):
    text: str
    transitions: NotRequired[Dict[str, str]]
    next: NotRequired[str]
    buttons: NotRequired[list[str]]
    handler: NotRequired[Callable[[int], None]]
    input: NotRequired[bool]


EMPTY_STATE: State = {"text": "Ошибка состояния", "next": MAIN_MENU}


# Определение словаря состояний
fsm: Dict[str, State] = {
    "main_menu": {
        "text": "👋 Здравствуйте! Мы рады помочь вам с остеклением. Что вас интересует?",
        "buttons": [
            "Остекление окон",
            "Остекление балкона/лоджии",
            "📞 Контакты",
            "🖼 Портфолио",
        ],
        "transitions": {
            "Остекление окон": "glazing_place",
            "Остекление балкона/лоджии": "balcony_type",
            "📞 Контакты": "contacts",
            "🖼 Портфолио": "portfolio",
        },
    },
    "glazing_place": {
        "text": "Куда хотите установить окна?",
        "buttons": ["Квартира", "Дом", "Офис", "Другое помещение"],
        "transitions": {
            "Квартира": "glazing_item",
            "Дом": "glazing_item",
            "Офис": "glazing_item",
            "Другое помещение": "glazing_item",
        },
    },
    "glazing_item": {
        "text": "Какой тип изделия?",
        "buttons": ["Квартирное окно", "Балконный блок", "Входная группа"],
        "transitions": {
            "Квартирное окно": "glazing_profile",
            "Балконный блок": "glazing_profile",
            "Входная группа": "glazing_profile",
        },
    },
    "glazing_profile": {
        "text": "Выберите профиль:",
        "buttons": ["Rehau", "KBE", "Brusbox", "Нужна консультация"],
        "transitions": {
            "Rehau": "glazing_size",
            "KBE": "glazing_size",
            "Brusbox": "glazing_size",
            "Нужна консультация": "glazing_size",
        },
    },
    "glazing_size": {
        "text": "Можете указать размеры изделий?",
        "buttons": ["Да, могу", "Нет, нужен замерщик"],
        "transitions": {"Да, могу": "adress", "Нет, нужен замерщик": "adress"},
    },
    "balcony_type": {
        "text": "Выберите тип остекления:",
        "buttons": ["Тёплое остекление", "Холодное остекление", "Slidors"],
        "transitions": {
            "Тёплое остекление": "balcony_form",
            "Холодное остекление": "balcony_form",
            "Slidors": "balcony_form",
        },
    },
    "balcony_form": {
        "text": "Какая у вас форма балкона?",
        "buttons": ["Прямая лоджия", "Лодочка", "Сапожек", "П-образный", "Другое"],
        "transitions": {
            "Прямая лоджия": "balcony_sheathing",
            "Лодочка": "balcony_sheathing",
            "Сапожек": "balcony_sheathing",
            "П-образный": "balcony_sheathing",
            "Другое": "balcony_sheathing",
        },
    },
    "balcony_sheathing": {
        "text": "Нужна ли обшивка?",
        "buttons": ["Да", "Нет", "Другое"],
        "transitions": {
            "Да": "balcony_insulation",
            "Нет": "balcony_insulation",
            "Другое": "balcony_insulation",
        },
    },
    "balcony_insulation": {
        "text": "Утепление требуется?",
        "buttons": ["Да", "Нет", "Другое"],
        "transitions": {
            "Да": "balcony_size",
            "Нет": "balcony_size",
            "Другое": "balcony_size",
        },
    },
    "balcony_size": {
        "text": "Указать размеры?",
        "buttons": ["Да, могу", "Нет, нужен замерщик"],
        "transitions": {
            "Да, могу": "adress",
            "Нет, нужен замерщик": "adress",
        },
    },
    "contacts": {
        "text": (
            "📍 Наши контакты:\n"
            "ул. Центральная, д. 10\n"
            "📱 +7 (900) 000-00-00\n"
            "✉ info@okna.ru\n"
            "📲 [WhatsApp](https://wa.me/79000000000)\n"
            "📲 [Telegram](https://t.me/okna_manager)"
        ),
    },
    "portfolio": {
        "text": "🖼 Портфолио: [пример](https://github.com/Alexfox36/telegramm_okna.git)",
    },
    "adress": {
        "text": "Укажите ваш город/район:",
        "next": "phone",
        "input": True,
    },
    "phone": {
        "text": "Укажите ваш номер телефона:",
        "next": "name",
        "input": True,
    },
    "name": {
        "text": "Укажите ваше имя:",
        "next": "summary",
        "input": True,
    },
    "summary": {
        "text": "Спасибо за информацию! Вот ваша заявка:",
        "handler": send_summary,
    },
}


# Добавляем создание и сохранение данных о сессии, а так же о шагах вперед и назад
class UserSession:
    def __init__(self):
        self.state_stack = [MAIN_MENU]
        self.data = {}

    def push_state(self, state: str):
        self.state_stack.append(state)

    def pop_state(self):
        if len(self.state_stack) > 1:
            removed_state = self.state_stack.pop()
            if removed_state in self.data:
                del self.data[removed_state]

    def current_state(self) -> str:
        return self.state_stack[-1]

    def reset(self):
        self.state_stack = [MAIN_MENU]
        self.data = {}


sessions: Dict[int, UserSession] = {}


# Получние сессии
def get_session(user_id: int) -> UserSession:
    return sessions.setdefault(user_id, UserSession())

# Отправка состояния пользователю
def send_state(user_id: int):
    session = get_session(user_id)
    state_name = session.current_state()
    state = fsm.get(state_name, EMPTY_STATE)

    buttons = state.get("buttons", [])
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for btn in buttons:
        markup.add(types.KeyboardButton(btn))
    if state_name != MAIN_MENU:
        markup.add(types.KeyboardButton(BACK))

    bot.send_message(
        user_id, state.get("text", "..."), reply_markup=markup, parse_mode="Markdown"
    )

    handler = state.get("handler")
    if callable(handler):
        handler(user_id)


def is_text_input(message):
    session = get_session(message.chat.id)
    state = fsm.get(session.current_state(), EMPTY_STATE)
    return state.get("input") is True


def is_menu_choice(message):
    text = message.text
    if not text:
        return False
    if text.startswith("/"):
        return False
    if is_text_input(message):
        return False
    if text == BACK:
        return False
    return True

# Обработчики состояний. Старт, назад, выбор следующего состояния, выбор предидущего состояния,текстовый ввод
@bot.message_handler(commands=["start"])
def handle_start(message):
    session = get_session(message.from_user.id)
    session.reset()
    send_state(message.from_user.id)


@bot.message_handler(func=lambda message: message.text == BACK)
def handle_back(message):
    session = get_session(message.chat.id)
    session.pop_state()
    send_state(message.chat.id)


@bot.message_handler(func=is_menu_choice)
def handle_menu_choice(message):
    session = get_session(message.chat.id)
    text = message.text.strip()
    state_name = session.current_state()
    state = fsm.get(state_name, EMPTY_STATE)

    next_state = state.get("transitions", {}).get(text)
    if next_state:
        session.data[state_name] = text
        session.push_state(next_state)
        send_state(message.chat.id)
    else:
        bot.send_message(
            message.chat.id, "Не понял. Пожалуйста, выберите один из вариантов."
        )


@bot.message_handler(func=is_text_input)
def handle_text_states(message):
    session = get_session(message.chat.id)
    state_name = session.current_state()
    state = fsm.get(state_name, EMPTY_STATE)
    session.data[state_name] = message.text.strip()
    next_state = state.get("next", MAIN_MENU)
    session.push_state(next_state)
    send_state(message.chat.id)


if __name__ == "__main__":
    bot.polling(none_stop=True)
