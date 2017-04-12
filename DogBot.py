import markovify
import os
with open("filteredTweets","r") as f:
    text = f.read();
text_model = markovify.NewlineText(text)

successes = 0
for i in range(0,10):
 output = text_model.make_sentence();
 if(output is not None):
     print(output)
     successes+=1
print("got "+str(successes)+"out of 10")
