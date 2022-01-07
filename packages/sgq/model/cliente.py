def config_db(self, pkg):
        tbl = pkg.table('cliente', pkey='id', name_plural='Clienti',
                        name_long='Cliente', rowcaption='$ragione_sociale', caption_field='ragione_sociale')
        self.sysFields(tbl)
        tbl.column('ragione_sociale', name_long='Ragione sociale', indexed=True, group='001', unaccent=True)
        tbl.column('cognome', name_long='Cognome', validate_case='t', group='002')
        tbl.column('nome', name_long='Nome', validate_case='t', group='003')
        tbl.column('indirizzo_esteso', name_long='Indirizzo esteso', group='*')
        tbl.column('geocoords', name_long='Geocoder coords', group='_')
        tbl.column('societa', 'B', name_long='Società',  group='004')

        tbl.column('indirizzo', name_long='Indirizzo',
                   validate_regex='![?]{2,2}', validate_regex_error='Civico invalido', group='b_indirizzi.01')
        tbl.column('numero_civico', name_long='Numero Civico', group='*')
        tbl.column('cap', name_long='Cap', indexed=True, group='b_indirizzi.02')

        tbl.column('localita', name_long='Località', indexed=True, group='b_indirizzi.03')
        tbl.column('provincia', size='2', name_long='Provincia',
                   name_short='Prov.', indexed=True,
                   group='b_indirizzi.04').relation('glbl.provincia.sigla',
                                                    mode='foreignkey', one_group='b_indirizzi.04', many_group='_')
        tbl.column('comune_id', size='22', name_long='Comune', group='_').relation(
            'glbl.comune.id', mode='foreignkey', relation_name='anagrafiche', one_group='b_indirizzi.05')

        tbl.column('nazione', size='2', name_long='Nazione', group='b_indirizzi.06').relation(
            'glbl.nazione.code', mode='foreignkey', one_group='_', many_group='_')
        
        tbl.column('indirizzo_domicilio', name_long=' Domicilio', group='b_indirizzi.07')
        tbl.column('titolo', size=':30', name_long='Titolo', group='*')
        tbl.column('denominazione_cortesia', name_long='Denominazione cortesia', group='*')
        tbl.column('codice_fiscale', size=':16', name_long='Codice fiscale', indexed=True, group='c_datifiscali.01')
        tbl.column('partita_iva', size=':20', name_long='Partita Iva', indexed=True, group='c_datifiscali.02')
        tbl.column('rea', name_long='REA', group='c_datifiscali.03')
        tbl.column('rea_provincia', size='2', name_long='Provincia REA', name_short='Pr. REA', indexed=True, group='b_indirizzi.07'
                   ).relation('glbl.provincia.sigla',mode='foreignkey', one_group='_', many_group='_')
        tbl.column('data_nascita', 'D', name_long='Data di nascita', group='c_datifiscali.04')
        tbl.column('luogo_nascita', name_long='Luogo di nascita', group='c_datifiscali.05')
        tbl.column('provincia_nascita', size='2', name_long='Provincia di nascita', group='c_datifiscali.06'
                   ).relation('glbl.provincia.sigla',mode='foreignkey', one_group='_', many_group='_')
        tbl.column('nazione_nascita', size='2', name_long='Nazione Nascita', group='c_datifiscali.07'
                   ).relation('glbl.nazione.code', mode='foreignkey', one_group='_', many_group='_')
        tbl.column('cittadinanza', size='2', name_long='Nazione Cittadinanza', group='c_datifiscali.08'
                   ).relation('glbl.nazione.code', mode='foreignkey', one_group='_', many_group='_')

        tbl.column('sesso', size=':2', name_long='Sesso', group='c_datifiscali.07')
        tbl.column('note', name_long='Note', group='*')
        tbl.column('telefono', name_long='Telefono', group='d_comunicazioni.001')
        fpars = dict(format_bag_cells='mv_main,mv_label,mv_value,mv_note',
                     format_bag_mv_main='<div class="tick_icon10"></div>,')
        tbl.column('telefono_mv', dtype='X', name_long='Lista Telefoni', group='d_comunicazioni.002',
                   format_bag_mv_value='phone', **fpars)
        tbl.column('cellulare', name_long='Cellulare', group='d_comunicazioni.003')
        tbl.column('cellulare_mv', dtype='X', name_long='Lista Cellulari',
                   format_bag_mv_value='phone',
                   group='d_comunicazioni.004', **fpars)
        tbl.column('fax', name_long='Fax', group='d_comunicazioni.005')
        tbl.column('fax_mv', dtype='X', name_long='Lista Fax', group='d_comunicazioni.006', **fpars)
        tbl.column('chat', name_long='Chat', group='d_comunicazioni.007')
        tbl.column('chat_mv', dtype='X', name_long='Lista Chat', group='d_comunicazioni.008', **fpars)
        tbl.column('voip', name_long='Voip', group='d_comunicazioni.009')
        tbl.column('voip_mv', dtype='X', name_long='Lista Voip', group='d_comunicazioni.010', **fpars)

        tbl.column('codice_telefono', size=':8', name_long='Codice Tel', group='d_comunicazioni.011')
        tbl.column('email', name_long='Email principale', group='d_comunicazioni.012')
        tbl.column('email_mv', dtype='X', name_long='Lista Email',
                   format_bag_mv_value='mailto', group='d_comunicazioni.013', **fpars)

        tbl.column('pec', name_long='Pec', group='d_comunicazioni.014')

        tbl.column('www', name_long='Internet', group='d_comunicazioni.015')

        tbl.column('classificazione', name_long='Classificazione', group='a_04')
        tbl.column('settore', name_long='Settore', group='c_datifiscali.10')

        tbl.column('tipo', size=':12', name_long='Tipo', group='c_datifiscali.09')
        tbl.column('old_id', size=':10', name_long='Codice legacy', group='*')
        tbl.column('errori', name_long='!!Errori', group='y_vari.01')
        tbl.column('fuso_orario', name_long='Fuso orario')

        tbl.formulaColumn(
            'indirizzo_completo', "$ragione_sociale||' - '||COALESCE($indirizzo,'')||' - '||COALESCE($cap,'')||' '||COALESCE($localita,'')||' '||COALESCE($provincia,'')", group='*')
        tbl.formulaColumn(
            'cap_loc_pr', "coalesce($cap,'')||' '||coalesce($localita,'')||' '||coalesce($provincia,'')", group='*')
        tbl.formulaColumn('cognome_nome', "$cognome||' '||$nome", group='*')
        tbl.formulaColumn('rea_completa', "$rea_provincia||' '||$rea", group='*', name_long='REA')

        tbl.formulaColumn('codice_fiscale_pers', """$codice_fiscale  ~ '[A-Z,a-z]{6}' """, dtype='B', group='y_vari.02')

        tbl.aliasColumn('codice_cat','@comune_id.@localita.codice_comune', name_long='Codice Catastale')


        def partitionioning_pkeys(self):
            pass
        #     if self.db.currentEnv['cliente_id'] is None:
        #         where=None
        #     else:
        #         where='@external_users.cliente_id=:env_cliente_id'
        #     return [r['pkey'] for r in self.query(where=where).fetch()]

        # def defaultValues(self):
        #     return dict(nazione='IT')
