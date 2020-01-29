from django.db import models
from django.utils.translation import ugettext_lazy as _
from customer.models import Customer



# Create your models here.
class Employee(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    stock = models.IntegerField(_("Stock"))
    bill = models.ForeignKey(Bill, verbose_name=_("Bills"), on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = _("Employee")

        verbose_name_plural = _("Employees")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})



class Bill(models.Model):
    customer = models.ForeignKey(Customer, verbose_name=_("Customer"), on_delete=models.CASCADE)
    dop = models.DateTimeField(_("DOP"), auto_now=False, auto_now_add=False)


    

    class Meta:
        verbose_name = _("Bill")
        verbose_name_plural = _("Bills")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Bill_detail", kwargs={"pk": self.pk})

