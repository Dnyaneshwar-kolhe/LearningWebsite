import json
import facebook

def main():
    token = {"EAAFIJjZBjiCwBO0ZAlPQ7ckEJ8DZCE8QfjVC9f7GiFsuNgyDV06yu94tYAROr1YCFOl4xNYAoPawK6hUxfbP6ZAGHRTQI9JNJdvVti0b4vP1D2j02txZAYfMB1cxtcQczA5FT9GDtR7v8uYEFZANdXHtMkwYgxhtNKcI0yJPLKoize82oZAZB9irgJO24WmrPSOzcjJx5wg687n6mmbPZBkH9XiKZCZB9KxDPX6G1U4LmZCbXSJZBW4w0Chb6R51S7ILM"}
    graph = facebook.GraphAPI(token)
 
    fields = ['email,sports,gender']

    profile = graph.get_object('me', fields = fields)

    print(json.dumps(profile, indent=4))

if __name__=="__main__":
        main()    