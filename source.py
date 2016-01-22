import facebook
import os

token = os.environ['FB_TOKEN']
graph = facebook.GraphAPI(access_token=token)

profile = graph.get_object("me")

#friends = graph.get_connections("me", "friends")

graph.put_object("me", "feed", message="I am writing on my timeline!")
