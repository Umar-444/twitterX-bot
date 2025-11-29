import tweepy
import os
import random
import time
import logging
import signal
import sys
from datetime import datetime, timedelta
from typing import List, Optional
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class TwitterBotConfig:
    """Configuration class for Twitter bot settings"""

    def __init__(self):
        # Twitter API credentials
        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")
        self.access_token = os.getenv("ACCESS_TOKEN")
        self.access_secret = os.getenv("ACCESS_SECRET")

        # Scheduling configuration
        self.posts_per_day = int(os.getenv("POSTS_PER_DAY", "3"))
        self.hours_between_posts = int(os.getenv("HOURS_BETWEEN_POSTS", "8"))
        self.start_hour = int(os.getenv("START_HOUR", "9"))  # 9 AM
        self.timezone_offset = int(os.getenv("TIMEZONE_OFFSET", "0"))  # UTC offset in hours

        # Retry configuration
        self.max_retries = int(os.getenv("MAX_RETRIES", "3"))
        self.retry_delay = int(os.getenv("RETRY_DELAY", "60"))  # seconds

class TwitterBot:
    """Twitter bot for automated posting"""

    def __init__(self, config: TwitterBotConfig):
        self.config = config
        self.api: Optional[tweepy.API] = None
        self.running = True
        self.tweets_posted_today = 0
        self.last_post_time: Optional[datetime] = None

        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

        # Tweet content - you can expand this list or load from file
        self.tweets: List[str] = [
            "Good morning! Testing my Twitter bot. ☀️",
            "Learning Python automation with Tweepy. 🐍",
            "Posting automatically using Railway and Twitter API! 🚂",
            "This is another automated post by my bot. 🤖",
            "Building my developer skills with daily posting. 💻",
            "Exploring the world of automated social media! 🌐",
            "Code, coffee, and continuous learning. ☕",
            "AI and automation making life easier! ⚡",
            "Another day, another automated tweet! 📝",
            "Staying productive with Python scripts! 🛠️"
        ]

    def _signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        logger.info(f"Received signal {signum}. Shutting down gracefully...")
        self.running = False

    def validate_credentials(self) -> bool:
        """Validate that all required credentials are present"""
        required = ['api_key', 'api_secret', 'access_token', 'access_secret']
        missing = [key for key in required if not getattr(self.config, key)]

        if missing:
            logger.error(f"Missing required environment variables: {', '.join(missing)}")
            return False

        return True

    def authenticate(self) -> bool:
        """Authenticate with Twitter API"""
        try:
            auth = tweepy.OAuth1UserHandler(
                self.config.api_key,
                self.config.api_secret,
                self.config.access_token,
                self.config.access_secret
            )
            self.api = tweepy.API(auth)

            # Test authentication
            user = self.api.verify_credentials()
            logger.info(f"Successfully authenticated as: @{user.screen_name}")
            return True

        except tweepy.TweepyException as e:
            logger.error(f"Authentication failed: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error during authentication: {e}")
            return False

    def get_next_post_time(self) -> datetime:
        """Calculate the next post time based on configuration"""
        now = datetime.now()

        # If no posts today, check if it's time to start (based on start_hour)
        if self.tweets_posted_today == 0:
            start_time = now.replace(hour=self.config.start_hour, minute=0, second=0, microsecond=0)
            if now < start_time:
                return start_time
            else:
                # Start immediately if we're past start time
                return now

        # If we have posts today, calculate next post time
        if self.last_post_time:
            next_post = self.last_post_time + timedelta(hours=self.config.hours_between_posts)
            return next_post

        return now

    def wait_until_next_post(self):
        """Wait until the next scheduled post time"""
        next_post_time = self.get_next_post_time()
        now = datetime.now()

        if next_post_time > now:
            wait_seconds = (next_post_time - now).total_seconds()
            logger.info(f"Next post scheduled for: {next_post_time}")
            logger.info(f"Waiting {wait_seconds:.0f} seconds...")

            # Wait in smaller chunks to allow for graceful shutdown
            while wait_seconds > 0 and self.running:
                sleep_time = min(60, wait_seconds)  # Sleep in 1-minute chunks
                time.sleep(sleep_time)
                wait_seconds -= sleep_time

    def post_tweet(self) -> bool:
        """Post a single tweet with retry logic"""
        for attempt in range(self.config.max_retries):
            try:
                tweet = random.choice(self.tweets)
                self.api.update_status(tweet)

                self.last_post_time = datetime.now()
                self.tweets_posted_today += 1

                logger.info(f"✅ Tweet posted ({self.tweets_posted_today}/{self.config.posts_per_day}): {tweet}")
                return True

            except tweepy.TweepyException as e:
                logger.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt < self.config.max_retries - 1:
                    logger.info(f"Retrying in {self.config.retry_delay} seconds...")
                    time.sleep(self.config.retry_delay)
                else:
                    logger.error(f"Failed to post tweet after {self.config.max_retries} attempts")
            except Exception as e:
                logger.error(f"Unexpected error posting tweet: {e}")
                break

        return False

    def reset_daily_counter(self):
        """Reset the daily post counter"""
        self.tweets_posted_today = 0
        logger.info("Daily counter reset. Starting new day!")

    def should_reset_counter(self) -> bool:
        """Check if we should reset the daily counter (new day)"""
        if not self.last_post_time:
            return False

        now = datetime.now()
        # Reset if it's a new day
        return now.date() > self.last_post_time.date()

    def run(self):
        """Main bot loop"""
        logger.info("🚀 Starting Twitter Bot...")
        logger.info(f"Configuration: {self.config.posts_per_day} posts/day, {self.config.hours_between_posts}h intervals")

        if not self.validate_credentials():
            logger.error("❌ Credential validation failed. Exiting.")
            return

        if not self.authenticate():
            logger.error("❌ Authentication failed. Exiting.")
            return

        logger.info("✅ Bot initialized successfully. Starting posting schedule...")

        while self.running:
            try:
                # Check if we need to reset daily counter
                if self.should_reset_counter():
                    self.reset_daily_counter()

                # If we've reached our daily limit, wait for next day
                if self.tweets_posted_today >= self.config.posts_per_day:
                    logger.info(f"Daily limit reached ({self.config.posts_per_day} posts). Waiting for next day...")
                    # Sleep for a longer period, but check periodically
                    sleep_time = 60 * 60  # 1 hour
                    time.sleep(sleep_time)
                    continue

                # Wait until next post time
                self.wait_until_next_post()

                # Post if we're still running
                if self.running:
                    self.post_tweet()

            except KeyboardInterrupt:
                logger.info("Keyboard interrupt received. Shutting down...")
                break
            except Exception as e:
                logger.error(f"Unexpected error in main loop: {e}")
                time.sleep(60)  # Wait before retrying

        logger.info("👋 Twitter Bot stopped.")

def main():
    """Main entry point"""
    config = TwitterBotConfig()
    bot = TwitterBot(config)
    bot.run()

if __name__ == "__main__":
    main()
