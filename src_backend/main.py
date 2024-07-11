import os
from dotenv import load_dotenv

load_dotenv()

REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")

class UnofficialRedditAPI:
    def __init__(self, username=None, password=None):
        self.username = username or REDDIT_USERNAME
        self.password = password or REDDIT_PASSWORD

        if not self.username or not self.password:
            raise ValueError("REDDIT_USERNAME and REDDIT_PASSWORD must be set either as environment variables or as constructor parameters")

    def authenticate(self):
        # Authentication logic here
        pass


# Example usage
if __name__ == "__main__":
    pass
