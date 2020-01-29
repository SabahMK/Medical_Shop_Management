from django.db import models
from django.utils.translation import ugettext_lazy as _
from customer.models import Customer
from employee.models import Bill

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    customer = models.ForeignKey(Customer, related_name="meds", verbose_name=_(""), on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, verbose_name=_("Bill"), on_delete=models.CASCADE)
    quantity =  models.PositiveIntegerField(_("Qty"))
    price = models.IntegerField(_("Price"))
    mfd = models.DateField(_("MFD"), auto_now=False, auto_now_add=False)
    exp = models.DateField(_("EXP"), auto_now=False, auto_now_add=False)
    

    class Meta:
        verbose_name = _("Medicine")
        verbose_name_plural = _("Medicines")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Medicine_detail", kwargs={"pk": self.pk})
