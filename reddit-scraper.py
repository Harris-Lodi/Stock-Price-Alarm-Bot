import praw

reddit_read_only = praw.Reddit(client_id="kJLu1YlJuhbhCuqpS3HTSw",         # your client id
                               client_secret="Zd3CEKwD9sThYBTBa2RdZ_HYPwtKZg",      # your client secret
                               user_agent="Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0")

subreddit = reddit_read_only.subreddit("AMD_Stock")
 
# Display the name of the Subreddit
print("Display Name:", subreddit.display_name)
 
# Display the title of the Subreddit
print("Title:", subreddit.title)
 
# Display the description of the Subreddit
print("Description:", subreddit.description)

for post in subreddit.hot(limit=5):
    print(post.title)
    print()