class Catalog_event():
    def __init__(self,media_path,event_name,evnet_title,event_desc,event_owner_id,expiration_date):
        self.media_path=media_path
        self.evnet_title=evnet_title
        self.event_name=event_name
        self.event_desc=event_desc
        self.event_owner_id=event_owner_id
        self.expiration_date=expiration_date
        self.event_id=0