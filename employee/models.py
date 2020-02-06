from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.



    
class Employee(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    phone_no = models.CharField(_("Phone"), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = _("Employee")

        verbose_name_plural = _("Employees")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})

