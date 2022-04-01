# -*- coding: utf-8 -*-
from builtins import object
from gnr.core.gnrdecorator import  public_method
from gnr.core.gnrbag import Bag

"Collaborative rooms with shared Object. Please use websockets=True in siteconfig and gnrwsgiserve --tornado for testing"

class GnrCustomWebPage(object):
    py_requires = 'th/th:TableHandler'

    
    # def isDeveloper(self):
    #     return True

    def main(self,root,**kwargs):
        bc=root.borderContainer()
        fb = bc.contentPane(region='top', height='50%',datapath='wifi').formBuilder(cols=1)
        save=fb.button('Save Page Id')
        delete=fb.button('Erase Page Id')
        # fb.button('Inoltra Pec Atto', action="var invioId = GET .id;console.log(invioId); FIRE rcweb_invio.view.th_batch_run = {resource:'genera_pec',res_type:'action',invio_id:invioId};")
        # fb.sharedObject('value',shared_id='test',autoLoad=True,autoSave=True,expire=20)
        fb.div("^gnr.page_id",lbl='Page Id')
        fb.textBox(value='^value',lbl='Valore:')

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

        #self.setInClientData('value',value='pippo',page_id=pageId,fired=True)
       

    #     self.fieldsPane(bc.borderContainer(datapath='.shared.info',region='left',border_right='1px solid silver',splitter=True,width='300px'))
    #     #bc.workbenchPane('elements',region='center',datapath='.shared.drawing.elements')
        
    # def mainToolbar(self,pane,room=None,datapath=None):
    #     bar=pane.slotToolbar(slots='rooms,20,savebtn,*',datapath=datapath)
    #     bar.dataController('SET .room=room',_onStart=True,room=room or 'collaborative_test')
    #     bar.savebtn.slotButton('Save',action='genro.som.saveSharedObject(room);',room='=.room')
    #     fb=bar.rooms.formbuilder(cols=3,border_spacing='0')
    #     fb.textbox(value='^.room',lbl='Room')
    #     bar.sharedObject('main.shared',shared_id='^.room',autoLoad=True,autoSave=True,expire=20)
    #     #bar.dataController("""if (old_room){genro.som.unregisterSharedObject(old_room);};
    #     #                       genro.som.registerSharedObject('main.shared',room,{expire:20,autoSave:true,autoLoad:true});
    #     #                      SET .old_room=room;
    #     #                     """,room='^.room',old_room='=.old_room',_if='room')
                         
    # def fieldsPane(self,bc):
    #     pane=bc.contentPane(region='top')
    #     pane.div('Insert values, then reload or visit same page from another browser', padding='10px')
    #     fb = pane.div(padding='10px').formbuilder(cols=1,border_spacing='3px')
    #     fb.textbox(value='^.alfa',lbl='Alfa')
    #     fb.textbox(value='^.beta',lbl='Beta')
    #     fb.textbox(value='^.gamma',lbl='Gamma')
    #     fb.textbox(value='^.delta',lbl='Delta')
    #     fb.dataController("""
    #         var result=[alfa,beta,gamma,delta].join('<br/>');
    #         SET .result=result;
    #     """,alfa='^.alfa',
    #                        beta='^.beta',gamma='^.gamma',delta='^.delta')
    #     fb.dataController("""console.log('resulttrigger',_triggerpars)""",_fired='^.result')
    #     fb.div('^.result',lbl='result')
    #     center=bc.contentPane(region='center',moveable_constrain=True,
    #             selfsubscribe_moveable_created="console.log('moveable_created',$1);",
    #             selfsubscribe_moveable_moved="console.log('moveable_moved',$1);")
        
    #     center.simpletextarea('^.testo',width='200px',height='130px',lbl='testo',
    #                         moveable=True)


        