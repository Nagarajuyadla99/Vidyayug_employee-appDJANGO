from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Employees, Department
from .forms import EmployeesForm, DepartmenForm
from .decorators import employee_login_required


def home(request):
    return render(request, "home.html")


# ---------------- Employee CRUD ----------------

def employee_list(request):

    search_query = request.GET.get("search", "")
    department_filter = request.GET.get("department", "")

    employees = Employees.objects.all().order_by("id")
    if search_query:
        employees = employees.filter(name__icontains=search_query)
    if department_filter:
        employees = employees.filter(dep__id=department_filter)

    paginator = Paginator(employees, 5)
    page_number = request.GET.get("page")
    employees_page = paginator.get_page(page_number)

    departments = Department.objects.all()

    return render(request, "employee_list.html", {
        "employees": employees_page,
        "departments": departments,
        "search": search_query,
        "department_filter": department_filter,
    })


@employee_login_required
def employee_create(request):
    
    form = EmployeesForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, "add_employees.html", {"form": form})


@employee_login_required
def edit_employee(request, id):
    emp = get_object_or_404(Employees, id=id)
    if request.method == "POST":
        form = EmployeesForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully!")
            return redirect("employee_list")
    else:
        form = EmployeesForm(instance=emp)
    return render(request, "edit_employee.html", {"form": form})



def delete_employee(request, id):
    emp = get_object_or_404(Employees, id=id)
    if request.method == "POST":
        emp.delete()
        messages.success(request, "Employee deleted successfully!")
        return redirect("employee_list")
    return render(request, "delete_employee.html", {"employee": emp})


# ---------------- Department CRUD ----------------

def department_list(request):
    departments = Department.objects.all().order_by("id")
    return render(request, "department_list.html", {"departments": departments})



def department_create(request):
    if request.method == "POST":
        form = DepartmenForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Department created successfully!")
            return redirect("department_list")
    else:
        form = DepartmenForm()
    return render(request, "add_department.html", {"form": form})


# ---------------- Login / Logout ----------------
def login_view(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']

        try:
            user = Employees.objects.get(name=name, password=password)
            request.session['employee_id'] = user.id
            request.session['employee_name'] = user.name
            return redirect('employee_list')
        except Employees.DoesNotExist:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, "login.html")


def logout_view(request):
    request.session.flush()  
    return redirect("login")
