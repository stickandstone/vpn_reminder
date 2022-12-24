import time

import requests
from slack import WebClient

from settings import (
    SLACK_TOKEN,
    SLACK_TOKEN_CHAT,
    WARNING_MESSAGE,
    CHECKING_LOGIN_PERIOD,
    ADD_JOKE_TO_MESSAGE,
    logger,
)


class SlackClient:
    def __init__(
        self,
    ):
        self.chat_client = WebClient(token=SLACK_TOKEN_CHAT)
        self.workspace_client = WebClient(token=SLACK_TOKEN)

    def generate_message(self) -> str:
        if ADD_JOKE_TO_MESSAGE:
            try:
                response = requests.get("https://jokesrv.rubedo.cloud/facts")
            except TimeoutError:
                logger.error("Timeout error while getting a joke/fact")
                return ""
            return response.json()["content"]
        return ""

    def send_private_message(self, user_id: str) -> None:
        text = self.generate_message() + WARNING_MESSAGE
        logger.info(f"{text=}")
        self.chat_client.chat_postMessage(channel=user_id, text=text)

    def send_reminders(self, remind_list: list) -> None:
        logger.info("Sending reminding...")
        for user_id in remind_list:
            logger.info(f"Sending message to {user_id}")
            self.send_private_message(user_id)

    def filter_recent_logins(self, logins: list) -> list:
        return [
            login
            for login in logins
            if login["date_last"] > time.time() - CHECKING_LOGIN_PERIOD
        ]

    def get_logins(self) -> list:
        logins = self.workspace_client.team_accessLogs(count=100)
        return self.filter_recent_logins(logins["logins"])
