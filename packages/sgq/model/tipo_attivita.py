# encoding: utf-8
from gnr.core.gnrdecorator import metadata
class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('tipo_attivita',pkey='codice',caption_field='descrizione',name_long='Tipo Attivita',name_plural='Tipi Attività',lookup=True)
        self.sysFields(tbl, id=False)
        
        tbl.column('codice',size=':2', name_long='Codice')
        tbl.column('descrizione', name_long='Descrizione')

    @metadata(mandatory=True)
    def sysRecord_01(self):
        return self.newrecord(codice='01', descrizione='Bonifica amianto friabile')
    @metadata(mandatory=True)
    def sysRecord_02(self):
        return self.newrecord(codice='02', descrizione='Bonifica amianto compatto')
    @metadata(mandatory=True)
    def sysRecord_03(self):
        return self.newrecord(codice='03', descrizione='Bonifica FAV')
    @metadata(mandatory=True)
    def sysRecord_04(self):
        return self.newrecord(codice='04', descrizione='Bonifica amianto friabile')
    @metadata(mandatory=True)
    def sysRecord_05(self):
        return self.newrecord(codice='05', descrizione='StripOut')
    @metadata(mandatory=True)
    def sysRecord_06(self):
        return self.newrecord(codice='06', descrizione='Demolizione')



