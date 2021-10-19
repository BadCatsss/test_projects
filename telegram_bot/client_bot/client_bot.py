import sys
import os
workpath=sys.path.append(os.getcwd())
from share.catalog_event import Catalog_event
#ОСНОВНЫЕ ПЕРЕМЕННЫЕ В ЭТОМ МОДУЛЕ
from share.imports  import *
#import FSM_register
#import FSM_handlers
#for_test
my_id=None
#
def init_settings(rply_keyboard_conf,chat_reply_button_config_file,inln_keyboard_conf):
    global client_bot
    global service_bot
    global client_bot_dispatcher
    global service_bot_dispatcher
    global reply_buttons_cnfg_list
    global inline_buttons_cnfg_list
    global catalog_events_list
    global replay_kybrd
    global inline_kybrd
    global inline_kybrd_for_owner
    global catalog_pos
    global inline_kybrd_confirm
    global fsm_states_dist
    global chat_reply_buttons_cnfg_list
    global chat_replay_kybrd
    global inline_kybrd_cancel
    global inline_buttons_cnfg_list_cancel
    global client_bot_token
    global service_bot_token
    global client_bot_id
    global service_bot_id
    catalog_pos=0
    
   #Создание основных клавиатур - читаем кофниги
    IO_base.read_conf_file(rply_keyboard_conf,default_conf.default_reply_btn_conf)
    reply_buttons_cnfg_list=IO_base.file_read_res
    IO_base.read_conf_file(chat_reply_button_config_file,default_conf.default_chat_btn_conf)
    chat_reply_buttons_cnfg_list=IO_base.file_read_res
    IO_base.read_conf_file(inln_keyboard_conf,default_conf.default_inline_btn_conf)
    inline_buttons_cnfg_list=IO_base.file_read_res
    IO_base.read_conf_file(inline_button_config_file_owner,default_conf.default_inline_btn_conf_for_owner)
    inline_buttons_cnfg_list_for_owner=IO_base.file_read_res
    IO_base.read_conf_file(inline_button_confrm_config_file,default_conf.default_inline_confirm_btn)
    inline_buttons_cnfg_list_confirm=IO_base.file_read_res
    IO_base.read_conf_file(inline_button_cancel_config_file,default_conf.default_inline_btn_cancel_op)
    inline_buttons_cnfg_list_cancel=IO_base.file_read_res
   
    
    #for_test
    #my_id=IO_base.read_tken_file("test_id.txt")
    # #for test
    # event_disp.add_event_to_list(catalog_event.Catalog_event('https://telegram.org/img/t_logo.png','test_title','test_title','test_desc','1111','12.12.21'))
    # event_disp.add_event_to_list(catalog_event.Catalog_event('https://telegram.org/img/t_logo.png','test_title','test_title','test_desc',my_id,'12.12.21'))
    #event_disp.add_event_to_list(catalog_event.Catalog_event('h//telegram.org/img/t_logo.d','test_title','test_title','test_desc',my_id,'12.12.21'))
    # #

    #Диспетчер событий каталога
    catalog_events_list=event_disp.get_events()
     #Создание основных клавиатур - создаем основные клавиатуры
    replay_kybrd=construct_keyboard(getButtons(reply_buttons_cnfg_list,True),True)
    chat_replay_kybrd=construct_keyboard(getButtons(chat_reply_buttons_cnfg_list,True),True)
    inline_kybrd=construct_keyboard(getButtons(inline_buttons_cnfg_list,False),False)
    inline_kybrd_for_owner=construct_keyboard(getButtons(inline_buttons_cnfg_list_for_owner,False),False)
    inline_kybrd_confirm=construct_keyboard(getButtons(inline_buttons_cnfg_list_confirm,False),False)
    inline_kybrd_cancel=construct_keyboard(getButtons(inline_buttons_cnfg_list_cancel,False),False)
    #Тоже преполагало FSM (см FSM_handlers.pu и FSM_register.py и комментарий ниже)
    # fsm_states_dist={
    # FSM_handlers.FSM_states.leave_chat_state: FSM_handlers.leave_chat_handler,
    # FSM_handlers.FSM_states.start_chat_state:FSM_handlers.see_event_handler,
    # FSM_handlers.FSM_states.wait_chat_msg_state:FSM_handlers.wait_chat_msg_handler,
    # FSM_handlers.FSM_states.start_chat_state:FSM_handlers.start_chat_handler}

    #Настрйока ботов
    client_bot_token=IO_base.read_tken_file(client_bot_token_file_path)
    client_bot_id=client_bot_token[:client_bot_token.find(":")]
    client_bot = Bot(client_bot_token)
    client_bot_dispatcher=Dispatcher(client_bot,storage=MemoryStorage())

init_settings(rply_keyboard_conf=reply_button_config_file,chat_reply_button_config_file=chat_reply_button_config_file,
inln_keyboard_conf=inline_button_config_file)

async  def send_catalog(catalog,msg):
    global inline_kybrd
    global inline_kybrd_for_owner
    global catalog_pos
    for e in catalog:
        catalog_pos=catalog_pos+1
        snd_msg=e.evnet_title+'\n'+e.event_desc
        is_correct_media_type=False
        for t in media_types:
            if e.media_path.endswith(t):
                is_correct_media_type=True
                break
        if not ((e.media_path.startswith("https://") or e.media_path.startswith("http://")) and is_correct_media_type):
            e.media_path=default_event_img
        await client_bot.send_photo(msg.from_user.id,photo=e.media_path,caption=snd_msg)
        if e.event_owner_id==msg.from_user.id:
                    await msg.answer(text='Действия для события - '+str(catalog_pos-1)+':', reply_markup=inline_kybrd)
        else:
                    await msg.answer(text='Действия для события - '+str(catalog_pos-1)+':', reply_markup=inline_kybrd_for_owner)    

@client_bot_dispatcher.message_handler()
async def handle_usr_msg(msg:types.Message):
    global usr_msg
    global catalog_pos
    global in_chat_with_owner
    global event_create_in_progress
    global event_create_progress_step
    usr_msg=msg
    if msg.text=='/start':
        await client_bot.send_message(msg.from_user.id,'Добро пожаловать,'+msg.from_user.full_name,reply_markup=replay_kybrd)
    if msg.text==default_conf.catalog_text:
        event_create_progress_step=0
        event_create_in_progress=False
        catalog_pos=0
        if len(catalog_events_list)==0:
            await client_bot.send_message(msg.from_user.id,'Каталог пуст',reply_markup=replay_kybrd)
        if len(catalog_events_list)>0 and len(catalog_events_list)<=2:
            await  send_catalog(catalog_events_list,msg)
        else:
             await  send_catalog(catalog_events_list[:2],msg)
             delta_len=len(catalog_events_list)-2
             if delta_len>0:
                pagination_kybrd=InlineKeyboardMarkup()
                for i in range(delta_len):
                    pagination_kybrd.add(InlineKeyboardButton(text="+"+str(i+1),callback_data=default_conf.pagination_callback+str(i+1)))
                await msg.answer(text='Показать больше:', reply_markup=pagination_kybrd)
    if msg.text==default_conf.leave_chat_text:
        in_chat_with_owner=False
        await msg.answer(text='Выбирете другое событие', reply_markup=replay_kybrd)
    if msg.text==default_conf.show_event_text and ev_disp.Catalog_event_dispatcher.choosen_event!=None:
        event_d='\nНазвание:\n'+ev_disp.Catalog_event_dispatcher.choosen_event.evnet_title+'\n'+'Описание:\n'+ev_disp.Catalog_event_dispatcher.choosen_event.event_desc
        await msg.answer(text='Вы просматриваете событые'+event_d, reply_markup=chat_replay_kybrd)
    elif in_chat_with_owner:    
       await share.send_to_another_bot.send_to_bot(ev_disp.Catalog_event_dispatcher.choosen_event.evnet_title,msg.from_user.full_name,msg.text,service_bot,ev_disp.Catalog_event_dispatcher.choosen_event.event_owner_id,inline_kybrd_for_owner)
       # сам себе FSM ) 
    elif msg.text==default_conf.add_event_text or event_create_in_progress:
        if msg.text==default_conf.add_event_text:
            event_create_progress_step=0
            event_create_in_progress=True
            ev_pipline_text=""
            for e in event_pipline:
                ev_pipline_text+=str(e+1)+"."+event_pipline[e]+"\n"
            ev_pipline_text+="Что бы вернуться на один из предыдущих шагов - напишите номер шага (0,1,2..) - меньше текущего номера"
            await msg.answer(text=ev_pipline_text,reply_markup=inline_kybrd_cancel)
            await msg.answer(text=str(event_create_progress_step)+"."+event_pipline[event_create_progress_step])
        elif event_create_in_progress:
            if len(msg.text)==1 and str.isdigit(msg.text) and  int(msg.text) in event_pipline.keys(): #Вкрнуться к одному из предыдущих шагов
                if int(msg.text)<event_create_progress_step:
                    event_create_progress_step=int(msg.text)
                    await msg.answer(text="Вы вернулись к шагу - "+msg.text)
                else:
                    await msg.answer(text="Вы можете вернуться только к пройденым шагам. Введите число меньше текущего шага.")
            elif len(msg.text)>2: # продолжить создавать событие
                event_create_progress_step=event_create_progress_step+1
                if event_create_progress_step<len(event_pipline):
                    event_pipline_answ[event_create_progress_step]=msg.text
                    await msg.answer(text=str(event_create_progress_step)+"."+event_pipline[event_create_progress_step])                          
                else:
                    created_event=Catalog_event(event_pipline_answ[3],event_pipline_answ[0],event_pipline_answ[1],event_pipline_answ[2],msg.from_user.id,event_pipline_answ[4])
                    accepted_text=''
                    event_disp.add_event_to_list(created_event)
                    event_create_progress_step=0
                    event_create_in_progress=False
                    accepted_text+="Имя слбытия:\n"+created_event.evnet_title+'\nОписание события:\n'+created_event.event_desc+"\n"
                    accepted_text+="Вы создали событие👆👆👆\nДля того, чтобы получать уведомления о сообщениях перейдите в  @"+service_bot_name+" и напишите /start\n"
                    await msg.answer(text=accepted_text)                
            else:
                await msg.answer(text="Длина сообщения должна быть больше 2х символов")
            
@client_bot_dispatcher.callback_query_handler()
async def inline_keyboard_callback(callback_q:types.CallbackQuery):
    global usr_msg
    global catalog_pos
    global event_disp
    global fsm_states_dist
    global in_chat_with_owner
    global event_create_progress_step
    global event_create_in_progress
    if usr_msg!=None:
        if callback_q.data==inline_kybrd_callbacks[default_conf.connect_text]:
            #https://qna.habr.com/q/1061628 и 
            # https://ru.stackoverflow.com/questions/1339067/aiogram-fsm-%D0%BD%D0%B5-%D0%BC%D0%B5%D0%BD%D1%8F%D0%B5%D1%82-%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B5
            #  - спрашивал на форумах - т.к не мог понять почему FSM - не работает
            # state = bot_dispatcher.current_state(user=usr_msg.from_user.id)
            # await FSM_register.start_fsm(bot_dispatcher,fsm_states_dist,state=state)
            # await FSM_handlers.FSM_states.start_chat_state.set()
            #В директориях лежат вспомагательные классы FSM_handlers.pu и FSM_register.py  - которые планировал использовать
            #Поэтому дальше идут костыли и самописные FSM -  без "реальной" FSM 
            # (увы, хоть и понимаю, что это не по ТЗ и хочется поубивать таких людей, которые делают все не по ТЗ - ведь там русским по белому написанно,
            #  НО я честно потратил день, а время как бы идет и сдавать надо)
            await client_bot.answer_callback_query(callback_q.id,"") 
            ev_disp.Catalog_event_dispatcher.choosen_event=event_disp.get_events()[catalog_pos-1]
            await usr_msg.answer('Вы вошли в чат с владельцем события - '+ev_disp.Catalog_event_dispatcher.choosen_event.evnet_title,reply_markup=chat_replay_kybrd)
            #Предатсавим (хотя бы на минуту), что это наша Машина Состояний (сам не знал что они так выглядят) )
            in_chat_with_owner=True
            
        if callback_q.data==inline_kybrd_callbacks[default_conf.del_text] or callback_q.data==inline_kybrd_callbacks[default_conf.accept_text]  or  callback_q.data==inline_kybrd_callbacks[default_conf.reject_text]:
            if callback_q.data==inline_kybrd_callbacks[default_conf.del_text]:
                await client_bot.answer_callback_query(callback_q.id,"")
                await usr_msg.answer("Вы уверены, что хотите удалить событие? Подтвердите действие",reply_markup=inline_kybrd_confirm)
            if callback_q.data==inline_kybrd_callbacks[default_conf.accept_text]:
                event_disp.remove_event(catalog_pos)
                await client_bot.answer_callback_query(callback_q.id,"")
                await usr_msg.answer("Событие было удалено")
                return
            if callback_q.data==inline_kybrd_callbacks[default_conf.reject_text]:
                await client_bot.answer_callback_query(callback_q.id,"")
                await usr_msg.answer("Ок, ничего не удалено")
                return 
        if re.match(default_conf.pagination_callback+"[0-9]",callback_q.data):
            pagination_number=int(callback_q.data[-1])
            return  await  send_catalog(catalog_events_list[catalog_pos::pagination_number],usr_msg)  
        if callback_q.data==inline_kybrd_callbacks[default_conf.cancel_operation_text]: #cancel create event
            event_create_progress_step=0
            event_create_in_progress=False
            await usr_msg.answer("Ок, событие не создано")


if __name__=='__main__':
    if client_bot_dispatcher!=None and reply_buttons_cnfg_list!=None and client_bot_token!=None and client_bot_token!=None:
        executor.start_polling(client_bot_dispatcher)


