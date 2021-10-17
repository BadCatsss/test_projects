import share.catalog_event as catalog_event



class Catalog_event_dispatcher():
    __dispatcher=None
    __catalog_events_list__=None
    choosen_event=None

    def __init__(self) -> None:
        if Catalog_event_dispatcher.__dispatcher!=None:
            print('dispatcher instance already create')
        else:
            Catalog_event_dispatcher.__catalog_events_list__=list()
            Catalog_event_dispatcher.__dispatcher=self
    
    def get_dispatcher_instance():
        if  Catalog_event_dispatcher.__dispatcher==None:
            Catalog_event_dispatcher.__dispatcher=Catalog_event_dispatcher()
        return Catalog_event_dispatcher.__dispatcher
    
    

    def add_event_to_list(self,event):
        event.event_id=len(Catalog_event_dispatcher.__catalog_events_list__)
        Catalog_event_dispatcher.__catalog_events_list__.append(event)
    def remove_event(self,catalog_pos):
        Catalog_event_dispatcher.__catalog_events_list__.pop(catalog_pos-1)
    
    def get_events(self):
        return Catalog_event_dispatcher.__catalog_events_list__