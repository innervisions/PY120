class A:
    def __init__(self):
        self.var_a = "A class variable"


class B(A):
    def __init__(self):
        self.var_b = "B class variable"


b = B()
print(b.var_a)  # AttributeError

# We never called A's init method so var_a instance variable will not be initialized.
