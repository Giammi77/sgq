# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('attivita_piano_qualita', pkey='id', name_long='Attività Piano Qualità', name_plural='Attività Piano qualità',caption_field='descrizione')
        self.sysFields(tbl)
        tbl.column('piano_qualita_id',size='22', group='_', name_long=''
                    ).relation('sgq.piano_qualita.id', relation_name='attivita_piano_qualita', mode='foreignkey', onDelete='cascade')
        tbl.column('tipo_attivita_codice',size=':2', group='_', name_long='Attività'
                    ).relation('sgq.tipo_attivita.codice', relation_name='attivita_piano_qualita', mode='foreignkey', onDelete='raise')
        tbl.aliasColumn('descrizione','@tipo_attivita_codice.descrizione', name_long='Descrizione Attività', name_short='Desc.Attività')
