#----------------------------------- https://github.com/m4mallu/DeleteMediaRobot -------------------------------------#

import os
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "DeleteMediaRobot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7148114178:AAGpKYE4hsBg7INn0LqPryseKvSrreP_ZSM")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "22894706"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "13c8f765d49c935d2ffd9152f8430f7e")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQC6kfsABhUpjLg4BUPOk-ot7uV_MX25n370c6mwHvUFp1GMAaJEwYHg_UEl4jTqGtGg0Zm_ijo4UzB8VMUVHCVSEW-6zrPXMu5sWE3tZpamh7isq0pKwdw8IMHpyGCjy35DimhKibNvkUt1Zy9bfABJPIuUhuyTqcP9aGmt3HAyJF3dj7UgdyLwjDcURuZ636UicPqKpYFj1wR2fqvIJwCsVcEkh0DQmYsQrhN_kthgde6OWU_4wponGLG2-6cftFwvFX_HziYSGhCK4YisiJcY6lOZcQ4jPxRD9ENsMHrEtst_lK7NkXCGdJ_I4ZHxcbvKebOMenENtJOBvaI4c-fG7GGCCwAAAAGnUoSaAA")

    # Authorized users to perform delete messages in group
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6797820880").split())


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
