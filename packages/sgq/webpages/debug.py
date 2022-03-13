# -*- coding: UTF-8 -*-
# class GnrCustomWebPage(object):
from gnr.core.gnrbag import Bag

class GnrCustomWebPage(object):
    py_requires = 'th/th:TableHandler'
    css_requires=''

    def main(self,pane,**kwargs):     
        
        pane.div("Inclinometro pagina di debug:")