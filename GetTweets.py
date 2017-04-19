from twitter import *
import os
import config
def getTweets(consumer1,consumer2,secret1,secret2,cacheName="tweetStore"):
    t = Twitter(
        auth=OAuth(consumer1,consumer2,secret1,secret2)
        )
    numtweets = 0;
    numgoal = 2500;
    tweets = t.statuses.user_timeline(screen_name="dog_rates", include_rts=0)
    cache = open(cacheName,'w')
    numtweets += len(tweets);

    while numtweets < numgoal:
        ids = []
        for tw in tweets:
            ids.append(tw['id'])
            cache.write(tw['text'].encode('utf8'))
            cache.write("\n".encode('utf8'))
        minId = min(ids)
        numtweets += len(tweets)
        tweets = t.statuses.user_timeline(screen_name="dog_rates", include_rts=0, max_id=minId)
    cache.close();

def main():
    getTweets(
    config.consumer1,
    config.consumer2,
    config.secret1,
    config.secret2
    )
if __name__ == '__main__':
    main()
