info = {
    "name" : "divyansh raj",
    "age" : "15",
    "class" : "nineth",
    "is_adulit": False,
}
print(info) #{'name': 'divyansh raj', 'age': '15', 'class': 'nineth', 'is_adulit': False}
print(type(info)) #<class 'dict'>
print(info["age"]) #15

info["name"] = "akash raj" #{'name': 'akash raj', 'age': '15', 'class': 'nineth', 'is_adulit': False}
print(info)
print(info.keys()) #dict_keys(['name', 'age', 'class', 'is_adulit']

#nested dictionary
student = {
    "name" : "rahul kumar",
    "age" : 45,
    "subject_marks" : {
        "phy" : 89,
        "math" : 88,
        "chem" : 56,
    }  
}
print(student)

print(student["subject_marks"]) #{'name': 'rahul kumar', 'age': 45, 'subject_marks': {'phy': 89, 'math': 88, 'chem': 56}}

print(student["age"]) # 45

print(student.keys()) # dict_keys(['name', 'age', 'subject_marks'])

print(student["subject_marks"]["math"]) #88

print(len(student)) #3

print(student.values()) #dict_values(['rahul kumar', 45, {'phy': 89, 'math': 88, 'chem': 56}])

print(student.items()) #dict_items([('name', 'rahul kumar'), ('age', 45), ('subject_marks', {'phy': 89, 'math': 88, 'chem': 56})])

print(student.get("name2")) #None

student.update({"city" : "Patna"})
print(student)  #{'name': 'rahul kumar', 'age': 45, 'subject_marks': {'phy': 89, 'math': 88, 'chem': 56}, 'city': 'Patna'}