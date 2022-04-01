# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('connessione_wifi', pkey='id', name_long='Connessone wifi', name_plural='Connessioni wifi',caption_field='utente')
        self.sysFields(tbl)

        tbl.column('page_id', name_long='Pagina wifi')
        tbl.column('utente', name_long='Utente')