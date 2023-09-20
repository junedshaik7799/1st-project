from django.contrib import admin
from django.urls import path
from app1.api.views.views2 import EmployeeDetails, EmployeeList
from app1.api.views1 import employee_details,employee_list
from app1.api.views3 import Employee_List
from app1.api.views4 import CompanyList,CompanyDetails
from app1.api.views5 import Company_list
from app1.api.artehmaticviews import Arthematiclist
from app1.api.newarthematicsviews import Arthematics_list


urlpatterns = [
    #path ('',home),
    path('employee/',employee_list), 
    path('employee/details/<str:pk>',employee_details),
    path('EmployeeList/',EmployeeList.as_view(),name="EmployeeList"),
    path('EmployeeDetails/<int:pk>/',EmployeeDetails.as_view(),name="EmployeeDetails"),
    path('Employee_List/',Employee_List.as_view(),name="Employee_List"),
    path('Employee_List/<int:id>/',Employee_List.as_view(),name="Employee_List"),
    path('CompanyList/',CompanyList.as_view(),name="CompanyList"),
    path('CompanyDetails/<int:pk>/',CompanyDetails.as_view(),name="CompanyDetails"),
    path('Company_list/',Company_list.as_view(),name="Company_list"),
    path('Company_list/<int:id>/',Company_list.as_view(),name="Company_list"),
    path('Arthematiclist/',Arthematiclist.as_view(),name="Arthematiclist"),
    path('Arthematics_list/',Arthematics_list.as_view(),name="Arthematics_list"),
    # path('Arthematics_list/<int:id>/',Arthematics_list.as_view(),name="Arthematic_list")
]