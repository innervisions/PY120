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


class RoadTrip(Oracle):
    def choices(self):
        return [
            "visit Vegas",
            "fly to Fiji",
            "romp in Rome",
            "go on a Scrabble cruise",
            "get hopelessly lost",
        ]

trip = RoadTrip()
print(trip.predict_the_future())

# Choices will come from RoadTrip's choices method as self in predict_the_future
# refers to the calling instance, an object of the RoadTrip class.
