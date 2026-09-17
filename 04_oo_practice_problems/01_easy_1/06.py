import random


class Oracle:
    def predict_the_future(self):
        return f"You will {random.choice(self.choices())}."

    def choices(self):
        return [
            "eat a nice lunch",
            "take a nap soon",
            "stay at work late",
            "adopt a cat",
        ]


oracle = Oracle()
print(oracle.predict_the_future())
 # Will print a random message from the list returned in choices.
