#Create an empty dictionary
student_info = {}

#Add key-value pairs for student's name, age and major
student_info["student_name"] = "Joe Bloggs"
student_info["age"] = 25
student_info["major"] = "Economics"

print(student_info)

#Modify the student's age and major 
student_info["age"] = 32
student_info["major"] = "French"

print(student_info)

#Remove the key-value pair for the student's major
del student_info["major"]

print(student_info)

#Use get() method to access a student's age
point_value = student_info.get("age", "No point value assigned")

print(point_value)