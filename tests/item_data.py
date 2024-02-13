from datetime import datetime
from random import randint

from tests.utils import random_email, random_lower_string


def user_dict() -> dict[str, str]:
    return {"name": random_lower_string(), "email": random_email()}


def request_dict() -> dict[str, datetime]:
    return {"issue_date": datetime.now(), "update_date": datetime.now()}


def block_storage_dict() -> dict[str, int]:
    return {
        "gigabytes": randint(0, 100),
        "per_volume_gigabytes": randint(0, 100),
        "volumes": randint(0, 100),
    }


def compute_dict() -> dict[str, int]:
    return {
        "cores": randint(0, 100),
        "instances": randint(0, 100),
        "ram": randint(0, 100),
    }


def network_dict() -> dict[str, int]:
    return {
        "networks": randint(0, 100),
        "ports": randint(0, 100),
        "public_ips": randint(0, 100),
        "security_groups": randint(0, 100),
        "security_group_rules": randint(0, 100),
    }