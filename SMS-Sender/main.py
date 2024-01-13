from twilio.rest import Client

account_sid = "Your Account SID"
auth_token = "Your Account Auth Token"
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="+12067526294", body="Hello World using Python", to="Your Mobile Number"
)

print(message.sid)
