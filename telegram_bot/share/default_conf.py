##client##
catalog_text='Каталог'
connect_text="Связаться"
add_event_text="Добавить событие"
accept_text="Да"
reject_text="Нет"
del_text="Удалить"
leave_chat_text="выйти из чата"
show_event_text="Показать событие"
cancel_operation_text="Отменить операцию"
#calbacks
del_calback="del_catalog_event"
pagination_callback="pagination_btn"
contact_callback="contact_btn"
confirm_calback="confrm_act"
reject_calback="reject_act"
cancel_operation_callback="cancel_act"
##########################

##service##
serv_msg_repl_text="Ответить"
serv_see_event_text="Посмотреть событие"

#calbacks
serv_msg_repl_callback="serv_repl_msg"
serv_see_event_callback="serv_see_ev"

#########################

default_reply_btn_conf='[{"text":"'+catalog_text+'"},{"text":"'+add_event_text+'"}]'
default_inline_btn_conf='[{"text":["'+connect_text+'","'+contact_callback+'"]}]'
default_inline_btn_conf_for_owner='[{"text":["'+connect_text+'","'+contact_callback+'"]},{"text":["'+del_text+'","'+del_calback+'"]}]'
default_inline_confirm_btn='[{"text":["'+accept_text+'","'+confirm_calback+'"]},{"text":["'+reject_text+'","'+reject_calback+'"]}]'
default_chat_btn_conf='[{"text":"'+leave_chat_text+'"},{"text":"'+show_event_text+'"}]'
default_inline_btn_cancel_op='[{"text":["'+cancel_operation_text+'","'+cancel_operation_callback+'"]}]'
##
default_serv_inline_btn_conf='[{"text":["'+serv_msg_repl_text+'","'+serv_msg_repl_callback+'"]},{"text":["'+serv_see_event_text+'","'+serv_see_event_callback+'"]}]'
