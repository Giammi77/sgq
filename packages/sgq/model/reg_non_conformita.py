# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('reg_non_conformita', pkey='id', name_long='Registro Non Conformità', name_plural='Registro Non Conformità',caption_field='descrizione')
        self.sysFields(tbl,counter='piano_qualita_id')
        tbl.column('piano_qualita_id',size='22', group='_', name_long='Piano Qualità Commessa'
            ).relation('sgq.piano_qualita.id', relation_name='reg_non_conformita', mode='foreignkey', onDelete='cascade')
        tbl.column('tipo_non_conformita_codice',size=':2', group='_', name_long='Tipo Non Conformità',validate_notnull=True
                    ).relation('sgq.tipo_non_conformita.codice', relation_name='reg_non_conformita', mode='foreignkey', onDelete='raise')
        tbl.column ('stato_doc',size=':2', name_long='Stato Documento', values='S:Presente,N:Non Presente,NP:Non Pertinente')#, validate_notnull=True)
        tbl.column('specifiche', name_long='Specifiche')
        tbl.column('note', name_long='Note')
        tbl.column('collaboratore_id',size='22', group='_', name_long='Compilatore'
                    ).relation('collaboratore.id', relation_name='reg_non_conformita', mode='foreignkey', onDelete='raise')
        tbl.column('data', dtype='D', name_long='Data')
   
        tbl.aliasColumn('descrizione','@tipo_non_conformita_codice.descrizione', name_long='Descrizione Non Conformità', name_short='Desc.Non Conformità')