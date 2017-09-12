from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    postcode = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    companies_house_number = models.CharField(max_length=255, null=True, blank=True)
    effective_date = models.CharField(max_length=255, null=True, blank=True)
    current_status = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
