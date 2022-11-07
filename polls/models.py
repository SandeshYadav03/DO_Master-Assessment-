from django.db import models

class DO_Master(models.Model):
    do_number = models.IntegerField(default=0)
    do_type = models.CharField(max_length=100)
    permit_number = models.IntegerField(default=0)
    material = models.CharField(max_length=100)
    consigner_name = models.CharField(max_length=100)
    consignee_name = models.CharField(max_length=100)
    do_issue_date = models.DateField()
    do_validity_date = models.DateField()
    from_city = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)
    total_do_qty = models.IntegerField(default=0)
    allocate_do_qty = models.IntegerField(default=0)
    company_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    do_alias = models.CharField(max_length=100)
    adv_amt_limit = models.IntegerField(default=0)
    diesel_amt_limit = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    def __str__(self):
       return self.do_type