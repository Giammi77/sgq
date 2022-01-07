#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        # r.fieldcell('committente_id')
        r.fieldcell('titolo_piano', width='30em')
        r.fieldcell('ruolo_codice')

        r.fieldcell('anagrafica_id', width='30em')
        r.fieldcell('data_inizio')
        r.fieldcell('data_fine')
        r.fieldcell('indirizzo')
        # r.fieldcell('descrizione')

    def th_order(self):
        return 'committente_id'

    def th_query(self):
        return dict(column='committente_id', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        
        bc = form.center.borderContainer()
        self.datiGenerali(bc.roundedGroupFrame(title='Dati Generali',
                                            region='top',
                                            splitter=True,
                                            height='180px',
                                            datapath='.record'))
        tc = bc.tabContainer(region='center')

        tc.contentPane(title='Attività Previste').inlineTableHandler(relation='@attivita_piano_qualita',
                                            datapath='.attivita',viewResource='ViewFromPianoQualita',addrow=False,
                                            picker='tipo_attivita_codice')

        tc.contentPane(title='Pianificazione Lavori').inlineTableHandler(relation='@reg_pianif_lav',
                                            datapath='.registro_pianif_lavori',viewResource='ViewFromPianoQualita',addrow=True,
                                            picker='tipo_lavoro_codice')

        tc.contentPane(title='Apprivvigionamento Materiali - Attrezzature').inlineTableHandler(relation='@reg_risorse',
                                            datapath='.registro_risorse',viewResource='ViewFromPianoQualita',addrow=False,
                                            picker='tipo_risorsa_codice')

        tc.contentPane(title='Esecuzione Lavori').inlineTableHandler(relation='@reg_lavori',
                                            datapath='.registro_esecuzione_lavori',viewResource='ViewFromPianoQualita',addrow=True,
                                            picker='tipo_lavoro_esec_codice')
                                            
        tc.contentPane(title='Prove  e Controlli Finali').inlineTableHandler(relation='@reg_prove',
                                            datapath='.registro_prove',viewResource='ViewFromPianoQualita',addrow=False,
                                            picker='tipo_prova_codice')

        tc.contentPane(title='Non Conformità').inlineTableHandler(relation='@reg_non_conformita',
                                            datapath='.registro_non_conformita',viewResource='ViewFromPianoQualita',addrow=False,
                                            picker='tipo_non_conformita_codice') 

    def datiGenerali(self,frame):
        fb = frame.div(margin_left='10px',margin_right='40px',margin_top='5px').formbuilder(cols=2, border_spacing='4px',colswidth='auto',
                                            fld_width='100%')
        fb.field('committente_id',colspan=2)
        fb.field('anagrafica_id' )
        fb.field('ruolo_codice')
        
        fb.field('data_inizio')
        fb.div()
        fb.field('data_fine')
        fb.field('tipo_fine',tag='radioButtonText')
        fb.field('indirizzo',colspan=2)
        fb.field('descrizione',colspan=2)

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')

