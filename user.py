import requests

from settings import (
    FORBIDDEN_COUNTRIES,
    GEOIP_API_URL,
    SKIP_MOBILE_CLIENTS_CHECK,
    logger,
)


def get_geo_by_ip(ip_address: str) -> dict | None:
    try:
        response = requests.get(f"{GEOIP_API_URL}{ip_address}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error while getting geo by IP. Error: {e}")
        return None
    return response.json()


class User:
    def __init__(self, login, users_to_remind):
        self.id = login["user_id"]
        self.username = login["username"]
        self.agent = login["user_agent"]
        self.ip = login["ip"]
        self.geo = get_geo_by_ip(self.ip)
        self.country = self.geo.get("country", "Unknown")
        self.countryCode = self.geo.get("countryCode", "Unknown")
        self.needs_reminder = self.is_need_to_remind(users_to_remind)

    def _is_mobile_client(self) -> bool:
        if SKIP_MOBILE_CLIENTS_CHECK:
            return False
        return "iPhone" in self.agent or "Android" in self.agent

    def is_need_to_remind(self, users_to_remind: list) -> bool:
        return (
            self.countryCode in FORBIDDEN_COUNTRIES
            and self.id not in users_to_remind
            and not self._is_mobile_client()
        )

    def __str__(self):
        return f"User {self.username} with {self.id} is from forbidden country {self.country}"

    def __repr__(self):
        return self.__str__()
