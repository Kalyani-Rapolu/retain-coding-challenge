from .database import save_url, get_url, increment_click
from .utils import generate_short_code, is_valid_url

BASE_URL = "http://localhost:5000"

def shorten_url(original_url):
    if not is_valid_url(original_url):
        return None, "Invalid URL"

    short_code = generate_short_code()
    save_url(short_code, original_url)
    return {"short_code": short_code, "short_url": f"{BASE_URL}/{short_code}"}, None

def get_redirect(short_code):
    data = get_url(short_code)
    if not data:
        return None
    increment_click(short_code)
    return data["url"]

def get_stats(short_code):
    data = get_url(short_code)
    if not data:
        return None
    return {
        "url": data["url"],
        "clicks": data["clicks"],
        "created_at": data["created_at"]
    }
