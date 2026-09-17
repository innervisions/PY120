class Greeting:
    def greet(self, message):
        print(message)


class Hello(Greeting):
    def hi(self):
        self.greet("Hello")


class Goodbye(Greeting):
    def bye(self):
        self.greet("Goodbye")

hello = Hello()
hello.hi()      # Hello

hello = Hello()
hello.bye()  # AttributeError raised

hello = Hello()
hello.greet()   # TypeError raised


hello = Hello()
hello.greet("Goodbye")   # Goodbye

Hello.hi()          # TypeError bc this is an instance method. Could be called on class with calling object as
                    # first argument.
