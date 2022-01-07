# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('piano_qualita', pkey='id', name_long='Piano Qualità Commessa', name_plural='Piani Qualità commessa',caption_field='titolo_piano')
        self.sysFields(tbl)
        # tbl.column('clinete_id',size='22', group='_', name_long='Cliente'
        #             ).relation('sgq.cliente.id', relation_name='piano', mode='foreignkey', onDelete='raise')
        tbl.column('committente_id',size='22', group='_', name_long='Committente'
                    ).relation('sgq.committente.id', relation_name='piano_qualita', mode='foreignkey', onDelete='raise')
        tbl.column('ruolo_codice',size='2', group='_', name_long='Ruolo'
                    ).relation('sgq.ruolo.codice', relation_name='piano_qualita', mode='foreignkey', onDelete='raise')
        tbl.column('anagrafica_id',size='22', group='_', name_long='Società Affidataria di Riferimento'
                    ).relation('sgq.anagrafica.id', relation_name='piano_qualita', mode='foreignkey', onDelete='raise')
        tbl.column('data_inizio', dtype='D', name_long='Data Inizio Lavori', name_short='Data Inizio Lav.')
        tbl.column('data_fine', dtype='D', name_long='Data Fine Lavori', name_short='Data Fine Lav.')
        tbl.column ('tipo_fine',size='1', name_long='Tipo Fine', values='P:Presunta,E:Effettiva', validate_notnull=True)
        tbl.column('indirizzo', name_long='Indirizzo Cantiere')
        tbl.column('descrizione', name_long='Oggetto Cantiere')

        # tbl.aliasColumn('rag_sociale','@committente_id.rag_sociale', name_long='Committente')
        tbl.formulaColumn('titolo_piano',"@committente_id.rag_sociale || ' - ' || $descrizione", name_long='Titolo' )