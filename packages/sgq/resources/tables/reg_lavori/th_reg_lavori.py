#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count',name='Nr.')
        r.fieldcell('piano_qualita_id')
        r.fieldcell('tipo_lavoro_esec_codice')
        r.fieldcell('stato_doc')
        r.fieldcell('specifiche')
        r.fieldcell('note')
        r.fieldcell('collaboratore_id')
        r.fieldcell('data')


    def th_order(self):
        return '_row_count'

    def th_query(self):
        return dict(column='piano_qualita_id', op='contains', val='')

class ViewFromPianoQualita(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count',name='Nr.')
        r.fieldcell('piano_qualita_id')
        r.fieldcell('tipo_lavoro_esec_codice',edit=True,width='20em')
        r.fieldcell('stato_doc',edit=True)
        r.fieldcell('specifiche',edit=True)
        r.fieldcell('note',edit=True,width='30em')
        r.fieldcell('collaboratore_id',edit=True)
        r.fieldcell('data',edit=True)

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('piano_qualita_id')
        fb.field('tipo_lavoro_esec_codice')
        fb.field('stato_doc')
        fb.field('specifiche')
        fb.field('note')
        fb.field('collaboratore_id')
        fb.field('data')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')