from django.db import models
import uuid
from django.urls import reverse

class Departments(models.Model):
    """models Representing the departments in the organizaion"""
    deptObjID = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = "unique Departments objectid for each department registered in the organization")
    deptID = models.SmallIntegerField(unique = True, blank = False, help_text = "unique Departments id for each department registered in the organization")
    deptName = models.CharField(max_length = 50, help_text = "Department Nmae For Each Department registered in the Organaization")
    deptLocation = models.CharField(max_length = 50, help_text = "Department Location For Each Department Regissteredin the Organization")
    
    def __str__(self):
        return self.deptName
        
    def get_absolute_url(self):
        return reverse('department-details',args = [int(self.deptID)])
    
class JobCategories(models.Model):
    """Models Representing the different Job categories registered in the organisaton"""
    jobCatObjID = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = "unique job category Id registered in the organization")
    jobCatID = models.SmallIntegerField(unique = True, blank = False, help_text = "unique job category Id registered in the organization")
    jobCatName = models.CharField(max_length = 100, unique = True, blank = False, help_text = "Job category name for the job registered in the organization")
    jobCatDesc = models.CharField(max_length = 500, blank = False, help_text = "job category description for category registered in the organization")
    def __str__(self):
        return self.jobCatName
    def get_absolute_url(self) :
        return reverse('jobcategories-details', args = [int(self.jobCatID)]) 
    
class Skills(models.Model):
    """models representing the skills of the employee registered in the organization"""
    skillobjID = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = "unique sill id registered in the organization")
    skillID = models.SmallIntegerField(unique = True, blank = False, help_text = "unique sill id registered in the organization")
    skillName = models.CharField(max_length = 50, unique = True, blank = False, help_text = "skill name for registered in the organization")
    sillDesc = models.CharField(max_length = 500, blank = False, help_text = "skill description registered in the organization")
    def __str__(self):
        return self.skillName
    def get_absolute_url(self) :
        return reverse('skills-details', args = [int(self.skillID)])

class Technologies(models.Model):
    technologyName = models.CharField(max_length = 50, unique = False, help_text = "technologies names that are identified by the organizations")
    def __str__(self):
        return self.technologyName
        
    def get_absolute_url(self):
        return reverse('technologies-details', args = [int(self.technologyName)])
    

    
    
    
    
class Employees(models.Model):
    """Model Representing The Employees Registered In The Organaization"""
    empObjID = models.UUIDField(primary_key =  True, default = uuid.uuid4, help_text = "Unique Employeee ID for Each employee Registered in the company")
    empID = models.SmallIntegerField(unique =  True, blank = False, help_text = "Unique Employeee ID for Each employee Registered in the company")
    empName = models.CharField(max_length = 50, help_text = "Employee Name For Each employee in the department")
    JOB_LIST = (
        ('P', 'President'),
        ('M', 'Manager'),
        ('A', 'Analyst'),
        ('s', 'Salesman'),
        ('C', 'Clerk')
    )
    empJob = models.CharField(max_length = 1, blank = False, choices = JOB_LIST, default = 's', help_text = "Employee Designation for the each employee Registered in the company")
    hireDate = models.DateField(null = False, blank = False)
    empSal = models.DecimalField(decimal_places = 2, max_digits = 8, help_text = "Employee fixed salary for the each emoloyee registered in the organisation")
    empComm = models.DecimalField(decimal_places = 2, max_digits = 8, null = True, blank = True, help_text = "Employee fixed Commission for the each employee registered in the organisation")
    empDeptID = models.ForeignKey('Departments', to_field = 'deptID', on_delete = models.CASCADE , null = False)
    empMgrID = models.ForeignKey('self', to_field = 'empID', on_delete = models.SET_NULL, null = True, blank = True, help_text = "Employees Manager ID for each employee registered in the orgaization")
    empJobCatID = models.ForeignKey('JobCategories', to_field = 'jobCatID', on_delete = models.SET_NULL, null = True, blank = True, help_text = "Employees working job category Id for each employee registered in the organization")
    empSkillID = models.ForeignKey('Skills', to_field = 'skillID', on_delete = models.SET_NULL, null = True, blank = True, help_text = "employees Area of main skill for each employee registered in the organization")
    empTechnologies = models.ManyToManyField('Technologies', help_text = "select the required tehnologies, hold ctrl key to select the multiple technologies for employee")
    
    def display_Technolgies(self):
        return ', '.join(empTechnologies.technologyName for empTechnologies in self.empTechnologies.all()[:2])
        
    display_Technolgies.short_description = 'Technologies'

    def __str__(self):
        return self.empName
        
    def get_absolute_url(self):
        return reverse('employees-details', args = [int(self.empID)])
    
class EmpDeputations(models.Model):
    """model representing the employees deputation between the organization or depatments"""
    deputobjID = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = "unique deputaion ID allocated for each deputation executed upon the employee")
    deputID = models.SmallIntegerField(unique = True, blank = False, help_text = "unique deputaion ID allocated for each deputation executed upon the employee")
    deputBeignDate = models.DateField(null = False, blank = False, help_text = "employee deputation begin date for the employeee registerred in the organization")
    deputPeriod = models.IntegerField(help_text = "employee deputaion period in months to the organization")
    deputEndDate = models.DateField(null = True, blank = True, help_text = "employee deputation end date for the employeee registerred in the organization")
    deputStatus = models.CharField(max_length = 1, help_text = "deputation status of the employee whether A : active, D : Deactive")
    deputCity = models.CharField(max_length = 100, help_text = "deputation city name of the employee where he is deputed")
    deputEmpID = models.ForeignKey('Employees', to_field = 'empID', on_delete = models.CASCADE, null = False, help_text = "employee id who is on or sent for deputation")   
    
    def __str__(self):
        return str(self.deputID)
        
    def get_absolute_url(self):
        return reverse('deputations-details',args = [int(self.deputID)])