from telegram import Update
from telegram.ext import CallbackContext
import subprocess
from config import OWNER_ID

# Deploy bot from GitHub repository
def deploy_github(update: Update, context: CallbackContext):
    if len(context.args) < 1:
        update.message.reply_text("Usage: /deploy_github <repo_url>")
        return

    repo_url = context.args[0]
    user_id = update.message.from_user.id

    # Check if the user is authorized (owner only)
    if user_id != OWNER_ID:
        update.message.reply_text("You are not authorized to deploy bots.")
        return

    # Command to clone the repo and build the Docker image
    bot_id = repo_url.split("/")[-1]
    subprocess.run(["git", "clone", repo_url])
    subprocess.run(["docker", "build", "-t", bot_id, bot_id])

    update.message.reply_text(f"Bot {bot_id} deployed successfully from {repo_url}.")

# Stop a running bot
def stop_bot(update: Update, context: CallbackContext):
    if len(context.args) < 1:
        update.message.reply_text("Usage: /stop_bot <bot_id>")
        return

    bot_id = context.args[0]
    subprocess.run(["docker", "stop", bot_id])
    subprocess.run(["docker", "rm", bot_id])

    update.message.reply_text(f"Bot {bot_id} stopped and removed successfully.")

# Delete a bot
def delete_bot(update: Update, context: CallbackContext):
    if len(context.args) < 1:
        update.message.reply_text("Usage: /delete_bot <bot_id>")
        return

    bot_id = context.args[0]
    subprocess.run(["rm", "-rf", bot_id])  # Remove bot files from the system
    update.message.reply_text(f"Bot {bot_id} deleted successfully.")
