from django.contrib import admin
from .models import Departments, JobCategories, Skills, Technologies, Employees, EmpDeputations

# Register your models here.

class DepartmentsAdminInLineEditing(admin.TabularInline):
    model = Employees
    
#admin.site.register(Departments)
@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin) :
    list_display = ('deptID','deptName','deptLocation') 
    inlines = [DepartmentsAdminInLineEditing]
    
#admin.site.register(Departments, DepartmentsAdmin)



#admin.site.register(JobCategories)
class JobCategoriesAdmin(admin.ModelAdmin):
    list_display = ('jobCatID','jobCatName','jobCatDesc')
admin.site.register(JobCategories,JobCategoriesAdmin)


#admin.site.register(Skills)
@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skillID','skillName','sillDesc')
    
@admin.register(Technologies)
class TechnologiesAdmin(admin.ModelAdmin):
    pass
    
#admin.site.register(EmpDeputations)
@admin.register(EmpDeputations)
class EmpDeputationsAdmin(admin.ModelAdmin):
    list_display = ('deputEmpID','deputBeignDate','deputPeriod','deputEndDate','deputStatus','deputCity','deputID')
   
class EmpDeputationsAdminInLineEditing(admin.TabularInline):
    model = EmpDeputations
    

#admin.site.register(Employees)
@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('empID','empName','empJob','hireDate','empSal','empComm','empDeptID','empMgrID','empJobCatID','empSkillID','display_Technolgies')
    #fields = ['empID','empName','empJob','hireDate',('empSal','empComm'),('empDeptID',('empMgrID')),('empJobCatID','empSkillID'),'empTechnologies']
    list_filter = ('empID','hireDate','empTechnologies')
    fieldsets =(
        (None, {
            'fields' :  ('empID','empName','empJob','hireDate','empSal','empComm')
            }), 
            ('Defendencies',{
                'fields' : ('empDeptID','empMgrID',     'empJobCatID','empSkillID','empTechnologies')
                })
        )
    inlines = [EmpDeputationsAdminInLineEditing]
        
    
   
