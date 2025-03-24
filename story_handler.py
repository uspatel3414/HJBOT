import logging
from utils import random_delay

def like_followed_stories(instagram_client):
    """
    For each account you follow, fetch their active stories
    and like each story with a 30-second delay between each action.
    If no stories are found, handles messages instead.
    """
    from message_handler import reply_to_unread_messages

    following_ids = instagram_client.get_following_list()
    if not following_ids:
        logging.info("⚠️ No accounts found in your following list.")
        reply_to_unread_messages(instagram_client)
        return

    stories_found = False

    for user_id in following_ids:
        stories = instagram_client.get_user_stories(user_id)
        if stories:
            stories_found = True
            for story in stories:
                instagram_client.like_story(story.id)
                logging.info("⏳ Waiting 30 seconds before liking the next story...")
                random_delay(30, 30)  # Fixed 30-second delay
    
    if not stories_found:
        logging.info("⚠️ No stories found, switching to message handling...")
        reply_to_unread_messages(instagram_client)
        logging.info("⏳ No stories found, waiting 5 minutes before next run...")
        time.sleep(300)  # 5 minutes = 300 seconds
        return True  # Signal main loop to restart immediately
