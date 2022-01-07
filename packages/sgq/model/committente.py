# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('committente', pkey='id', name_long='Committente', name_plural='Committente',
                            row_caption='cognome_nome', caption_field='rag_sociale')#,
                            # partition_cliente_id='cliente_id')
        self.sysFields(tbl)

        # tbl.column('cliente_id', size='22', name_long='Cliente'
        #                 ).relation('rcweb.cliente.id', relation_name='anagrafica', mode='foreignkey', onDelete='raise')
        tbl.column('rag_sociale', name_long='Ragione Sociale', name_short='Rag.Soc.')
        tbl.column('p_iva', size='11', name_long='Partita Iva', name_short='P.Iva')
        tbl.column('c_fiscale',name_long='Codice Fiscale')
        tbl.column('cognome',name_long='cognome')
        tbl.column('nome',name_long='nome')
        tbl.column('data_nascita',dtype='D',name_long='datanascita')
        tbl.column('luogo_nascita',name_long='luogonascita')
        tbl.column('pr_nascita',name_long='prnascita')
        tbl.column('indirizzo',name_long='indirizzo')
        tbl.column('cap',size='5',name_long='cap')
        tbl.column('comune',name_long='comune')
        tbl.column('provincia', size='2', name_long='pr').relation('glbl.provincia.sigla')
        tbl.column('societa',dtype='B',name_long='societa')
        tbl.column('note',name_long='note')
        tbl.column('telefono',name_long='telefono')
        tbl.column('email',name_long='email')
        tbl.column('pec',name_long='pec')

