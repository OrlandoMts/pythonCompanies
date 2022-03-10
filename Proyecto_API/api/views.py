import json
import pstats
from django.views import View
from .models import Company, Employee
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class CompanyView(View):

    """
        csrf_exempt elimina el error de la verificacion del cliente
        al realizar una peticion POST 
        (En este ejemplo no use un formulario, use postman. Por eso el error)
    """

    #Este metodo se ejecuta cada vez que se hace una peticion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]
                data={
                    'message': "Success",
                    'company': company
                }
            else:
                data={'message': "Company not found :("}
        else:
            companies = list(Company.objects.values())
            if len(companies)>0:
                data={
                    'message': "Success",
                    'companies': companies
                }
            else:
                data={
                    'message': "Companies not found!"
                }
        return JsonResponse(data)
    
    def post(self, request):
        # print(request.body)
        # Convierte el JSON a un diccionario de python
        jd = json.loads(request.body)
        Company.objects.create(name=jd['name'], webSite=jd['webSite'], foundation=jd['foundation'])
        data={'message': "Success"}
        return JsonResponse(data)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.webSite = jd['webSite']
            company.foundation = jd['foundation']
            company.save()
            data={'message:' "Success, company updated :)"}
        else:
            data={'message': "Company not found. Can't update :("}
        return JsonResponse(data, safe=False)
    
    def delete(self, request, id):
        companies = list(Company.objects.filter(id=id).values())

        if len(companies) > 0:
            Company.objects.filter(id=id).delete()
            data={'message:' "Success"}            
        else: 
            data={'message': "Company not found"}
        
        return JsonResponse(data, safe=False)


class EmployeeView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    
    def get(self, request, id=0):
        
        if id>0:
            employees = list(Employee.objects.filter(id=id).values())

            if len(employees) > 0:
                employee = employees[0]
                data={
                    'message': "Success",
                    'employee': employee
                }
            else:
                data = { 'message': "Employee not found"}
        else:
            employees = list(Employee.objects.values())
            if len(employees)>0:
                data = {
                    'message': "Succes", 
                    'employees': employees
                }
            else:
                data = {'message': "Without employees"}
        
        return JsonResponse(data)

    
    def post(self, request):
        jk = json.loads(request.body)
        companies = list(Company.objects.values())
        arrayIds = []
        jkCompanyId = jk['companyId_id']

        for companie in companies:
            arrayIds.append(companie['id'])
        
        if jkCompanyId in arrayIds:
            Employee.objects.create(name=jk['name'], lastName=jk['lastName'], age=jk['age'], companyId_id=jk['companyId_id'])
            data = {'message': "Success, Employee registered."} 
        else:
            data = {'message': "Error, Companie not found."}

        return JsonResponse(data)


    def put(self, request, id):
        jk = json.loads(request.body)
        employees = list(Employee.objects.filter(id=id).values())

        if len(employees) > 0:
            employee = Employee.objects.get(id=id)
            employee.name = jk['name']
            employee.lastName = jk['lastName']
            employee.age = jk['age']
            employee.save()
            data = {
                'message': "Success. Employee updated",
                'employee': employee
            }
        else:
            data = { 'message': "Employee not found"}

        return JsonResponse(data, safe=False)    


    def delete(self, request, id):
        employee = list(Employee.objects.filter(id=id).values())

        if len(employee) > 0:
            Employee.objects.filter(id=id).delete()
            data = { 'message': "Employee deleted"}
        else:
            data = { 'message': "Employee not found"}
        
        return JsonResponse(data, safe=False)