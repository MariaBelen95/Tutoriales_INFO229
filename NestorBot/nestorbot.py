# import the random library to help us generate the random numbers
import random

class NestorBot:

    # Create a constant that contains the default text for the message
    HOLA_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hola! "
            ),
        },
    }

    # The constructor for the class. It takes the channel name as the a
    # parameter and then sets it as an instance variable
    def __init__(self, channel):
        self.channel = channel

    # Generate a random number to simulate the decision between "Buenos días" y "Buenas tardes". Then return the
    # crafted slack payload with the message.
    def _choose_message(self):
        rand_int =  random.randint(0,1)
        if rand_int == 0:
            results = "Buenos días!"
        else:
            results = "Buenas tardes!"

        text = f"{results}"

        return {"type": "section", "text": {"type": "mrkdwn", "text": text}},

    # Craft and return the entire message payload as a dictionary.
    def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                self.HOLA_BLOCK,
                *self._choose_message(),
            ],
        }
