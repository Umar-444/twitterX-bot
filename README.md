# Twitter Bot

A simple Python Twitter bot that automatically posts tweets at scheduled intervals.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get Twitter API credentials:**
   - Go to [Twitter Developer Portal](https://developer.twitter.com/)
   - Create a new app and get your API keys
   - Generate access tokens

3. **Set environment variables:**
   Create a `.env` file in the project root:
   ```
   API_KEY=your_api_key_here
   API_SECRET=your_api_secret_here
   ACCESS_TOKEN=your_access_token_here
   ACCESS_SECRET=your_access_secret_here
   ```

   Or export them directly:
   ```bash
   export API_KEY="your_api_key_here"
   export API_SECRET="your_api_secret_here"
   export ACCESS_TOKEN="your_access_token_here"
   export ACCESS_SECRET="your_access_secret_here"
   ```

4. **Run the bot:**
   ```bash
   python bot.py
   ```

## Features

- Posts 3 random tweets per day
- 8-hour intervals between posts
- Uses predefined tweet content
- Continuous operation

## Security Note

Never commit your API credentials to version control. Always use environment variables.