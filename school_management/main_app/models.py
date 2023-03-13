from django.db import models

# Create your models here.

Subject_list=(
    ('bangla','Bangla'),
    ('english','English'),
    ('mathematics','Mathematics'),
    ('computer','Computer'),
)

Class_list=(
    ('one','One'),
    ('two','Two'),
    ('three','Three'),
    ('four','Four'),
    ('five','Five'),
    ('six','Six'),
    ('seven','Seven'),
    ('eight','Eight'),
    ('nine','Nine'),
    ('tem','Ten'),
)


class Subject(models.Model):
    name = models.CharField(max_length=50)
    mark = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ClassSubject(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    subject_name = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.class_name.name}-{self.subject_name.name}'


class Student(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.TextField()
    roll = models.SmallIntegerField()
    class_name = models.ForeignKey(ClassSubject, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('class_name', 'roll',)

    def __str__(self):
        return self.name