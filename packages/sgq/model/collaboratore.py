# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('collaboratore', pkey='id', name_long='Collaboratore', name_plural='Colaboratori',caption_field='nominativo')
        self.sysFields(tbl)

        tbl.column('anagrafica_id',size='22', group='_', name_long='Impresa'
                    ).relation('sgq.anagrafica.id', relation_name='collaboratore', mode='foreignkey', onDelete='cascade')
        tbl.column('cognome', name_long='Cognome')
        tbl.column('nome', name_long='Nome')
        tbl.column('telefono',name_long='Telefono')
        tbl.column('email',name_long='Email')

        tbl.formulaColumn('nominativo',"$cognome || ' ' || $nome", name_long='Nominativo')
