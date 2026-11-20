import os
from dotenv import load_dotenv

load_dotenv()

def get_env(key: str) -> str:
    value = os.getenv(key)

    if value is None:
        raise ValueError("Invalid environment key. Make sure the key name is spelt correctly and that it exists in your environment variables")

    return value