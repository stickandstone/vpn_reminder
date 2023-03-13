import time
import datetime
import pytz

from settings import (
    CHECKING_PERIOD,
    WORKING_HOURS,
    WEEKEND,
    TIME_ZONE,
    logger,
)
from slack_client import SlackClient
from user import User


class Controller:
    def __init__(self):
        self.slack = SlackClient()
        self.users_to_remind = []

    def is_within_working_hours(self) -> bool:
        today = datetime.datetime.now(tz=pytz.timezone(TIME_ZONE))
        working_hours = WORKING_HOURS[0] <= today.hour < WORKING_HOURS[1]
        return today.weekday() not in WEEKEND and working_hours

    def wait_until_next_working_hour(self):
        now = datetime.datetime.now(tz=pytz.timezone(TIME_ZONE))
        next_day = now + datetime.timedelta(days=1)
        next_start_time = datetime.datetime(
            year=next_day.year,
            month=next_day.month,
            day=next_day.day,
            hour=WORKING_HOURS[0],
            tzinfo=pytz.timezone(TIME_ZONE),
        )
        sleep_seconds = (next_start_time - now).total_seconds()
        time.sleep(sleep_seconds)

    def identify_users_to_remind(self) -> list:
        logger.info("Checking logins")
        logins = self.slack.get_logins()
        for login in logins:
            user = User(login, self.users_to_remind)
            if user.needs_reminder:
                self.users_to_remind.append(user.id)
                logger.info(user)
        return self.users_to_remind

    def run(self):
        if users_to_remind := self.identify_users_to_remind():
            self.slack.send_reminders(users_to_remind)
        else:
            logger.info("No one to remind")
        self.users_to_remind = []


def main():
    controller = Controller()

    while True:
        if controller.is_within_working_hours():
            controller.run()
            logger.info("Waiting...")
            time.sleep(CHECKING_PERIOD)
        else:
            logger.info(
                "Outside of working hours. Sleeping until next working day starts."
            )
            controller.wait_until_next_working_hour()


if __name__ == "__main__":
    main()
