# Good variable names
name = "Raza"
length = len(name)

print(name)
print(length)

# Multiple words use underscores
user_name = "Raza Hussain"
print(user_name)

# Numbers can be used, but not at the beginning
length1 = 5
length2 = 10

print(length1)
print(length2)


# Examples of INVALID variable names
# (Commented out to avoid errors)


# user name = "Raza"      # SyntaxError (spaces not allowed)
# 1length = 5             # SyntaxError (cannot start with a number)
# 3length = 10            # SyntaxError

# Avoid using Python keywords/functions as variable names
# print = "Hello"         # Bad practice
# input = "Raza"          # Bad practice


# NameError Example


name = "Angela"

# Uncomment the next line to see a NameError
# print(nama)

# Correct spelling
print(name)

# Python only cares about consistency
nama = "Player Nama"
print(nama)