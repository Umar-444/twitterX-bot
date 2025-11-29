# Twitter Bot 🤖

A robust Python Twitter bot that automatically posts tweets at scheduled intervals with advanced features for production use.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## 🚀 Quick Start

```bash
# 1. Clone and install
git clone <your-repo-url>
cd twitterX-bot
pip install -r requirements.txt

# 2. Setup credentials
cp config.example.env .env
# Edit .env with your Twitter API credentials

# 3. Run the bot
python bot.py
```

That's it! The bot will start posting according to your configuration.

## Features

- 🕐 **Flexible Scheduling**: Configurable posting times and intervals
- 🔄 **Error Handling**: Automatic retry logic with exponential backoff
- 📝 **Comprehensive Logging**: Detailed logs to file and console
- ⚙️ **Configurable**: Environment-based configuration system
- 🛑 **Graceful Shutdown**: Proper signal handling for clean stops
- 🔐 **Security**: Credential validation and environment variable usage
- 📊 **Daily Limits**: Automatic daily post counting and limits
- 🌍 **Timezone Support**: Configurable timezone offsets
- 🎯 **Smart Resumption**: Remembers last post time and resumes schedule
- 📈 **Production Ready**: 24/7 operation with proper error recovery

## 📁 Project Structure

```
twitterX-bot/
├── bot.py                 # Main bot application
├── config.example.env     # Example configuration file
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .gitignore            # Git ignore rules
└── bot.log              # Generated log file (after running)
```

## 🖥️ System Requirements

- **Python**: 3.7 or higher
- **Internet Connection**: Required for Twitter API access
- **Twitter Developer Account**: With API v2 access
- **Storage**: ~10MB for logs and dependencies

## 🛠️ Setup

### Prerequisites

1. **Python 3.7+** installed on your system
2. **Twitter Developer Account** with API access

### Step-by-Step Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd twitterX-bot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get Twitter API credentials:**
   - Visit [Twitter Developer Portal](https://developer.twitter.com/)
   - Create a new Project/App
   - Generate API Key, API Secret, Access Token, and Access Secret
   - Ensure your app has **write permissions**

4. **Configure the bot:**
   ```bash
   # Copy the example configuration
   cp config.example.env .env

   # Edit .env with your actual credentials
   nano .env  # or use your preferred editor
   ```

   **Required credentials in `.env`:**
   ```env
   API_KEY=your_actual_api_key
   API_SECRET=your_actual_api_secret
   ACCESS_TOKEN=your_actual_access_token
   ACCESS_SECRET=your_actual_access_secret
   ```

   **Optional configuration:**
   ```env
   POSTS_PER_DAY=3              # Number of posts per day (default: 3)
   HOURS_BETWEEN_POSTS=8        # Hours between posts (default: 8)
   START_HOUR=9                 # Hour to start posting (0-23, default: 9)
   TIMEZONE_OFFSET=0            # UTC offset in hours (default: 0)
   MAX_RETRIES=3                # Max retry attempts (default: 3)
   RETRY_DELAY=60               # Delay between retries in seconds (default: 60)
   ```

4. **Run the bot:**
   ```bash
   python bot.py
   ```

## Configuration Options

| Variable | Default | Description |
|----------|---------|-------------|
| `POSTS_PER_DAY` | 3 | Number of tweets to post per day |
| `HOURS_BETWEEN_POSTS` | 8 | Hours to wait between posts |
| `START_HOUR` | 9 | Hour of day to start posting (24-hour format) |
| `TIMEZONE_OFFSET` | 0 | UTC offset for scheduling (in hours) |
| `MAX_RETRIES` | 3 | Maximum retry attempts for failed posts |
| `RETRY_DELAY` | 60 | Seconds to wait between retry attempts |

## 🚀 Advanced Usage & Deployment

### Usage Examples

#### Basic Setup (Default)
Just set the API credentials and run - posts 3 tweets per day starting at 9 AM UTC.

#### Custom Schedule Examples

**Business Hours Posting:**
```env
POSTS_PER_DAY=5
HOURS_BETWEEN_POSTS=4
START_HOUR=8
TIMEZONE_OFFSET=-5  # Eastern Time
```
Posts 5 tweets per day, every 4 hours, starting at 8 AM Eastern Time.

**High-Frequency Engagement:**
```env
POSTS_PER_DAY=10
HOURS_BETWEEN_POSTS=2
START_HOUR=6
```
Posts 10 tweets per day, every 2 hours, starting at 6 AM.

**Weekend Special:**
```env
POSTS_PER_DAY=6
HOURS_BETWEEN_POSTS=3
START_HOUR=10
TIMEZONE_OFFSET=-8  # Pacific Time
```

### Deployment Options

#### Local Development
```bash
# Run directly
python bot.py

# Run in background (Linux/Mac)
nohup python bot.py &

# Run with process manager
pip install supervisor
# Configure supervisor for process management
```

#### Cloud Deployment

**Railway:**
```bash
# Railway automatically detects Python apps
# Set environment variables in Railway dashboard
# Deploy with: railway deploy
```

**Heroku:**
```yaml
# Procfile
worker: python bot.py
```
```bash
# Set config vars in Heroku dashboard
heroku config:set API_KEY=your_key_here
```

**Docker:**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "bot.py"]
```

#### VPS/Cloud Server
```bash
# Install dependencies
sudo apt update
sudo apt install python3 python3-pip
pip install -r requirements.txt

# Use systemd for production
sudo nano /etc/systemd/system/twitter-bot.service
```

**Systemd Service Configuration:**
```ini
[Unit]
Description=Twitter Bot Service
After=network.target

[Service]
Type=simple
User=your-user
WorkingDirectory=/path/to/twitterX-bot
ExecStart=/usr/bin/python3 bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**Start the service:**
```bash
sudo systemctl daemon-reload
sudo systemctl enable twitter-bot
sudo systemctl start twitter-bot
sudo systemctl status twitter-bot
```

## 📊 Monitoring & Logs

### Log Files
The bot creates a `bot.log` file with detailed information about:
- ✅ Authentication status
- 📝 Tweet posting attempts and results
- ⚠️ Error messages and retry attempts
- 🕐 Scheduling information
- 🛑 Shutdown events

### Real-time Monitoring
```bash
# View live logs
tail -f bot.log

# Or run the bot in foreground to see console output
python bot.py
```

### Log Format
```
2024-01-15 09:00:01,234 - INFO - 🚀 Starting Twitter Bot...
2024-01-15 09:00:01,456 - INFO - Successfully authenticated as: @your_username
2024-01-15 09:00:01,567 - INFO - ✅ Tweet posted (1/3): Your tweet content here...
```

## Stopping the Bot

To stop the bot gracefully:
- Press `Ctrl+C` in the terminal
- Send a `SIGTERM` signal to the process

The bot will complete any ongoing operations before shutting down.

## Security Notes

- ✅ Never commit your `.env` file or API credentials to version control
- ✅ Use environment variables for all sensitive data
- ✅ The bot validates credentials before starting
- ✅ All credentials are required and checked at startup

## 🎨 Customizing Tweet Content

### Current Tweet Library
The bot includes 10 diverse tweets covering:
- 🤖 Automation and AI themes
- 💻 Developer and coding content
- ☕ Productivity and motivation
- 📈 Learning and growth
- 🌐 Technology trends

### Adding Custom Tweets

**Option 1: Edit the code directly**
```python
# In bot.py, modify the self.tweets list
self.tweets = [
    "Your custom tweet here! 🎉",
    "Another engaging tweet content 📱",
    "Keep your audience interested! 🚀",
    # ... add more tweets
]
```

**Option 2: Load from file (Recommended)**
Create a `tweets.txt` file:
```
Your first tweet here!
Another interesting tweet 🌟
Keep them coming! 📈
```

Then modify `bot.py` to load from file:
```python
# Add this in __init__ method
try:
    with open('tweets.txt', 'r', encoding='utf-8') as f:
        self.tweets = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    # Fall back to default tweets
    pass
```

### Tweet Best Practices
- 📏 Keep tweets under 280 characters
- 🎯 Include relevant emojis (1-2 per tweet)
- ❓ Ask questions to encourage engagement
- 🔗 Include calls-to-action when appropriate
- 📊 Mix content types (educational, inspirational, fun)
- 🕐 Vary posting times for different audiences

## 🐛 Troubleshooting

### Common Issues

**Authentication Errors:**
- ❌ Verify all API credentials are correct
- ❌ Check Twitter Developer Portal for app permissions
- ❌ Ensure your app has write permissions
- ❌ Confirm API v2 access (not v1.1)

**Rate Limiting:**
- ⚠️ Twitter has rate limits; the bot includes retry logic
- ⚠️ If you hit limits frequently, reduce `POSTS_PER_DAY`
- ⚠️ Free tier allows ~300 posts per 3 hours

**Scheduling Issues:**
- ❌ Check your `TIMEZONE_OFFSET` setting
- ❌ Verify `START_HOUR` is in 0-23 range
- ❌ Check logs for scheduling information
- ❌ Ensure system time is correct

**Permission Errors:**
```bash
# Fix file permissions
chmod +x bot.py
# Ensure log file is writable
touch bot.log
chmod 644 bot.log
```

### Debug Mode
Add to your `.env` for verbose logging:
```env
LOG_LEVEL=DEBUG
```

### Health Checks
```bash
# Check if bot is running
ps aux | grep python
# View recent logs
tail -20 bot.log
# Check system resources
top -p $(pgrep -f bot.py)
```

## 🔗 API Considerations

### Twitter API v2
- ✅ Uses Tweepy with API v2 support
- ✅ Handles authentication properly
- ✅ Respects rate limits automatically

### Rate Limits (Free Tier)
- **Posts**: 300 per 3 hours
- **Authentication**: 75 requests per 15 minutes
- **Bot automatically handles these limits**

### Cost Considerations
- **Free Tier**: Sufficient for most personal use
- **Basic Tier**: $100/month for higher limits
- **Pro Tier**: $5000/month for enterprise use

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
git clone https://github.com/your-username/twitterX-bot.git
cd twitterX-bot
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp config.example.env .env
# Edit .env with test credentials
python bot.py
```

## 🙏 Acknowledgments

- [Tweepy](https://github.com/tweepy/tweepy) - Twitter API library for Python
- [python-dotenv](https://github.com/theskumar/python-dotenv) - Environment variable management
- Twitter Developer Platform for API access

## 📞 Support

If you encounter issues:
1. Check the logs in `bot.log`
2. Review the troubleshooting section above
3. Verify your configuration in `.env`
4. Check Twitter API status: https://api.twitterstat.us/

For bugs or feature requests, please [open an issue](https://github.com/your-username/twitterX-bot/issues) on GitHub.