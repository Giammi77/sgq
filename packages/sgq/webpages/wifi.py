# -*- coding: utf-8 -*-
from builtins import object
from gnr.core.gnrdecorator import websocket_method, public_method
from gnr.core.gnrbag import Bag

"Collaborative rooms with shared Object. Please use websockets=True in siteconfig and gnrwsgiserve --tornado for testing"

class GnrCustomWebPage(object):
    
    py_requires='gnrcomponents/workbench/workbench:WorkbenchManager,th/th:TableHandler'
    
    def isDeveloper(self):
        return True

    def main(self,root,**kwargs):
        bc=root.borderContainer()
        fb = bc.contentPane(region='top', height='50%',datapath='wifi').formBuilder(cols=1)
        save=fb.button('Save Page Id')
        delete=fb.button('Erase Page Id')
        fb.sharedObject('value',shared_id='test',autoLoad=True,autoSave=True,expire=20)
        fb.div("^gnr.page_id",lbl='Page Id')
        # fb.textBox(value='value',lbl='Valore:')


        save.dataRpc('result',
                        self.savePageId,
                        pageId = "^gnr.page_id",
                        _onResult='genro.publish("floating_message", {message:"Page Id salvato", messageType:"message"});'
                    )
        delete.dataRpc('result',
                        self.deletePageId,
                        pageId = "=gnr.page_id",
                        _onResult='genro.publish("floating_message", {message:"Page Id eliminato", messageType:"message"});'
                    )
        bc.contentPane(region='center').plainTableHandler(table='sgq.connessione_wifi',
                                            datapath='elenco_connessioni',condition_onStart=True
                                            )

    @public_method                  
    def savePageId(self,pageId=None):
        tblConnessioneWifi = self.db.table('sgq.connessione_wifi')
        tblConnessioneWifi.deleteSelection(where="$utente='esp01'")
        record=tblConnessioneWifi.newrecord()
        record['page_id'] = pageId
        record['utente'] ='esp01'
        tblConnessioneWifi.insert(record)
        self.db.commit()

    @public_method                  
    def deletePageId(self,pageId=None):
        tblConnessioneWifi = self.db.table('sgq.connessione_wifi')
        tblConnessioneWifi.deleteSelection(where="$utente='esp01'")
        self.db.commit()

