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

## Features

- 🕐 **Flexible Scheduling**: Configurable posting times and intervals
- 🔄 **Error Handling**: Automatic retry logic with exponential backoff
- 📝 **Comprehensive Logging**: Detailed logs to file and console
- ⚙️ **Configurable**: Environment-based configuration system
- 🛑 **Graceful Shutdown**: Proper signal handling for clean stops
- 🔐 **Security**: Credential validation and environment variable usage
- 📊 **Daily Limits**: Automatic daily post counting and limits
- 🌍 **Timezone Support**: Configurable timezone offsets

## 🖥️ System Requirements

- **Python**: 3.7 or higher
- **Internet Connection**: Required for Twitter API access
- **Twitter Developer Account**: With API v2 access

## 🛠️ Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get Twitter API credentials:**
   - Visit [Twitter Developer Portal](https://developer.twitter.com/)
   - Create a new Project/App
   - Generate API Key, API Secret, Access Token, and Access Secret
   - Ensure your app has **write permissions**

3. **Configure the bot:**
   ```bash
   cp config.example.env .env
   # Edit .env with your actual credentials
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

## 🚀 Deployment

### Local Development
```bash
python bot.py
```

### Cloud Deployment

**Railway/Heroku:**
```bash
# Set environment variables in dashboard
# Deploy automatically or with railway/heroku CLI
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

## 📊 Monitoring & Logs

The bot creates a `bot.log` file with detailed information about authentication, posting attempts, errors, and scheduling.

```bash
# View live logs
tail -f bot.log
```

## 🐛 Troubleshooting

**Common Issues:**
- Verify all API credentials are correct
- Check Twitter Developer Portal for app permissions
- Ensure your app has write permissions
- Confirm API v2 access (not v1.1)
- Twitter has rate limits; reduce `POSTS_PER_DAY` if hitting limits frequently

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Author:** Umar Pak  
**Email:** umarpak995@gmail.com  
**GitHub:** [umar-444](https://github.com/umar-444)  
**LinkedIn:** [umar444](https://linkedin.com/in/umar444)

## 🙏 Acknowledgments

- [Tweepy](https://github.com/tweepy/tweepy) - Twitter API library for Python
- [python-dotenv](https://github.com/theskumar/python-dotenv) - Environment variable management