import tweepy
api_key ="SCzIhCCZZrz7Q79bvputU7z7a"
api_secret ="6dUiAxKyoSd7UUokKRn1Jt3wcF76NUF0w06Dq8yPv7Go2Gfehy"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAJnftgEAAAAAIlvJPXbGYJwP69%2Bcs1n1A3DTy14%3DvONKQi35xJQfjmGR5x168tPB8lYcVpG5D8OMRbGxegOE18xn5o"
access_token="1788591014627684352-akw86B4W0BMFOYRBh7bbuRmn45vg62"
access_token_secret ="yc3habX6NJPVH3xIYdxdQUYO03JVIpyAHaMvwT6VTyjA0"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

#client.delete_tweet(1789226959052165169,user_auth=True)

try: 
  client.create_tweet(text="Hello Everyone This IS GHOSTRIDERS")
  print("POST CREATED SUCCESSFULLY")

except: 
  print("FAILED")
