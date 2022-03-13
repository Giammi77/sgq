# -*- coding: UTF-8 -*-
# class GnrCustomWebPage(object):
from gnr.core.gnrbag import Bag

class GnrCustomWebPage(object):
    py_requires = 'th/th:TableHandler'
    css_requires=''

    def main(self,root,**kwargs):     
        bc = root.borderContainer()
        bc.contentPane(region='top', height='10%').div("Inclinometro pagina di debug:")
        fb = bc.contentPane(region='center').formbuilder()
        fb.textBox(value='^gnr.page_id',lbl='page_id',edit=False)
        fb.data('valore',None,serverpath='valore', dbenv=True)
        fb.textBox(value = '^valore', width='10em', lbl='valore')
