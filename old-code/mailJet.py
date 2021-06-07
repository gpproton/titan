from mailjet_rest import Client
import os


def sendEmail(subject, toEmail, body):
    api_key = "6d8f0ad31d3bb36b6b1363308a090a0e"
    api_secret = "818df8b8369fd85a113ee7a4ec20046e"
    mailjet = Client(auth=(api_key, api_secret))
    data = {
        "FromEmail": "orion.reports@tolaram.com",
        "FromName": "Orion Reports",
        "Subject": subject,
        "Text-part": body,
        "Html-part": body,
        "Recipients": [{"Email": toEmail}],
    }
    result = mailjet.send.create(data=data)
    # print (result.status_code)
    # print (result.json())
