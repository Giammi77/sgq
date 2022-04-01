# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('reg_risorsa', pkey='id', name_long='Registro Materiale - Attrezzatura', name_plural='Registro Materiale - Attrezzatura',caption_field='descrizione')
        self.sysFields(tbl,counter='piano_qualita_id')
        tbl.column('piano_qualita_id',size='22', group='_', name_long='Piano Qualità Commessa'
            ).relation('sgq.piano_qualita.id', relation_name='reg_risorse', mode='foreignkey', onDelete='cascade')
        tbl.column('tipo_risorsa_codice',size=':2', group='_', name_long='Tipo Risorsa',validate_notnull=True
                    ).relation('sgq.tipo_risorsa.codice', relation_name='reg_risorse', mode='foreignkey', onDelete='raise')
        tbl.column ('stato_doc',size=':2', name_long='Stato Documento', values='S:Presente,N:Non Presente,NP:Non Pertinente')#, validate_notnull=True)
        tbl.column('luogo', name_long='Luogo', values='M:Magazzino,C:Cantiere')
        tbl.column('note', name_long='Note')
        tbl.column('compilatore_id',size='22', group='_', name_long='Compilatore'
                    ).relation('compilatore.id', relation_name='reg_risorse', mode='foreignkey', onDelete='raise')
        tbl.column('data', dtype='D', name_long='Data')

   
        tbl.aliasColumn('descrizione','@tipo_risorsa_codice.descrizione', name_long='Descrizione Risorsa', name_short='Desc.Risorsa')
