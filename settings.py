import os
import logging

# Slack API token for sending messages to specific users or channels
SLACK_TOKEN_CHAT = os.getenv("SLACK_TOKEN_CHAT")

# Slack API token for interacting with the Slack API
SLACK_TOKEN = os.getenv("SLACK_TOKEN")

# A list of country codes that are prohibited from using the service
FORBIDDEN_COUNTRIES = ["RU"]

# Message sent to the user if they are accessing the service from a prohibited country
WARNING_MESSAGE = "\nИ кстати, не забудь включить VPN! 😉\n"

# Number of seconds between each check for the VPN status
CHECKING_PERIOD = 60 * 15

# Number of seconds between each check for user logins
CHECKING_LOGIN_PERIOD = 60 * 5

# URL for the GeoIP API that is used to determine the user's country based on their IP address
GEOIP_API_URL = "http://ip-api.com/json/"

# Time zone used by the service
TIME_ZONE = "Europe/Moscow"

# Boolean indicating whether the service should ignore requests from mobile clients
IGNORE_MOBILE_CLIENTS = True

# Boolean indicating whether the service should only run during specific days and hours
CHECK_WORKING_DAYS_AND_HOURS = True

# List integers representing the start and end hours for the working day
WORKING_HOURS = [8, 20]

# List of integers representing the days of the week that are considered weekends
WEEKEND = [5, 6]

# Boolean indicating whether a joke should be added to the warning message
ADD_JOKE_TO_MESSAGE = True

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(message)s",
)
logger = logging.getLogger(__name__)
