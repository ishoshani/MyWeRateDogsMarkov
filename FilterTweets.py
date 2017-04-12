import os
cache = open("tweetStore","r");
filtered = open("filteredTweets","w")
actualTweets = []
for tweet in cache:
    if(tweet[0]=="@" or (tweet[0]=="R" and tweet[1]=="T")):
        pass
    else:
        textandpic = tweet.split("http")
        justText = textandpic[0]
        print(justText)
        filtered.write(justText)
        filtered.write(".\n")
