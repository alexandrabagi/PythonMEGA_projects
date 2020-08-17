"""import datetime
print("The date and time is", datetime.datetime.now())

monday_temperatures = [9.1, 8.8, 7.5]
student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}

mysum = sum(student_grades.values())
mylen = len(student_grades)
mymean = mysum / mylen
print(mymean)"""

def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else: 
        return "Cold"

user_input = float(input("Enter temperature: "))
print(weather_condition(user_input))

def area(a, b=5):
    return a * b

print(area(4, 4))
