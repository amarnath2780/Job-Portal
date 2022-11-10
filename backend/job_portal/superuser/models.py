from django.db import models


class CompanyCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class CompanyDepartment(models.Model):
    category = models.ForeignKey(CompanyCategory, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=200)

    def __str__(self):
        return self.department_name


class Skill(models.Model):
    department = models.ForeignKey(CompanyDepartment, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=200)

    def __str__(self):
        return self.skill_name

