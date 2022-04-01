#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('anagrafica_id')
        r.fieldcell('cognome')
        r.fieldcell('nome')
        r.fieldcell('telefono')
        r.fieldcell('email')

    def th_order(self):
        return 'anagrafica_id'

    def th_query(self):
        return dict(column='anagrafica_id', op='contains', val='',runOnStart=True)

class ViewFromAnagrafica(View):
    pass


class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=1, border_spacing='4px')
        fb.field('anagrafica_id')
        fb.field('cognome')
        fb.field('nome')
        fb.field('telefono')
        fb.field('email')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')

class FormFromAnagrafica(Form):
    pass