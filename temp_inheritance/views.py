from django.shortcuts import render

def student(request):
    students = [
        {"name": "John", "age": 30, "address": "KTM"},
        {"name": "Johny", "age": 35, "address": "BKT"},
        {"name": "Jan", "age": 31, "address": "LTP"},
        {"name": "Jen", "age": 39, "address": "PKR"},
    ]
    
    return render(request, template_name="temp_inheritance/student.html", context={"students": students})



