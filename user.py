import requests

from settings import FORBIDDEN_COUNTRIES, GEOIP_API_URL, IGNORE_MOBILE_CLIENTS, logger


class User:
    def __init__(self, login, users_to_remind):
        self.id = login["user_id"]
        self.username = login["username"]
        self.agent = login["user_agent"]
        self.ip = login["ip"]
        self.geo = self.get_geo_by_ip()
        self.country = self.geo["country"]
        self.countryCode = self.geo["countryCode"]
        self.is_need_to_remind = self.is_need_to_remind(users_to_remind)

    def _is_mobile_client(self) -> bool:
        if IGNORE_MOBILE_CLIENTS:
            return False
        return "iPhone" in self.agent or "Android" in self.agent

    def is_need_to_remind(self, users_to_remind) -> bool:
        return (
            self.countryCode in FORBIDDEN_COUNTRIES
            and self.id not in users_to_remind
            and not self._is_mobile_client()
        )

    def get_geo_by_ip(self) -> dict | None:
        try:
            response = requests.get(f"{GEOIP_API_URL}{self.ip}")
        except TimeoutError:
            logger.error("Timeout error while getting geo by ip")
            return None
        return response.json()

    def __str__(self):
        return f"User {self.username} with {self.id} is from forbidden country {self.country}"

    def __repr__(self):
        return self.__str__()
