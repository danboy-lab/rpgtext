
import requests
import time
import json
from random import choice

# Simple cache with timestamps (cache for 1 hour)
_cache = {}
CACHE_DURATION = 3600  # 1 hour

# Load enemy phrases
try:
    with open("data/enemy_phrases.json", "r") as f:
        _phrases = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    _phrases = {"taunt": ["Die!"], "attack_reaction": ["Ouch!"], "defeat": ["..."]}

def _get_cached_or_fetch(url, cache_key):
    now = time.time()
    if cache_key in _cache:
        data, timestamp = _cache[cache_key]
        if now - timestamp < CACHE_DURATION:
            return data
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        _cache[cache_key] = (data, now)
        return data
    except (requests.RequestException, ValueError):
        # Return None on failure
        return None

def get_random_quote():
    """Get a random quote from quotable.io"""
    data = _get_cached_or_fetch("https://api.quotable.io/random", "quote")
    if data:
        return f'"{data["content"]}" - {data["author"]}'
    return '"The only way to do great work is to love what you do." - Steve Jobs'  # Fallback

def get_random_user():
    """Get a random user profile (no caching to ensure variety)"""
    try:
        response = requests.get("https://randomuser.me/api/", timeout=5)
        response.raise_for_status()
        data = response.json()
        if data and data.get("results"):
            user = data["results"][0]
            name = f"{user['name']['first']} {user['name']['last']}"
            return name
    except (requests.RequestException, ValueError):
        pass
    return "Adventurer"  # Fallback

def get_useless_fact():
    """Get a random useless fact"""
    data = _get_cached_or_fetch("https://uselessfacts.jsph.pl/random.json", "fact")
    if data:
        return data.get("text", "Did you know? The shortest war in history lasted only 38-45 minutes.")
    return "Did you know? The shortest war in history lasted only 38-45 minutes."  # Fallback

def get_cat_fact():
    """Get a random cat fact"""
    data = _get_cached_or_fetch("https://catfact.ninja/fact", "catfact")
    if data:
        return data.get("fact", "Cats have over 20 muscles that control their ears.")
    return "Cats have over 20 muscles that control their ears."  # Fallback

def get_random_enemy_name():
    """Get a random name for enemy"""
    return get_random_user()

def get_enemy_taunt():
    """Get a random taunt from local phrases"""
    return choice(_phrases.get("taunt", ["Die!"]))

def get_attack_reaction():
    """Get a random attack reaction from local phrases"""
    return choice(_phrases.get("attack_reaction", ["Ouch!"]))

def get_defeat_phrase():
    """Get a random defeat phrase from local phrases"""
    return choice(_phrases.get("defeat", ["..."]))

def get_random_event_fact():
    """Get a random fact for game events"""
    facts = [get_useless_fact, get_cat_fact]
    return choice(facts)()
