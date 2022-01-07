from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('ruolo',pkey='codice',caption_field='descrizione',name_long='Ruolo',name_plural='Ruoli', lookup=True)
        self.sysFields(tbl, id=False)
        
        tbl.column('codice',size='2', name_long='Codice')
        tbl.column('descrizione', name_long='Descrizione')

    @metadata(mandatory=True)
    def sysRecord_AA(self):
        return self.newrecord(codice='AA', descrizione='Affidataria')
    @metadata(mandatory=True)
    def sysRecord_AE(self):
        return self.newrecord(codice='AE', descrizione='Affidataria Esecutrice')
    @metadata(mandatory=True)
    def sysRecord_EE(self):
        return self.newrecord(codice='EE', descrizione='Esecutrice')



