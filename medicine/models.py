from django.db import models
from django.utils.translation import ugettext as _
from customer.models import Customer
# from employee.models import Bill

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    customer = models.ForeignKey(Customer, related_name="meds", verbose_name=_(""), on_delete=models.CASCADE)
    # bill = models.ForeignKey(Bill, verbose_name=_("Bill"), on_delete=models.CASCADE)
    quantity =  models.IntegerField(_("Quantity"))
    weight = models.CharField(_("Weight"), blank=True, null=True, max_length=50)
    price = models.IntegerField(_("Price"))
    mfd = models.DateField(_("Manufactured on"), auto_now=False, auto_now_add=False)
    exp = models.DateField(_("Expires on"), auto_now=False, auto_now_add=False)
    placed_at = models.CharField(_("Placed at"), max_length=40, blank=True, null=True)
    

    class Meta:
        verbose_name = _("Medicine")
        verbose_name_plural = _("Medicines")

    def __str__(self):
        return f'{self.name}'
            