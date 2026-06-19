from django.shortcuts import render

# Create your views here.
from app.models import*
from django.http import HttpResponse
from django.db.models import *
from django.db.models.functions import Length


def insert_dept(request):
    dpt=int(input('Enter Deptno: '))
    dn=input('Enter Dname: ')
    dl=input('Enter Loc: ')
    TDO=Dept.objects.get_or_create(deptno=dpt,dname=dn,loc=dl)     #t-->tuple
    return HttpResponse('Dept is created')
    

def insert_emp(request):
    dpt=int(input('Enter Deptno: '))
    LDO=Dept.objects.filter(deptno=dpt)

    if LDO:
        DO=LDO[0]
        eno=int(input('Enter emp no: '))
        en=input('Enter emp name: ')
        sa=int(input('Enter emp salary: '))
        jb=input('Enter Emp Job: ')
        hd=input('Enter Hiredate: ')
        
        cm=input('Enter comm: ')
        if cm:
            cm=int(cm)
        else:
            cm=None

        mgr=input('Enter Emp of Manager No: ')
        if mgr:
            LMO=Emp.objects.filter(empno=int(mgr))
            if LMO:
                MO=LMO[0]
            else:
                MO=None
        else:
            MO=None
    TEMPO=Emp.objects.get_or_create(empno=eno,ename=en,sal=sa,job=jb,hiredate=hd,comm=cm,mgr=MO,deptno=DO)
    return HttpResponse('Emp is created')
    
def display_dept(request):
        QSLDO=Dept.objects.all()
        d={'QSLDO': QSLDO}
        return render (request,'display_dept.html',d)
    
def display_emp(request):
        QSLMEO=Emp.objects.all()
        QSLMEO=Emp.objects.filter(mgr__ename='KING')
        QSLMEO=Emp.objects.order_by('-sal')
        QSLMEO=Emp.objects.filter(comm__isnull=True)
        QSLMEO=Emp.objects.filter(comm__isnull=False)
        QSLMEO=Emp.objects.filter(deptno=30)
        QSLMEO=Emp.objects.all()
        QSLMEO=Emp.objects.filter(deptno__loc='Dallas')
        QSLMEO=Emp.objects.all()
        QSLMEO=Emp.objects.select_related('mgr').all()
        d={'QSLMEO':QSLMEO}
        return render (request,'display_emp.html',d)


def emptomgr(request):
     QSLEDMO=Emp.objects.all()
     QSLEDMO=Emp.objects.select_related('deptno','mgr').all()
     QSLEDMO=Emp.objects.filter(deptno__deptno=20)
     QSLEDMO=Emp.objects.filter(mgr__ename='KING')
     QSLEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno=20) 
     QSLEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='ACCOUNTING')

     d={'QSLEDMO':QSLEDMO}
     return render(request,'emptomgr.html',d)


def empdeptmgrjoin(request):
     obj=Emp.objects.all()
     obj=Emp.objects.select_related('deptno','mgr').filter(deptno=20) 
     d={'obj':obj}
     return render(request,'empdeptmgrjoin.html',d)


def DeptToEmpjoin(request):
     ADEO=Dept.objects.prefetch_related('emp_set').all()
     ADEO=Dept.objects.prefetch_related('emp_set').filter(dname__in=('Accounting','Research'))
     ADEO=Dept.objects.prefetch_related('emp_set').filter(loc='New York')
     ADEO=Dept.objects.prefetch_related('emp_set').filter(deptno=20)
     ADEO=Dept.objects.prefetch_related(Prefetch('emp_set',queryset=Emp.objects.filter(sal__gt=4000)))
     ADEO=Dept.objects.prefetch_related(Prefetch('emp_set',queryset=Emp.objects.filter(ename='BLAKE')))
     
     d={'ADEO':ADEO}
     return render(request,'DeptToEmpjoin.html',d)


# def display_agganno(request):
#      QSLEDO=Emp.objects.all()
#      QSLEDO=Emp.objects.select_related('deptno').filter(deptno__dname='Accounting')
#      #print(Emp.objects.aggregate(Avg('sal')))
#      #print(Emp.objects.aggregate(Sum('sal')))
#      #print(Emp.objects.aggregate(Max('sal')))
#      #print(Emp.objects.aggregate(Min('sal')))
#      #print(Emp.objects.aggregate(Avg('sal'))['sal__avg'])
#      #print(Emp.objects.aggregate(avs=Avg('sal'))['avs'])
#      #avgsal=Emp.objects.aggregate(avs=Avg('sal'))['avs']
#      #QSLEDO=Emp.objects.select_related('deptno').filter(sal__lt=avgsal)
#      #QSLEDO=Emp.objects.select_related('deptno').filter(sal__gt=avgsal)

#      data=Dept.objects.values('deptno').filter(dname='Research')
#      print(data)
#      print(data[0])
#      print(data[0]['deptno'])
#      Emp.objects.filter(deptno=data[0]['deptno'])
#      QSLEDO=Emp.objects.select_related('deptno').annotate(loen=Length('ename')).filter(loen=5)
#      print(Emp.objects.values('deptno').annotate(Avg('sal')))
#      print(Emp.objects.values('deptno').annotate(Avg('sal')).filter(deptno=10))
#      d={'QSLEDO':QSLEDO}
#      return render(request,'display_agganno.html',d)







