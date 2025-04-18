import tweepy

#Put your Bearer Token in the parenthesis below
client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAJnftgEAAAAAIlvJPXbGYJwP69%2Bcs1n1A3DTy14%3DvONKQi35xJQfjmGR5x168tPB8lYcVpG5D8OMRbGxegOE18xn5o")

# Get tweets that contain the hashtag #petday
# -is:retweet means I don't want retweets
# lang:en is asking for the tweets to be in english
query = '#ghost -is:retweet lang:en'
tweets = tweepy.Paginator(client.search_recent_tweets, query=query,
                              tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=1000)

for tweet in tweets:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)