import os

def filterOutGarbage(cacheName="tweetStore",filteredfile="filteredTweets"):
    cache = open(cacheName,"r");
    filtered = open(filteredfile,"w")
    actualTweets = []
    for tweet in cache:
        if(tweet[0]=="@" or (tweet[0]=="R" and tweet[1]=="T")):
            pass
        else:
            textandpic = tweet.split("http")
            justText = textandpic[0]
            filtered.write(justText)
            filtered.write(".\n")
def main():
    filterOutGarbage()

if __name__ == '__main__':
    main()
