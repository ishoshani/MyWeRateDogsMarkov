import markovify
import os

def generate(howMany, filteredfile="filteredTweets"):
    sentences = [];
    with open(filteredfile,"r") as f:
        text = f.read();
    text_model = markovify.NewlineText(text)
    for i in range(0,howMany):
        output = text_model.make_sentence();
        if(output is not None):
            sentences.append(output)
    return sentences
def main():
    s = generate(10)
    for str in s:
        print(str)
if __name__ == '__main__':
    main()
