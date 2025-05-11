import os

# Function to check if the bot directory exists
def check_bot_directory(bot_id):
    return os.path.exists(bot_id)
