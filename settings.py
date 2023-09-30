import os
import logging


def get_env_var(key: str) -> str:
    try:
        return os.environ[key]
    except KeyError:
        raise KeyError(f"Please set the {key} environment variable") from None


# Slack API token used for sending messages to specific users or channels
SLACK_TOKEN_CHAT = get_env_var("SLACK_TOKEN_CHAT")

# Slack API token used for interacting with the Slack API
SLACK_TOKEN = get_env_var("SLACK_TOKEN")

# Flag to enable debug mode, which determines whether to send alert messages to
# members of your Slack group during testing.
DEBUG = get_env_var("DEBUG")

# Number of recent logins to check. Increase this if you have many active users; consider 2-3x daily active users.
LOGINS_COUNT = 100

# A list of country codes that are disallowed from using the service
FORBIDDEN_COUNTRIES = ["RU"]

# Message sent to the user if they are accessing the service from a disallowed country
WARNING_MESSAGE = "\nИ кстати, не забудь включить VPN! 😉\n"

# Interval (in seconds) for checking the VPN status
CHECKING_PERIOD = 60 * 15

# Interval (in seconds) for checking user logins
CHECKING_LOGIN_PERIOD = 60 * 5

# URL of the GeoIP API to determine the user's country by IP address
GEOIP_API_URL = "http://ip-api.com/json/"

# Time zone used by the service
TIME_ZONE = "Europe/Moscow"

# Flag to ignore requests from mobile clients
SKIP_MOBILE_CLIENTS_CHECK = False

# List of integers representing the start and end hours for the working day
WORKING_HOURS = [8, 20]

# List of integers for days of the week considered as weekends, starting from 0 (Monday)
WEEKEND = [5, 6]

# Flag to add a joke to the warning message
ADD_JOKE_TO_MESSAGE = True

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(message)s",
)
logger = logging.getLogger(__name__)
