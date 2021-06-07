from urlAssit import Callback
import base64


def sendSMS(pmsg):

    # Declare auth processing
    usrPass = "Panabiz:Schuster1!"
    b64Val = base64.b64encode(usrPass.encode()).decode()
    authval = "Basic %s" % b64Val

    parameters = {
        "callType": "POST",
        "host": "https://api.infobip.com/sms/1/text/single",
        "headers": {
            "Content-Type": "application/json",
            "Accept-Charset": "UTF-8",
            "Authorization": authval,
        },
        "body": {
            "from": "MCPL",
            "to": ["+2347017745329", "+2348153494051", "+2348081473292"],
            "text": pmsg,
        },
        "params": {},
    }

    response = Callback(parameters)
    response.execute()
    print(response.result())
