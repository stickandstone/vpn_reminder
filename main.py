import time
import datetime

import pytz

from settings import (
    CHECKING_PERIOD,
    CHECK_WORKING_DAYS_AND_HOURS,
    WORKING_HOURS,
    WEEKEND,
    TIME_ZONE,
    logger,
)
from controller import Controller


def working_day_and_hours() -> bool:
    if CHECK_WORKING_DAYS_AND_HOURS:
        today = datetime.datetime.now(tz=pytz.timezone(TIME_ZONE))
        working_hours = WORKING_HOURS[0] <= today.hour < WORKING_HOURS[1]
        return today.weekday() not in WEEKEND and working_hours
    return True


def main():
    while True:
        controller = Controller()
        if working_day_and_hours():
            controller.run()
            logger.info("Waiting...")
            time.sleep(CHECKING_PERIOD)


if __name__ == "__main__":
    main()
