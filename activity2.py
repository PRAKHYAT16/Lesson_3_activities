name="penguin"
age=15
is_student=True
weight=38.5
print("Data type of name is:", type(name))
print("Data type of age is:", type(age))
print("Data type of is_student is:", type(is_student))
print("Data type of weight is:", type(weight))
print("\n ---------AFTER TYPE CASTING---------")
age=str(age)
print(age)
print("Data type of age is", type(age))
weight=int(weight)
print(weight)
print("Data type of weight is", type(weight))
