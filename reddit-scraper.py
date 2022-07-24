import praw
import pandas as pd 
from praw.models import MoreComments

reddit_read_only = praw.Reddit(client_id="kJLu1YlJuhbhCuqpS3HTSw",         # your client id
                               client_secret="Zd3CEKwD9sThYBTBa2RdZ_HYPwtKZg",      # your client secret
                               user_agent="Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0")

subreddit = reddit_read_only.subreddit("AMD_Stock")
 
# Display the name of the Subreddit
# print("Display Name:", subreddit.display_name)
 
# Display the title of the Subreddit
# print("Title:", subreddit.title)
 
# Display the description of the Subreddit
# print("Description:", subreddit.description)

# for post in subreddit.hot(limit=5):
#     print(post.title)
#     print()

posts = subreddit.top(time_filter="month", limit=10)
# Scraping the top posts of the current month

posts_dict = {"Title": [], "Post Text": [],
			"ID": [], "Score": [],
			"Total Comments": [], "Post URL": []
			}

for post in posts:
	# Title of each post
	posts_dict["Title"].append(post.title)
	
	# Text inside a post
	posts_dict["Post Text"].append(post.selftext)
	
	# Unique ID of each post
	posts_dict["ID"].append(post.id)
	
	# The score of a post
	posts_dict["Score"].append(post.score)
	
	# Total number of comments inside the post
	posts_dict["Total Comments"].append(post.num_comments)
	
	# URL of each post
	posts_dict["Post URL"].append(post.shortlink)

# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)

# print(top_posts)

# top_posts.to_csv("Top Posts.csv", index=True)

# get the url for a certain post from the data frame
post1 = top_posts._get_value(1, "Post URL")
# print(post1)

# get submissions
submission = reddit_read_only.submission(url=post1)

post_comments = []

for comment in submission.comments.list():
    if type(comment) == MoreComments:
        continue
 
    post_comments.append(comment.body)
 
# creating a dataframe
comments_df = pd.DataFrame(post_comments, columns=['comment'])
print(comments_df)

# so this works, but am now realizing Reddit may not be a useful site for getting this data in real time, thus this is now redundant