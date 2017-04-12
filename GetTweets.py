from twitter import *
import os

t = Twitter(
    auth=OAuth(
    "24402771-ubOY1IpmOG5ibnIXj3BzTJsNDN6XiHczABU5Ye28P",
    "SECNSAYwvYKpfoqvfl6LPDYu9I9R31u4NOMaocXnbRHZa",
    "9Q4DuLLm6cBwvT2lZ4lTl6EEV",
    "1Qd75eOOGxF5eOvPRdy3O7QngDAEvewzRnmBcfvOCl6jZDD3hj")
    )
tweets = t.statuses.user_timeline(screen_name="dog_rates", count=5000)
cache = open("tweetStore",'w')
for tw in tweets:
    print(tw['text'])
    cache.write(tw['text'].encode('utf8'))
    cache.write("\n".encode('utf8'))
cache.close();
