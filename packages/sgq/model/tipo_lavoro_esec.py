from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('tipo_lavoro_esec',pkey='codice',caption_field='descrizione',name_long='Tipo Lavoro in Esecuzione',name_plural='Tipi Lavori in Esecuzione', lookup=True)
        self.sysFields(tbl, id=False)
        
        tbl.column('codice',size=':2', name_long='Codice')
        tbl.column('descrizione', name_long='Descrizione')

    @metadata(mandatory=True)
    def sysRecord_01(self):
        return self.newrecord(codice='01', descrizione='Sopralluogo preliminare')
    @metadata(mandatory=True)
    def sysRecord_02(self):
        return self.newrecord(codice='02', descrizione='Contratti di appalto')
    @metadata(mandatory=True)
    def sysRecord_03(self):
        return self.newrecord(codice='03', descrizione='Preventivo/Offerta confermato')
    @metadata(mandatory=True)
    def sysRecord_04(self):
        return self.newrecord(codice='04', descrizione='Capitolato di appalto')
    @metadata(mandatory=True)
    def sysRecord_05(self):
        return self.newrecord(codice='05', descrizione='Cronoprogramma lavori')
    @metadata(mandatory=True)
    def sysRecord_06(self):
        return self.newrecord(codice='06', descrizione='Documenti ed elaborati grafici')
    @metadata(mandatory=True)
    def sysRecord_07(self):
        return self.newrecord(codice='07', descrizione='Piano di Sicurezza e Coordinamento (PSC)')
    @metadata(mandatory=True)
    def sysRecord_08(self):
        return self.newrecord(codice='08', descrizione='Piano Operativo di Sicurezza (POS)')
    @metadata(mandatory=True)
    def sysRecord_09(self):
        return self.newrecord(codice='09', descrizione='Piano di Lavoro Amianto (PdL)')
    @metadata(mandatory=True)
    def sysRecord_10(self):
        return self.newrecord(codice='10', descrizione='Piano Montaggio Uso e Smontaggio Ponteggio (PiMUS)')
    @metadata(mandatory=True)
    def sysRecord_11(self):
        return self.newrecord(codice='11', descrizione='Analisi massive preliminari (Amianto)')
    @metadata(mandatory=True)
    def sysRecord_12(self):
        return self.newrecord(codice='12', descrizione='Analisi massive preliminari (FAV)')
    @metadata(mandatory=True)
    def sysRecord_13(self):
        return self.newrecord(codice='13', descrizione='Analisi ambientali preliminari (MOCF)')
    @metadata(mandatory=True)
    def sysRecord_14(self):
        return self.newrecord(codice='14', descrizione='Verbale prova fumi')
    @metadata(mandatory=True)
    def sysRecord_15(self):
        return self.newrecord(codice='15', descrizione='Verbale prova visiva')
    @metadata(mandatory=True)
    def sysRecord_16(self):
        return self.newrecord(codice='16', descrizione='Verbale di restituzione aree')
    @metadata(mandatory=True)
    def sysRecord_17(self):
        return self.newrecord(codice='17', descrizione='Check-List di cantiere (Mod E) ')
    @metadata(mandatory=True)
    def sysRecord_18(self):
        return self.newrecord(codice='18', descrizione='Verifica Certificazione Verde')








 

