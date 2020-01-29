from django.db import models
from employee.models import Bill
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(_("Name"), max_length=150)
    stock = models.IntegerField(_("Stock"))
    company = models.CharField(_("Company"), max_length=50)
    bill = models.ForeignKey(Bill, verbose_name=_("Bills"), on_delete=models.CASCADE)
    address = models.TextField(_("Address"))

    class Meta:
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Supply_detail", kwargs={"pk": self.pk})
