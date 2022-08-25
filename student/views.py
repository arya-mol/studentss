from django.shortcuts import render, redirect
from .forms import StudentForm
import openpyxl
from .models import *
from django.contrib import messages

# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']

            if not file.name.endswith('.xlsx'):
                messages.error(request, 'Please upload an excel file')
                return redirect('home')

            wb = openpyxl.load_workbook(file)
            worksheet = wb.active

            objects = list()
            for row in worksheet.iter_rows(min_row=2):
                row_data = list()
                for cell in row:
                    row_data.append(str(cell.value))
                if not Student.objects.filter(id=row_data[0]).exists():
                    grade = Grade.objects.filter(code=row_data[4]).values('id')
                    obj = Student(id=row_data[0], name=row_data[1], address=row_data[2], email=row_data[3], grade_id=grade)
                    objects.append(obj)

            Student.objects.bulk_create(objects)

            obj_list = list(Student.objects.all().values('id', 'name', 'address', 'email', 'grade__code'))
            return render(request, 'index.html', {'obj_list': obj_list})

    else:
        form = StudentForm()
    return render(request, 'home.html', {'form': form})