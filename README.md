# Bot Deployer

Bot Deployer ek Telegram bot management tool hai jo users ko GitHub repositories se bots ko Docker container me deploy karne ki suvidha deta hai. Users apne bots ko deploy, stop, delete, aur manage kar sakte hain.

## Features

- **GitHub Repo Deployment:** GitHub repository se bot ko clone aur deploy karna.
- **Docker Sandbox:** Har bot ko Docker container me securely run karna.
- **Free Bot Limit:** Har user ko 5 bots free me deploy karne ki suvidha milti hai.
- **Admin Privileges:** Bot owners aur sudo users ke liye unlimited bot hosting.
- **Auto-Start:** Server restart ke baad bots automatically start ho jate hain.
- **Command Line Interface (CLI):** Makefile ke through Docker containers aur bots ko manage karna.

## Prerequisites

- **Docker**: Docker containers ko run karne ke liye system pe Docker installed hona chahiye.
- **Docker Compose**: Docker containers ko easily manage karne ke liye Docker Compose hona chahiye.
- **Python 3.11+**: Telegram bot aur server management ke liye Python version 3.11 ya usse upar hona chahiye.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-repo/bot-deployer.git
    cd bot-deployer
    ```

2. **Create `.env` file:**  
   `.env` file ko root directory me create karen aur apni environment variables set karen:

    ```env
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
    OWNER_ID=123456789
    SUDO_USERS=111111111,222222222
    FREE_BOT_LIMIT=5
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Build Docker images:**

    ```bash
    make build
    ```

5. **Start the bot containers:**

    ```bash
    make up
    ```

## Usage

- **Start the bot:**

    ```bash
    make up
    ```

- **Stop and remove all containers:**

    ```bash
    make down
    ```

- **View logs of running containers:**

    ```bash
    make logs
    ```

- **Restart the containers:**

    ```bash
    make restart
    ```

- **Clean up unused Docker images and containers:**

    ```bash
    make clean
    ```

- **Deploy the bot:**

    GitHub repository se bot deploy karne ke liye `/deploy_github` command use karein.

    **Command format:**  
    `/deploy_github <repo_url>`

- **Stop a running bot:**

    Bot ko stop karne ke liye `/stop_bot` command ka use karein.

    **Command format:**  
    `/stop_bot <bot_id>`

- **Delete a bot:**

    Bot ko delete karne ke liye `/delete_bot` command ka use karein.

    **Command format:**  
    `/delete_bot <bot_id>`

## Auto-Start on Reboot

Server restart ke baad bots automatically start ho jayenge agar tumne `auto_start.py` ko configure kar rakha ho.

## File Structure

bot_deployer/
├── main.py                # Telegram bot starter <br>
├── handlers.py            # All command handlers (/deploy_github, /stop_bot, etc.) <br>
├── docker_manager.py      # Docker image/build/run/stop logic <br>
├── utils.py               # Utility functions (e.g., validation, path handling) <br>
├── config.py              # Owner ID, sudo list, limits, env loading<br>
├── auto_start.py          # Logic to auto-start bots on reboot<br>
├── .env                   # Config vars like TOKEN, OWNER_ID, etc.<br>
├── Makefile               # Automation for Docker and bot management<br>
├── requirements.txt       # Python dependencies<br>
└── docker-compose.yaml     # Docker Compose configuration
