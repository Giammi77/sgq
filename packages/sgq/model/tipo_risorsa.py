from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('tipo_risorsa',pkey='codice',caption_field='descrizione',name_long='Tipo Risorsa',name_plural='Tipi Risorse', lookup=True)
        self.sysFields(tbl, id=False)
        
        tbl.column('codice',size=':2', name_long='Codice')
        tbl.column('descrizione', name_long='Descrizione')

    @metadata(mandatory=True)
    def sysRecord_01(self):
        return self.newrecord(codice='01', descrizione='Certificazione prodotto/attrezzatura')
    @metadata(mandatory=True)
    def sysRecord_02(self):
        return self.newrecord(codice='02', descrizione='Libretti di uso manutenzione')
    @metadata(mandatory=True)
    def sysRecord_03(self):
        return self.newrecord(codice='03', descrizione='Verifiche periodiche')
    @metadata(mandatory=True)
    def sysRecord_04(self):
        return self.newrecord(codice='04', descrizione='Schede di sicurezza (MSDS)')

