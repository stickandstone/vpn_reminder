from slack_client import SlackClient

from user import User
from settings import logger


class Controller:
    def __init__(self):
        self.slack = SlackClient()
        self.users_to_remind = []

    def get_list_whom_to_remind(self) -> list:
        logger.info("Checking logins")
        logins = self.slack.get_logins()
        for login in logins:
            user = User(login, self.users_to_remind)
            if user.is_need_to_remind:
                self.users_to_remind.append(user.id)
                logger.info(user)
        return self.users_to_remind

    def run(self):
        if users_to_remind := self.get_list_whom_to_remind():
            self.slack.send_reminders(users_to_remind)
        else:
            logger.info("No one to remind")
        self.users_to_remind = []
