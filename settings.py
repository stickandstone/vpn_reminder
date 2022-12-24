import os
import logging


SLACK_TOKEN_CHAT = os.getenv("SLACK_TOKEN_CHAT")
SLACK_TOKEN = os.getenv("SLACK_TOKEN")
FORBIDDEN_COUNTRIES = ["RU"]
WARNING_MESSAGE = "\nИ кстати, не забудь включить VPN! 😉\n"
CHECKING_PERIOD = 60 * 15
CHECKING_LOGIN_PERIOD = 60 * 5
GEOIP_API_URL = "http://ip-api.com/json/"
TIME_ZONE = "Europe/Moscow"
IGNORE_MOBILE_CLIENTS = True
CHECK_WORKING_DAYS_AND_HOURS = True
WORKING_HOURS = [8, 20]
WEEKEND = [5, 6]
ADD_JOKE_TO_MESSAGE = True

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(message)s",
)
logger = logging.getLogger(__name__)
