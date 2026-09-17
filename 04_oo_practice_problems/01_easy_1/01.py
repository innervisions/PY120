# True
# "hello"
# [1, 2, 3, "happy days"]
# 142
# {1, 2, 3}
# 1.2345

#  All of the above are objects in Python.Find their class with built-in type function.
# eg type(True) == bool

# or __class__ magic instance variable.

print(True.__class__)  # <class 'bool'>
print("hello".__class__)  # <class 'str'>
print([1, 2, 3, "happy days"].__class__)  # <class 'list'>
print({1, 2, 3}.__class__)  # <class 'set'>
print((142).__class__)  # <class 'int'>
print((1.2345).__class__)  # <class 'float'>

print(True.__class__.__name__)  # bool
print("hello".__class__.__name__)  # str
print([1, 2, 3, "happy days"].__class__.__name__)  # list
print({1, 2, 3}.__class__.__name__)  # set
print((142).__class__.__name__)  # int
print((1.2345).__class__.__name__)  # float
