import requests
import facebook
import json
#Your Access Keys
page_id_1 = 254704574402358
# Your Page Access Token
def main():
    facebook_access_token_1 ='EAANo8X4fNswBO8lxNdjIP0OO0i4tFa2zb9vlXWN5VJsMOxPOhUdApqcSLfAlaSggwfzgKdXiM4eZCh71Pkvl4ZB0XRNDw0ZCkduRcvxO3yr2dKjFZCqyN136gV9OeATYEqfaN3ycbXwZBFM91kTpMfScee9Udy4XwMRYEZCb7UkZCvVJ1GlOFZAzPScixWRQ63FFrHFSWRa1DBIqN9BAGF1Ls1PgEy5b97IZD'
# Post Content as Text
    graph = facebook.GraphAPI(facebook_access_token_1)
 
    fields = ['id,name,about']

    profile = graph.get_object('me', fields = fields)

    print(json.dumps(profile, indent=4))

msg = 'Hi This Is Dnyaneshwar Kolhe'
post_url = 'https://graph.facebook.com/{}/feed'.format(page_id_1)
payload = {
'message': msg,
'access_token':'EAANo8X4fNswBO8lxNdjIP0OO0i4tFa2zb9vlXWN5VJsMOxPOhUdApqcSLfAlaSggwfzgKdXiM4eZCh71Pkvl4ZB0XRNDw0ZCkduRcvxO3yr2dKjFZCqyN136gV9OeATYEqfaN3ycbXwZBFM91kTpMfScee9Udy4XwMRYEZCb7UkZCvVJ1GlOFZAzPScixWRQ63FFrHFSWRa1DBIqN9BAGF1Ls1PgEy5b97IZD'
}
r = requests.post(post_url, data=payload)

print(r.text)
if __name__=="__main__":
        main()  