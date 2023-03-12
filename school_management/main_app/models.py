from django.db import models

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=50)
    mark = models.IntegerField(null=True, blank=True)
    full_mark = models.IntegerField(default=100,null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=30)
    subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.TextField()
    roll = models.SmallIntegerField()
    class_name = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('class_name', 'roll',)

    def __str__(self):
        return self.name