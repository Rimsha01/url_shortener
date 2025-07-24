# TODO: Implement your data models here
# Consider what data structures you'll need for:
# - Storing URL mappings
# - Tracking click counts
# - Managing URL metadata
from datetime import datetime


class URLShortener:
    _id: int = 1


    def __init__(self, long_url):
        self.long_url = long_url
        self.id = self._id
        self.clicks = 0
        self.created_at = datetime.now()
        self._id +=1


    def to_dict(self):
        return {"id": self.id,
                "url": self.long_url,
                "created_at": self.created_at,
                "clicks": self.clicks
                }


stored_urls = {}
