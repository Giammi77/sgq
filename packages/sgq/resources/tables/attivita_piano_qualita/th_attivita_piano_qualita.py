#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('piano_qualita_id')
        r.fieldcell('tipo_attivita_codice',width='25em')

    def th_order(self):
        return 'piano_qualita_id'

    def th_query(self):
        return dict(column='piano_qualita_id', op='contains', val='')

class ViewFromPianoQualita(View):
    pass


class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('piano_qualita_id')
        fb.field('tipo_attivita_codice')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')

class FormFromPianoQualta(Form):
    pass