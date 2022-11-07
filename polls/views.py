from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect,render
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator

from . models import DO_Master

# Retrieve data
def Main_View(request):
    if 'q' in request.GET:
        q=request.GET['q']
        data=DO_Master.objects.filter(Q(do_number__icontains=q)|Q(do_type__icontains=q)|Q(permit_number__icontains=q)|Q(material__icontains=q)|Q(consigner_name__icontains=q)|Q(consignee_name__icontains=q)|Q(do_issue_date__icontains=q)|Q(do_validity_date__icontains=q)|Q(from_city__icontains=q)|Q(to_city__icontains=q)|Q(total_do_qty__icontains=q)|Q(allocate_do_qty__icontains=q)|Q(company_name__icontains=q)|Q(branch_name__icontains=q)|Q(source__icontains=q)|Q(destination__icontains=q)|Q(do_alias__icontains=q)|Q(adv_amt_limit__icontains=q)|Q(diesel_amt_limit__icontains=q))
    else:
        data = DO_Master.objects.all()
        paginator = Paginator(data,2)
        page = request.GET.get('page')
        data = paginator.get_page(page)
        result = data.paginator.num_pages

    return render(request,'Main.html',{'data':data})


#Insert Data
def Add_DO(request):
    if request.method == 'POST':
        do_number = request.POST['do_number']
        do_type = request.POST['do_type']
        permit_number = request.POST['permit_number']
        material = request.POST['material']
        consigner_name = request.POST['consigner_name']
        consignee_name = request.POST['consignee_name']
        do_issue_date = request.POST['do_issue_date']
        do_validity_date = request.POST['do_validity_date']
        from_city = request.POST['from_city']
        to_city = request.POST['to_city']
        total_do_qty = request.POST['total_do_qty']
        allocate_do_qty = request.POST['allocate_do_qty']
        company_name = request.POST['company_name']
        branch_name = request.POST['branch_name']
        source = request.POST['source']
        destination = request.POST['destination']
        do_alias = request.POST['do_alias']
        adv_amt_limit = request.POST['adv_amt_limit']
        diesel_amt_limit = request.POST['diesel_amt_limit']
        new_emp= DO_Master(do_number=do_number,do_type=do_type,permit_number=permit_number,material=material,consigner_name=consigner_name,consignee_name=consignee_name,do_issue_date=do_issue_date,do_validity_date=do_validity_date,from_city=from_city,to_city=to_city,total_do_qty=total_do_qty,allocate_do_qty=allocate_do_qty,company_name=company_name,branch_name=branch_name,source=source,destination=destination,do_alias=do_alias,adv_amt_limit=adv_amt_limit,diesel_amt_limit=diesel_amt_limit)
        new_emp.save()
        return HttpResponseRedirect(reverse('Main_View'))
    if request.method =='GET':
        return render(request,'Add_DO.html')
    return HttpResponse('An exception occured ! Employee')

# Update
def Update(request,id):
    data = DO_Master.objects.get(id=id)
    data= status=not(data.status)
    data.save()
    return HttpResponseRedirect(reverse('Main_View'))