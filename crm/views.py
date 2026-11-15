from django.shortcuts import render
from django.views.generic import View
from crm.models import Student
from django.http import JsonResponse
from json import loads
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class StudentListCreateView(View):
  def get(self,request):
    qs=Student.objects.all().values()
    response_data=list(qs)
    return JsonResponse(response_data,safe=False)

  def post(self,request):
    form_data=loads(request.body)
    Student.objects.create(
      name=form_data.get("name"),
      email=form_data.get("email"),
      course=form_data.get("course"),
      pass_out_year=form_data.get("pass_out_year"),
      college=form_data.get("college")
    )
    response_data={"message":"record inserted successfully.."}
    return JsonResponse(response_data)

@method_decorator(csrf_exempt,name="dispatch")
class StudentRetrieveUpdateDelete(View):
  def get(self,request,pk=None):
    qs=Student.objects.filter(id=pk).values()
    response_data=list(qs)
    return JsonResponse(response_data,safe=False)
  
  def put(self,request,pk=None):
    json_data=request.body
    form_data=loads(json_data)
    Student.objects.filter(id=pk).update(**form_data)
    response_data={"message":"updated"}
    return JsonResponse(response_data)
  
  def delete(self,request,pk=None):
    Student.objects.filter(id=pk).delete()
    response_data={"message":"record deleted successfully..."}
    return JsonResponse(response_data)

