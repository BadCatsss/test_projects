async def send_to_bot(event_title,from_full_name,msg,bot,owner_id,keybrd=None):
    text="\#Сообщение:"+event_title+"\n"+from_full_name+":"+msg
    await bot.send_message(owner_id,text)
    