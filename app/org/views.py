from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def stub(Request):
    resp = HttpResponse('Not implemented yet')
    resp.status_code = 200
    return resp