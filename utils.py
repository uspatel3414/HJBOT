import time
import random
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def random_delay(min_seconds, max_seconds):
    delay = random.randint(min_seconds, max_seconds)
    logging.info(f"⏳ Waiting {delay} seconds...")
    time.sleep(delay)
def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1"
    ]
    return random.choice(user_agents)
