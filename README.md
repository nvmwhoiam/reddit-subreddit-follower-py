# Reddit Subreddit Follower Bot

A Python-based script that automates subscribing to subreddits using their URLs. This tool utilizes the Reddit API (via `praw`) to authenticate a Reddit account and subscribe to specified subreddits provided in a list of URLs.

## Features

- Authenticate with the Reddit API using personal credentials.
- Automatically extract subreddit names from URLs.
- Subscribe to subreddits using their URLs (e.g., `https://www.reddit.com/r/python/`).
- Provides error handling for invalid URLs and failed subscriptions.

## Requirements

To run this script, you will need:

1. **Python 3.7 or later** installed.
2. A set of Reddit API credentials (client ID, client secret, etc.).
3. The `praw` library installed.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/nvmwhoiam/reddit-subreddit-follower.git
   cd reddit-subreddit-follower
   ```
2. **Install Dependencies: Install the required Python libraries:**

   ```bash
   pip install praw
   ```

3. **Set Up Reddit API Credentials:**

- Go to [Reddit App Preferences](https://www.reddit.com/prefs/apps).
- Create a new app and select "script" as the app type.
- Copy the `client_id`, `client_secret`, and set the `redirect_uri` to `http://localhost`.

## Usage

1. **Prepare Your Reddit API Credentials: Replace the following placeholders in the script with your actual credentials:**

- `CLIENT_ID`
- `CLIENT_SECRET`
- `USER_AGENT`
- `USERNAME`
- `PASSWORD`

2. **Prepare a List of Subreddit URLs: Update the `subreddit_urls` variable in the script with the subreddits you want to subscribe to. For example:**

```bash
subreddit_urls = [
    "https://www.reddit.com/r/python/",
    "https://www.reddit.com/r/london/",
    "https://www.reddit.com/r/learnprogramming/"
]
```

3. **Run the Script: Execute the script with Python:**

```bash
python follow_subreddits.py
```

4. **Output: The script will authenticate your Reddit account, process the URLs, and subscribe to the subreddits. Any errors (e.g., invalid URLs or subscription failures) will be printed to the console.**

## Example Output

```text
Logged in as: your_reddit_username
Subscribed to r/python
Subscribed to r/london
Subscribed to r/learnprogramming
```

## Configuration

### Reddit API Credentials

You will need to replace the placeholders in the script with your Reddit API credentials:

- `CLIENT_ID`: Found under the app name in your [Reddit App Preferences](https://www.reddit.com/prefs/apps).
- `CLIENT_SECRET`: Found next to "secret" in the app details.
- `USER_AGENT`: A short description of your app (e.g., `script:subreddit_follower:v1.0 (by u/your_username)`).
- `USERNAME`: Your Reddit username.
- `PASSWORD`: Your Reddit password.

## Notes

- Ensure that your Reddit account is in good standing to avoid issues with the API.
- Be mindful of Reddit's [API rate limits](https://github.com/reddit-archive/reddit/wiki/API). Add delays if subscribing to many subreddits in one go.

## Troubleshooting

1. **Authentication Failed:**

- Ensure your `client_id`, `client_secret`, `username`, and `password` are correct.
- Confirm that your app is correctly set up as a script type in [Reddit App Preferences](https://www.reddit.com/prefs/apps).

2. **Invalid URLs:**

- Check that the URLs provided are properly formatted (e.g., `https://www.reddit.com/r/python/`).
- The script automatically skips invalid URLs.

3. **Subscription Errors:**

- The script might fail if you're already subscribed to the subreddit or if the subreddit doesn't exist.

## Contact

If you have any questions or need assistance, please do not hesitate to reach out. I apologize if any part of this setup is not clear; this is my first major project, and I am putting in continuous effort to improve it. Feel free to contact me at [your email address] or open an issue on the [GitHub Repository](https://github.com/nvmwhoiam/reddit_subreddit_follower)
.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

- nvmwhoiam
- GitHub: [GitHub Profile](https://github.com/nvmwhoiam/)
