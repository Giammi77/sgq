from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('tipo_prova',pkey='codice',caption_field='descrizione',name_long='Tipo Prova',name_plural='Tipi Prova', lookup=True)
        self.sysFields(tbl, id=False)
        
        tbl.column('codice',size=':2', name_long='Codice')
        tbl.column('descrizione', name_long='Descrizione')

    @metadata(mandatory=True)
    def sysRecord_01(self):
        return self.newrecord(codice='01', descrizione='Certificato di restituzione aree')
    @metadata(mandatory=True)
    def sysRecord_02(self):
        return self.newrecord(codice='02', descrizione='Verbale fine lavori')
    @metadata(mandatory=True)
    def sysRecord_03(self):
        return self.newrecord(codice='03', descrizione='Comunicazione fine lavori amianto')
    @metadata(mandatory=True)
    def sysRecord_04(self):
        return self.newrecord(codice='04', descrizione='Comunicazione fine lavori FAV')
    @metadata(mandatory=True)
    def sysRecord_05(self):
        return self.newrecord(codice='05', descrizione='Formulari rifiuti')


