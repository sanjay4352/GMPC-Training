students = [
    {
    "name":"Ram",
    "age":25,
    "roll":10005012,
    "subjects":["Computer","EE","Math","Design"],
    "marks":[80.5,98.2,25,36]
},

{
    "name":"Laxman",
    "age":22,
    "roll":10005013,
    "subjects":["Computer","EE","Math","Design"],
    "marks":[25,36,98,67]
}

]
print(students[0]['name'], students[0]["roll"],"Total Marks: ", sum(students[0]["marks"]), " Percentage: ", 100*sum(students[0]["marks"])/400)
print(students[1]['name'], students[1]["roll"],"Total Marks: ", sum(students[1]["marks"]), " Percentage: ", 100*sum(students[1]["marks"])/400)

# for student in students:
    # print(student['name'], student["roll"],"Total Marks: ", sum(student["marks"]), " Percentage: ", 100*sum(student["marks"])/400)
