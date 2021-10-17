from aiogram.dispatcher.filters.state import State, StatesGroup
import aiogram.types as types
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from share.catalog_event_dispatcher import *
from aiogram.dispatcher import FSMContext

class FSM_states(StatesGroup):
    start_chat_state=State()
    leave_chat_state=State()
    see_event_state=State()
    wait_chat_msg_state=State()
    resend_to_owner_state=State()

async def start_chat_handler(message: types.Message,state: FSMContext):
    #event_title=Catalog_event_dispatcher.choosen_event.evnet_title
    await message.answer(message.from_user.id,'Вы вошди в чат с владельцем события - ',reply_markup=ReplyKeyboardMarkup)

async def leave_chat_handler(message: types.Message, state: FSMContext):
    pass
async def see_event_handler(message: types.Message, state: FSMContext):
    pass

async def wait_chat_msg_handler(message: types.Message, state: FSMContext):
    pass

async def resend_to_owner_handler(message: types.Message, state: FSMContext):
    pass