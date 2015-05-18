# -*- coding: utf-8 -*-

from django.db import models


class DemirBankPayment(models.Model):
    account = models.CharField(max_length=255)
    added = models.BooleanField(default=False)
    processed_payment = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    auth_code = models.CharField(max_length=12, default='')
    extra_cardbrand = models.CharField(max_length=128, default='')
    extra_trxdate = models.DateTimeField(null=True)
    err_msg = models.CharField(max_length=255, default='')
    hash = models.CharField(max_length=255, default='')
    hash_params = models.CharField(max_length=255, default='')
    hash_params_val = models.CharField(max_length=255, default='')
    host_ref_num = models.CharField(max_length=50, default='')
    masked_pan = models.CharField(max_length=50, default='')
    pa_res_syntax_ok = models.BooleanField(default=False)
    pa_res_verified = models.BooleanField(default=False)
    proc_return_code = models.CharField(max_length=2, default='')
    response = models.CharField(max_length=50, default='')
    return_oid = models.CharField(max_length=64, default='')
    trans_id = models.CharField(max_length=64, default='')
    amount = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    cavv = models.CharField(max_length=28, default='')
    client_id = models.CharField(max_length=15, default='')
    currency = models.PositiveSmallIntegerField(default=0)
    eci = models.CharField(max_length=2, default='')
    md = models.CharField(max_length=512, default='')
    rnd = models.CharField(max_length=50, default='')
    md_error_msg = models.CharField(max_length=512, default='')
    md_status = models.PositiveSmallIntegerField(default=0)
    merchant_id = models.CharField(max_length=50, default='')
    oid = models.CharField(max_length=64, default='', unique=True)
    storetype = models.CharField(max_length=255, default='')
    txstatus = models.CharField(max_length=15, default='')
    client_ip = models.GenericIPAddressField(null=True)