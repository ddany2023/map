name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your  height: "))
hobbies_input = input("Enter your hobies separated by comma: ")

hobbies = hobbies_input.split(',')
hobbies = [hobby.strip() for hobby in hobbies]

print("Name: ", name)
print("Age: ", age)
print("Height: ", height)
print("Hobbies: ", ", ".join(hobbies))