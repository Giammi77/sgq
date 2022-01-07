from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('tipo_non_conformita',pkey='codice',caption_field='descrizione',name_long='Tipo Non Conformità',name_plural='Tipi Non Conformità', lookup=True)
        self.sysFields(tbl, id=False)
        
        tbl.column('codice',size=':2', name_long='Codice')
        tbl.column('descrizione', name_long='Descrizione')

    @metadata(mandatory=True)
    def sysRecord_01(self):
        return self.newrecord(codice='01', descrizione='Comunicazioni interne')
    @metadata(mandatory=True)
    def sysRecord_02(self):
        return self.newrecord(codice='02', descrizione='Comunicazioni esterne')
    @metadata(mandatory=True)
    def sysRecord_03(self):
        return self.newrecord(codice='03', descrizione='Verbali CSE')
    @metadata(mandatory=True)
    def sysRecord_04(self):
        return self.newrecord(codice='04', descrizione='Verbali organi di vigilanza')
    @metadata(mandatory=True)
    def sysRecord_05(self):
        return self.newrecord(codice='05', descrizione='Audit SGS/SGQ')






 
