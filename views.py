from django.shortcuts import render
from hrmscatalog.models import Departments, JobCategories, Skills, Technologies, Employees, EmpDeputations
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    num_Employees = Employees.objects.all().count()
    num_Deputations = EmpDeputations.objects.all().count()
    
    
    num_ActiveDeputations = EmpDeputations.objects.filter(deputStatus__exact = 'A').count()
    
    num_Departments = Departments.objects.all().count()
    
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_Employees' : num_Employees,
        'num_Deputations' : num_Deputations,
        'num_ActiveDeputations' : num_ActiveDeputations,
        'num_Departments' : num_Departments,
        'num_visits' : num_visits,
    }
    return render(request, 'index.html', context = context)
    

class DepartmentsListView(LoginRequiredMixin, ListView):
    model = Departments
    paginate_by = 1
    context_object_name = 'my_department_list'
    queryset = Departments.objects.all()
    template_name = 'departments/departments_list.html'
    
class DepartmentsDetailView(DetailView):
    model = Departments
    
    def get_queryset(self):
        return Departments.objects.all()
     
class EmployeesListView(LoginRequiredMixin, ListView):
    model = Employees
    paginate_by = 1
    
    context_object_name = 'my_employee_list'
    queryset = Employees.objects.all()
    template_name = 'employees/my_arbitrary_template_name_list.html'
    
class EmployeesDetailView(DetailView):
    model = Employees
    
    def get_queryset(self):
        return Employees.objects.all()
        
class JobCategoriesListView(ListView):
    model = JobCategories
    paginate_by = 1
    
    context_object_name = 'my_jobcategories_list'
    queryset = JobCategories.objects.all()
    template_name = 'jobcategories/my_arbitrary_template_name.html'
    
class JobCategoriesDetailView(DetailView):
    model = JobCategories
    
    def get_queryset(self):
        return JobCategories.objects.all()
        
class SkillsListView(ListView):
    model = Skills
    paginate_by = 1
    
    context_object_name = "my_skills"
    queryset = Skills.objects.all()
    template_name = 'skills/my_arbitary_template_name.html'
    
class SkillsDetailView(DetailView):
    model = Skills
    
    def get_queryset(self):
        return Skills.objects.all()
        
class EmpDeputationsListView(ListView):
    model = EmpDeputations
    paginate_by = 1
    
    context_object_name = "my_EmpDeputations"
    queryset = EmpDeputations.objects.all()
    template_name = 'EmpDeputations/my_arbitrary_template_name'
    
class EmpDeputationsDetailView(DetailView):
    model = EmpDeputations
    def get_queryset(self):
        return EmpDeputations.objects.all()
        
class TechnologiesListView(ListView):
    model = Technologies
    paginate_by = 1
    
    context_object_name = 'my_Technologies'
    qureyset = Technologies.objects.all()
    template_name = 'technologies/my_arbitrary_template_name'
    
class TechnologiesDetailView(DetailView):
    model = Technologies
    
    def get_queryset(self):
        return Technologies.objects.all()
        
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from hrmscatalog.forms import EmployeesDataForm

def onlyEmployeeView(request, pk):
    employee_instance = get_object_or_404(Employees, pk = pk)
    
    if request.method == 'post' :
        form = EmployeesDataForm(request.POST)
        
        if form.is_valid() :
            employee_instance.hireDate = form.cleaned_data['CleancheckHireDate']
            employee_instance.save()
            
        return HttpResponseRedirect(reverse('all-employees'))
    else :
        proposed_hiredate = datetime.date.today()
        
        form = EmployeesDataForm(initial = {'checkHireDate' : proposed_hiredate})
        
    context = { 
        'form' : form,
        'employee_instance' : employee_instance,
    }
    return render(request, 'hrmscatalog/onlyEmployeeView.html', context)
     
    
    
