from twilio.rest import Client
import config
ACCT = config.ACCT
TOKEN = config.TOKEN
def sendText(acct,token,toSend,from_Send,bodySend):
    client = Client(acct,token)
    client.messages.create(to=toSend,from_=from_Send,body=bodySend);

def main():
    acct = ACCT
    token = TOKEN
    sendText(acct,token,
    toSend="14089210992",
    from_Send="16692216638",
    bodySend="This is Bo. He's a Snowy Swiss Mountain Floofapolis. Cheeky wink. Tongue nifty af. 11/10 keep doin you Tripp ."
    )



if __name__ == '__main__':
    main()
