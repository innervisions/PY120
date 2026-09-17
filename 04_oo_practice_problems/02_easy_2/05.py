class Hello:
    def hi(self):
        self.greet("Hello")

    # Make sure you define the class method after
    # the instance method. If you try it the other
    # way, the question below will prove a bit
    # challenging.
    @classmethod
    def hi(cls):
        greeting = Greeting()
        greeting.greet("Hi")
