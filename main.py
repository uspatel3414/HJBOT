
import logging
import time
from instagram_client import InstagramClient
from message_handler import reply_to_unread_messages
from story_handler import like_followed_stories
from utils import setup_logging

def main():
    setup_logging()
    while True:
        instagram_client = InstagramClient()
        try:
            instagram_client.login()
            reply_to_unread_messages(instagram_client)
            retry = like_followed_stories(instagram_client)
            if not retry:
                logging.info("⏳ Waiting 9 minutes before next run...")
                time.sleep(540)  # 9 minutes = 540 seconds
        except Exception as e:
            logging.error(f"❌ An error occurred: {e}")
            time.sleep(300)  # Wait 5 minutes on error

if __name__ == "__main__":
    main()
