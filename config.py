import logging
import tweepy

logger = logging.getLogger()

def create_api():
    consumer_key ="swDtItWNk1lq9DSfbpAkcVWRI"
    consumer_secret = "4aH9CDERx7NPUgK1wxPJCvLiuHHbm6CrulsqyqIjW8fCro9WlW"
    access_token = "1411002769327091712-pyTLV3BS1DIgRL9e8KiQInNRoG13Dd"
    access_token_secret = "IzsqXWtzQUGH4zA9gznketNXIBnZMGRSJfCWl79dF8fgT"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api