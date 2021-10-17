import sys
import os
from threading import Thread
workpath=sys.path.append(os.getcwd())
from share.imports  import *
import threading
import asyncio

inline_serv_b_kybrd=None
owner_id=None
in_chat_with_person=False
usr_msg=None
#сообщения от бота не прехватываются (пробывал так же другие методы-декораторы хххх_handler())
@service_bot_dispatcher.message_handler()
async def handle_usr_msg(msg:types.message):
    global inline_serv_b_kybrd
    global owner_id
    global in_chat_with_person
    global usr_msg
    usr_msg=msg
    if msg.text=='/start':
         owner_id=msg.from_user.id
    if  msg.from_user.id==owner_id: #msg.from_user.id==owner_id: - for test - должно быть #msg.from_user.id!=owner_id #если захендлили сообщение от бота
        await client_bot.send_message(msg.from_user.id,'Действия:',reply_markup=inline_serv_b_kybrd)
    elif in_chat_with_person:
        await share.send_to_another_bot.send_to_bot(ev_disp.choosen_event.evnet_title,msg.from_user.full_name,msg.text,client_bot,ev_disp.choosen_event.event_owner_id,inline_kybrd_for_owner) 

@service_bot_dispatcher.callback_query_handler()
async def inline_keyboard_callback(callback_q:types.CallbackQuery):
    global usr_msg
    global in_chat_with_person
    if usr_msg!=None:
        if callback_q.data==default_conf.serv_msg_repl_callback:
            in_chat_with_person=True
            await usr_msg.answer('Вы вошли в чат с  - '+usr_msg.from_user.full_name,reply_markup=chat_replay_kybrd)
        if callback_q.data==default_conf.serv_see_event_callback: #Посмотреть событие
            #todo - разобраться с deeplink
            #заглушка вместо deeplink
            event_text=event_disp.choosen_event.evnet_title
            await usr_msg.answer(text=event_text,reply_markup=inline_kybrd_cancel)

if __name__=='__main__':
    IO_base.read_conf_file(service_b_inline_button_config_file,default_conf.default_serv_inline_btn_conf)
    serv_b_reply_buttons_cnfg_list=IO_base.file_read_res
    inline_serv_b_kybrd=construct_keyboard(getButtons(serv_b_reply_buttons_cnfg_list,False),False)
    if service_bot_dispatcher!=None:
        executor.start_polling(service_bot_dispatcher)