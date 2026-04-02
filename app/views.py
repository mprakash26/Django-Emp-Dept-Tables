from django.shortcuts import render

# Create your views here.
from app.models import*
from django.http import HttpResponse

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
     d={'QSLEDMO':QSLEDMO}
     return render(request,'emptomgr.html',d)

    