class KrispyKreme:
    def __init__(self, filling, glazing):
        self.filling = filling
        self.glazing = glazing

    # def __str__(self):
    #     description = self.filling or "Plain"
    #     if self.glazing:
    #         description += " with " + self.glazing
    #     return description

    # Put this code in the KrispyKreme class


    def __str__(self):
        options = []
        options.append(self.filling or "Plain")
        if self.glazing is not None:
            options.append(self.glazing)

        return " with ".join(options)


donut1 = KrispyKreme(None, None)
donut2 = KrispyKreme("Vanilla", None)
donut3 = KrispyKreme(None, "sugar")
donut4 = KrispyKreme(None, "chocolate sprinkles")
donut5 = KrispyKreme("Custard", "icing")

print(donut1)  # Plain
print(donut2)  # Vanilla
print(donut3)  # Plain with sugar
print(donut4)  # Plain with chocolate sprinkles
print(donut5)  # Custard with icing
