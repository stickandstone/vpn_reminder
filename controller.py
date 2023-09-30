import time
import datetime
import pytz

from settings import (
    WORKING_HOURS,
    WEEKEND,
    TIME_ZONE,
    logger, CHECKING_PERIOD,
)
from slack_client import SlackClient
from user import User


class Controller:
    def __init__(self):
        self.slack = SlackClient()
        self.users_to_remind = []
        self.tz = pytz.timezone(TIME_ZONE)

    @property
    def is_within_working_hours(self) -> bool:
        today = datetime.datetime.now(tz=self.tz)
        working_hours = WORKING_HOURS[0] <= today.hour < WORKING_HOURS[1]
        return today.weekday() not in WEEKEND and working_hours

    def wait_until_next_working_hour(self) -> None:
        now = datetime.datetime.now(tz=pytz.timezone(TIME_ZONE))
        next_day = now + datetime.timedelta(days=1)
        next_start_time = datetime.datetime(
            year=next_day.year,
            month=next_day.month,
            day=next_day.day,
            hour=WORKING_HOURS[0],
            tzinfo=pytz.timezone(TIME_ZONE),
        )
        sleep_seconds = (next_start_time - now).total_secxqonds()
        time.sleep(sleep_seconds)

    def identify_users_to_remind(self) -> list:
        users_to_remind = []
        logins = self.slack.get_logins()
        for login in logins:
            user = User(login, users_to_remind)
            if user.needs_reminder:
                users_to_remind.append(user.id)
                logger.info(user)
        return users_to_remind

    def run(self) -> None:
        if not self.is_within_working_hours:
            logger.info("Outside of working hours. Sleeping until next working day starts.")
            self.wait_until_next_working_hour()
            return

        if users_to_remind := self.identify_users_to_remind():
            self.slack.send_reminders(users_to_remind)
        else:
            logger.info("No one to remind")

        time.sleep(CHECKING_PERIOD)
        logger.info("Waiting...")
