# -*- coding: UTF-8 -*-
from gnr.core.gnrdecorator import public_method
from gnr.web.gnrwebpage import GnrBasicAuthenticationError
from datetime import datetime
import requests
import json


class GnrCustomWebPage(object):
    py_requires = 'gnrcomponents/externalcall:BaseRpc'

    @public_method
    def arest(self, **kwargs):
        
        request = self.request._request
        response = self.response._response

        if self.request.method == 'GET':
            tblConnessioneWifi = self.db.table('sgq.connessione_wifi')
            sensore = kwargs.get('sensore')
            if sensore:
                page_id=tblConnessioneWifi.readColumns(columns='$page_id',
                                    where='utente=:sensore',
                                    sensore=sensore,
                                    limit=1,
                                    ignoreMissing=True)
            else:
                return
            if page_id:
                return page_id
            return 
            
            
        elif request.method == 'POST':
            print('POST')
            incoming_message = json.loads(request.data.decode('utf-8'))
            # self.recordFromMessage(incoming_message=incoming_message)
        print(incoming_message)
    
    @public_method
    def inclinometro(self, valore=None,**kwargs):
        request = self.request._request
        response = self.response._response
        if request.method == 'POST':
            a = incoming_message = str(request.data.decode('utf-8'))
            sep = a.find(';')
            esp = a[]
            val = a[:sep]
            page_id = a[sep+1:]
            
            self.setInClientData('value',value=val,page_id=page_id,fired=True)
            return a
        return 'return della get dal server'



