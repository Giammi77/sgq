# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('reg_lavori', pkey='id', name_long='Registro Lavoro', name_plural='Registro Lavori',caption_field='descrizione')
        self.sysFields(tbl,counter='piano_qualita_id')
        tbl.column('piano_qualita_id',size='22', group='_', name_long='Piano Qualità Commessa'
            ).relation('sgq.piano_qualita.id', relation_name='reg_lavori', mode='foreignkey', onDelete='cascade')
        tbl.column('tipo_lavoro_esec_codice',size=':2', group='_', name_long='Tipo Lavoro',validate_notnull=True
                    ).relation('sgq.tipo_lavoro_esec.codice', relation_name='reg_lavori', mode='foreignkey', onDelete='raise')
        tbl.column ('stato_doc',size=':2', name_long='Stato Documento', values='S:Presente,N:Non Presente,NP:Non Pertinente')#, validate_notnull=True)
        tbl.column('specifiche', name_long='Specifiche')
        tbl.column('note', name_long='Note')
        tbl.column('collaboratore_id',size='22', group='_', name_long='Compilatore'
                    ).relation('collaboratore.id', relation_name='reg_lavori', mode='foreignkey', onDelete='raise')
        tbl.column('data', dtype='D', name_long='Data')

   
        tbl.aliasColumn('descrizione','@tipo_lavoro_esec_codice.descrizione', name_long='Descrizione Lavoro', name_short='Desc.Lavoro')
