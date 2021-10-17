from os import stat
from FSM_handlers import *
from aiogram.dispatcher.dispatcher import Dispatcher

async def start_fsm(dsip:Dispatcher,states:dict,state):
    for s in states:
        dsip.register_message_handler(states[s],state=s)
    