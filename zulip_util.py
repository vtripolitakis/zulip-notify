import zulip

class ZulipUtil:
    def __init__(self, site, user, key):
        self.site = site 
        self.user = user
        self.key = key
        
    def send_message_to_zulip(self, stream, subject, message_content):
        client = zulip.Client(email=self.user, api_key=self.key, site=self.site)
        message = {
            "type": "stream",
            "to": stream,
            "subject": subject,
            "content": message_content
        }
        client.send_message(message)

    
