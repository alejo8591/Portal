#!/usr/bin/env python
from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def helloWorld(request):
    return simplejson.dumps({'message':'Hola trollface'});