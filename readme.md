"""
# Telegram Navigation Bot

Welcome to the **Telegram Navigation Bot**! This bot allows you to navigate between various Telegram channels and provides helpful information to users. Below, you'll find all the setup instructions, usage guidelines, and customization options you need to get started.

# 🚀 Setup Instructions

### Prerequisites
To get started, you'll need:
- **Python 3.x**: Ensure you have Python installed.
- **pip**: Python's package installer.
- **A Telegram bot token**: Get one from [BotFather](https://t.me/BotFather) on Telegram.

### Installation Steps
1. **Clone the repository**:
   ```
   git clone <repository_url>
   ```

2. **Install the required Python packages**:
   ```
   pip install -r requirements.txt
   ```

3. **Configure the bot token**:
   - Open `config.py` and add your bot token.

4. **Run the bot**:
   ```
   python main.py
   ```

# 📋 Usage

### Commands
- **/start**: 
  - Starts the bot and sends a welcome message, including buttons that link to relevant channels.
  - **Customization Required**: 
    1. Open `start.py` and locate the section where buttons are defined.
    2. Replace the URLs and button texts to match your needs.
    3. Make sure the button labels and channel links reflect your intended use.

- **/help**: 
  - Displays help information for users.
  - **Customization Required**: 
    1. Open the `messages/help.txt` file.
    2. Edit the content to provide customized help information specific to your bot.

# 🛠 Customization

### 🔘 Buttons and Links
- **File**: `start.py`
  - The bot provides buttons that link to different channels or resources.
  - To modify:
    1. Locate the `InlineKeyboardButton` definitions in `start.py`.
    2. Update the button labels and URLs to match your requirements.

### ✉️ Messages
- **Directory**: `messages/`
  - **Files**: `start.txt`, `help.txt`
  - Customize these text files to change the messages that the bot sends for `/start` and `/help` commands.
  - Make sure that the messages are relevant and informative for your users.

### 🖼 Images
- The bot sends an image in response to the `/start` command.
- **File Name**: `image.png`
- **Directory**: `messages/`
- **Instructions**:
  1. Place your desired image in the `messages/` directory.
  2. Make sure the image is named **`image.png`** so the bot can find and use it.
  3. You can replace the existing image with any other image of your choice, ensuring the filename remains the same.

# 📂 Directory Structure
- **`config.py`**: Contains configuration settings, such as the bot token.
- **`main.py`**: The main script to run the bot.
- **`start.py`**: Handles the `/start` command.
- **`help.py`**: Handles the `/help` command.
- **`messages/`**: Contains text files for customizable bot messages and images.
  - **`start.txt`**: Customizable message for the `/start` command.
  - **`help.txt`**: Customizable message for the `/help` command.
  - **`image.png`**: The image sent in response to the `/start` command.
- **`logs/`**: Contains log files for tracking bot activity and errors.

# 🤝 Contributing
We welcome contributions! Feel free to submit issues or pull requests to improve this bot.

- **Report Issues**: If you find any bugs or have suggestions, open an issue on GitHub.
- **Pull Requests**: Contributions are always welcome. Please make sure to update documentation as needed.

# 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

# 📞 Support
If you need any help, feel free to reach out or open an issue on GitHub.

Thank you for using **Telegram Navigation Bot**! We hope it helps make your Telegram experience more organized and enjoyable.