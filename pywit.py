# import tweepy
# Auth=tweepy.OAuthHandler("98MAMigFUlLFEoc9Kd6auAHSa","UYET2zUWOCDyTC2rwlt9IV8eZFgzRwVWGozTVDZJ5UdgOO3AcG") 
# Auth.set_access_token("1783398570198282240-vUfwznLzj2vCeAgrSRwltWI07yiCL2","4NHcOHaCXD4Pc2SV5MKFkPGHbSRR0P5QSwkm5ComoaZjX") 
# api = tweepy.API(Auth) 
  
# try: 
#  api.verify_credentials() 
#  print("Authentication OK") 
# except: 
#  print("Error during authentication") 
# # Retrive trending topics for aspecific location(WOEID 1 in this example) 
# trends = api.get_place_trends(1) 
# # Print the trending topics 
# for trend in trends[0]['trends']: 
#  print(trend['name'])



import tweepy
consumer_key ='SCzIhCCZZrz7Q79bvputU7z7a'
consumer_secret ='6dUiAxKyoSd7UUokKRn1Jt3wcF76NUF0w06Dq8yPv7Go2Gfehy'

access_token="1788591014627684352-akw86B4W0BMFOYRBh7bbuRmn45vg62"
access_secret ="yc3habX6NJPVH3xIYdxdQUYO03JVIpyAHaMvwT6VTyjA0"
Client = tweepy.Client(
        consumer_key = consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_secret)

# response = Client.create_tweet(
#     text='Kaustubh Kolhe')
# print("POST CREATED")

try: 
  Client.create_tweet(
    text='Kaustubh Kolhe')
  print("POST CREATED SUCCESSFULLY")

except: 
  print("FAILED") 
