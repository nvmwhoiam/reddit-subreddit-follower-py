import praw
import re

def follow_subreddits_from_urls(subreddit_urls, client_id, client_secret, user_agent, username, password):
    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
            username=username,
            password=password
        )
        
        if not reddit.user.me():
            print("Authentication failed. Check your credentials.")
            return

        print(f"Logged in as: {reddit.user.me()}")

        for url in subreddit_urls:
            try:
                match = re.search(r"reddit\.com/r/([^/]+)/?", url)
                if not match:
                    print(f"Invalid URL: {url}")
                    continue
                
                subreddit_name = match.group(1)
                subreddit = reddit.subreddit(subreddit_name)
                subreddit.subscribe()
                print(f"Subscribed to r/{subreddit_name}")
            except Exception as e:
                print(f"Failed to subscribe to URL {url}: {e}")

    except Exception as e:
        print(f"Error initializing Reddit client: {e}")

if __name__ == "__main__":
    subreddit_urls = [
        "https://www.reddit.com/r/london/",
        "https://www.reddit.com/r/python/",
        "https://www.reddit.com/r/learnprogramming/"
    ]
    
    CLIENT_ID = "your_client_id"
    CLIENT_SECRET = "your_client_secret"
    USER_AGENT = "your_user_agent"
    USERNAME = "your_reddit_username"
    PASSWORD = "your_reddit_password"
    
    follow_subreddits_from_urls(
        subreddit_urls=subreddit_urls,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT,
        username=USERNAME,
        password=PASSWORD
    )