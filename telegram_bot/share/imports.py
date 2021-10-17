import sys
import os
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
workpath=sys.path.append(os.getcwd())

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor
import share.IO_base as IO_base
import share.catalog_event as catalog_event
import share.default_conf as default_conf
import share.catalog_event_dispatcher as ev_disp
import re
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import share.send_to_another_bot

client_bot_token_file_path="client_token.txt"
service_bot_token_file_path="service_token.txt"
client_bot_token=None
service_bot_token=None
client_bot_name='test_client_bot_IC_bot'
service_bot_name='test_service_bot_IC_bot'
client_bot_id=1959268476
service_bot_id=2076740220

service_bot=None
client_bot = None
service_bot_dispatcher=None
keyboard_for_service_bot=None
event_disp=ev_disp.Catalog_event_dispatcher.get_dispatcher_instance()
##client##
reply_button_config_file='rply_btn_conf.json'
chat_reply_button_config_file='chat_rply_btn_conf.json'
inline_button_config_file='inln_btn_conf.json'
inline_button_config_file_owner='inln_ownr_btn_conf.json'
inline_button_confrm_config_file="confrm_btn.json"
inline_button_cancel_config_file="cancel_btn.json"

client_bot_dispatcher=None
reply_buttons_cnfg_list=None
inline_buttons_cnfg_list=None
chat_reply_buttons_cnfg_list=None
inline_buttons_cnfg_list_confirm=None
inline_buttons_cnfg_list_cancel=None
inline_buttons_cnfg_list_for_owner=None
inline_kybrd_callbacks=dict()
catalog_events_list=None
replay_kybrd=None
inline_kybrd=None
inline_kybrd_for_owner=None
inline_kybrd_confirm=None
inline_kybrd_cancel=None
chat_replay_kybrd=None
usr_msg=None
catalog_pos=None
confirm_kybrd=None
in_chat_with_owner=False
event_create_in_progress=False
event_create_progress_step=0
fsm_states_dist=dict()


event_pipline={
0:"Введите имя события",
1:"Введите отображаемый заголовок события",
2:"Введите описание события",
3:"Укажите ссылку на медиа",
4:"Введите дату конца показа"}

event_pipline_answ={
0:"",
1:"",
2:"",
3:"",
4:""}
########################

##service##
service_b_inline_button_config_file='serv_inln_btn_conf.json'
service_b_inline_buttons_cnfg_list=None
#######################################

def construct_keyboard(buttons:list,is_reply_kybrd:bool,needResizeKeyboard=True):
    if is_reply_kybrd:
        markup=ReplyKeyboardMarkup(needResizeKeyboard)
    else:
        markup=InlineKeyboardMarkup()
    for btn in buttons:
        if (type(btn) is KeyboardButton and type(markup) is ReplyKeyboardMarkup) or (type(btn) is InlineKeyboardButton and type(markup) is InlineKeyboardMarkup ):
            markup.add(btn)
    return markup

def getButtons(btn_cnfgs,is_repl_kybrd):
    buttons=list()
    global inline_kybrd_callbacks
    #inline_kybrd_callbacks.clear()
    if btn_cnfgs!=None:
        if is_repl_kybrd:
            for btn in btn_cnfgs:
                buttons.append(KeyboardButton(btn["text"]))
        else:
            for btn in btn_cnfgs:
                buttons.append(InlineKeyboardButton(text=btn["text"][0],callback_data=btn["text"][1]))
                inline_kybrd_callbacks[btn["text"][0]]=btn["text"][1]
    return buttons