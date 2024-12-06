from cragAndCanyonArticles import get_summary as get_cragAndCanyon_summaries
from rockyMountainOutlookArticles import get_summary as rockyMountainOutlook_summaries
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
RECIPIENT_PHONE_NUMBER = os.getenv("RECIPIENT_PHONE_NUMBER")

def send_text_via_twilio(message, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, RECIPIENT_PHONE_NUMBER):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=RECIPIENT_PHONE_NUMBER
        )
        print(f"Message sent! SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")

def main():
    summaries_1 = get_cragAndCanyon_summaries() 

    summaries_2 = rockyMountainOutlook_summaries()

    crag_and_canyon_message = "Top News Summaries from the Crag and Canyon:\n" + "\n".join(summaries_1)
    rocky_outlook_message = "Top News Summaries from the Rocky Mountain Outlook:\n" + "\n".join(summaries_2)

    send_text_via_twilio(crag_and_canyon_message)
    send_text_via_twilio(rocky_outlook_message)

if __name__ == "__main__":
    main()
