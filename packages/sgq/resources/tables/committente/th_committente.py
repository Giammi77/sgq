#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('rag_sociale')
        r.fieldcell('p_iva')
        r.fieldcell('c_fiscale')
        r.fieldcell('cognome')
        r.fieldcell('nome')
        r.fieldcell('data_nascita')
        r.fieldcell('luogo_nascita')
        r.fieldcell('pr_nascita')
        r.fieldcell('indirizzo')
        r.fieldcell('cap')
        r.fieldcell('comune')
        r.fieldcell('provincia')
        r.fieldcell('societa')
        r.fieldcell('note')
        r.fieldcell('telefono')
        r.fieldcell('email')
        r.fieldcell('pec')

    def th_order(self):
        return 'rag_sociale'

    def th_query(self):
        return dict(column='rag_sociale', op='contains', val='',runOnStart=True)



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('rag_sociale')
        fb.field('p_iva')
        fb.field('c_fiscale')
        fb.field('cognome')
        fb.field('nome')
        fb.field('data_nascita')
        fb.field('luogo_nascita')
        fb.field('pr_nascita')
        fb.field('indirizzo')
        fb.field('cap')
        fb.field('comune')
        fb.field('provincia')
        fb.field('societa')
        fb.field('note')
        fb.field('telefono')
        fb.field('email')
        fb.field('pec')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
