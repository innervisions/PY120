class Tree:
    def __init__(self):
        self.type = "Generic Tree"


class Pine(Tree):
    def __init__(self):
        super().__init__()
        self.type = "Pine Tree"

pine = Pine()
print(pine.type) # Pine Tree

# type attribute will be initialized to "Generic Tree" when super().__init__ is called,
# then re-assigned.
