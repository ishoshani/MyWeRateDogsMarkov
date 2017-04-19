import DogBot;
import FilterTweets;
import GetTweets;
import SendSMS;

def doEverything():
    GetTweets.getTweets(
    "24402771-ubOY1IpmOG5ibnIXj3BzTJsNDN6XiHczABU5Ye28P",
    "SECNSAYwvYKpfoqvfl6LPDYu9I9R31u4NOMaocXnbRHZa",
    "9Q4DuLLm6cBwvT2lZ4lTl6EEV",
    "1Qd75eOOGxF5eOvPRdy3O7QngDAEvewzRnmBcfvOCl6jZDD3hj"
    )
    FilterTweets.filterOutGarbage()
    sentences = DogBot.generate(10)
    SendSMS.sendText(SendSMS.ACCT,SendSMS.TOKEN,toSend="14089210992",
    from_Send="16692216638",bodySend=sentences[0]);
def doFromCache():
    FilterTweets.filterOutGarbage()
    sentences = DogBot.generate(10)
    SendSMS.sendText(SendSMS.ACCT,SendSMS.TOKEN,toSend="14089210992",
    from_Send="16692216638",bodySend=sentences[0]);
def main():
    doFromCache()
if __name__ == '__main__':
    main()
