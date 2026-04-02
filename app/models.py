from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField()
    loc=models.CharField()
    def __str__(self):
        return str(self.deptno)

class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField()
    job=models.CharField()
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    hiredate=models.DateField()
    sal=models.DecimalField(max_digits=7,decimal_places=2)
    comm=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.empno)+' '+self.ename

class Salgrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    losal=models.DecimalField(max_digits=7,decimal_places=2)
    hisal= models.DecimalField(max_digits=7,decimal_places=2)

