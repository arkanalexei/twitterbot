import tweepy
import logging
from config import create_api
import time
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

kutipan_jokowi = open('jokoquotes.txt','r').readlines()
database = open('database.txt', 'r').readlines()

def check_mentions(api, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id

    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)

        if str(tweet.id) not in database:

            if 'quote' in tweet.text.lower():
                logger.info(f"Answering quote to {tweet.user.name}")

                api.update_status(
                    status=random.choice(kutipan_jokowi),
                    in_reply_to_status_id=tweet.id,
                    auto_populate_reply_metadata=True
                )

            if 'yntkts' in tweet.text.lower():
                logger.info(f"Answering yntkts to {tweet.user.name}")

                api.update_status(
                    status=random.randint(1,999999999),
                    attachment_url="https://twitter.com/i/status/1411029563564466181",
                    in_reply_to_status_id=tweet.id,
                    auto_populate_reply_metadata=True
                )

            with open('database.txt', 'a') as file:
                file.write(str(tweet.id) + ",")

    return new_since_id

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, since_id)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
