from datetime import datetime

# In-memory storage
db = {}

def save_url(short_code, original_url):
    db[short_code] = {
        "url": original_url,
        "clicks": 0,
        "created_at": datetime.utcnow().isoformat()
    }

def get_url(short_code):
    return db.get(short_code)

def increment_click(short_code):
    if short_code in db:
        db[short_code]["clicks"] += 1
