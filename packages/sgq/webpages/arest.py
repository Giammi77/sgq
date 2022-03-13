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
        # app_token = self.site.getPreference('subscription_token', pkg='rcweb')
        # received_token = self.request.headers.get('Authorization')

        # if app_token != received_token:
        #     raise GnrBasicAuthenticationError('Wrong Authorization Login')
        
        if self.request.method == 'GET':
            print('GET')
            # if kwargs['verify_token'] == token:
            #     return kwargs['challenge']
            # else:
            #     self.response.status_code = 403
            #     return 'Access forbidden'
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
            a = incoming_message = request.data.decode('utf-8')
            sep = a.find(';')
            val = a[:sep]
            page_id = a[sep+1:]
            
            # self.setInClientData('debug',value='pippo',page_id=page_id,fired=True)
            return page_id
        return 'return della get dal server'






# # -*- coding: UTF-8 -*-
# from gnr.core.gnrdecorator import public_method
# from datetime import datetime
# import requests
# import json
# class GnrCustomWebPage(object):
#     py_requires = 'gnrcomponents/externalcall:BaseRpc'

#     @public_method
#     def webhook(self, **kwargs):
#         fbmessenger = self.site.getService(service_type='social', service_name='facebook')
#         request = self.request._request
#         response = self.response._response
#         if request.method == 'GET':
#             if kwargs['hub.verify_token'] == fbmessenger.fb_verify_token and kwargs['hub.mode'] == 'subscribe':
#                 return kwargs['hub.challenge']
#             else: 
#                 response.status_code = 403
#                 return 'Access forbidden'
#                 #return self.site.forbidden_exception(self._environ, self.response)
#         elif request.method == 'POST':
#             incoming_message = json.loads(request.data.decode('utf-8'))
#             self.recordFromMessage(incoming_message=incoming_message)
        
#     def recordFromMessage(self, incoming_message=None):
#         for message in incoming_message['entry']:
#             sender = message['messaging'][0]['sender']['id']
#             recipient = message['messaging'][0]['recipient']['id']
#             timestamp = datetime.fromtimestamp(float(message['messaging'][0]['timestamp'])/1000.0)
#             message_text = message['messaging'][0]['message']['text']
#             message_mid = message['messaging'][0]['message']['mid']
#             new_message = self.db.table('social.messenger_chat').newrecord(sender=sender, recipient=recipient, 
#                                 message=message_text, message_mid=message_mid, timestamp=timestamp, 
#                                 message_delivered=True, messaging_type='CONTACT')

#             #If recipient already exists, add conversation_id to newrecord
#             conversation_id = self.db.table('social.messenger_chat').readColumns(columns='$conversation_id', 
#                                     where='$sender=:sender', sender=str(sender))
#             if conversation_id:
#                 new_message['conversation_id'] = conversation_id
#             else:
#                 new_conversation = self.db.table('social.messenger_conversation').newrecord(sender=sender, recipient=recipient)
#                 self.db.table('social.messenger_conversation').insert(new_conversation)
#                 new_message['conversation_id'] = new_conversation['id']
#             #Once received new message from Facebook, send an automated reply if present


#             self.db.table('social.messenger_chat').insert(new_message)
#             self.db.commit()
#             print('***NEW MESSAGE***', new_message)
#             return new_message