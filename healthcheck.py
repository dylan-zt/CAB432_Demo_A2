"""Simple health check for the Flask demo application."""

import sys
from urllib.error import URLError
from urllib.request import urlopen


APP_URL = "http://localhost:5000/"


def check_application() -> int:
    """Return 0 when the Flask app responds successfully, otherwise 1."""
    try:
        with urlopen(APP_URL, timeout=3) as response:
            if response.status == 200:
                print("Application is healthy")
                return 0

            print(f"Application returned HTTP {response.status}")
            return 1

    except URLError as error:
        print(f"Application is unavailable: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(check_application())
