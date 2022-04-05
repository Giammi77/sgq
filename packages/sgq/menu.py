#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    main = root.branch(u"Sistema Genstione Qualità")

    main.thpage(u"!!Piano Qualita Commessa", table="sgq.piano_qualita")
    main.thpage(u"!!Registro di Pianificazione Lavoro", table="sgq.reg_pianif_lav")
    
    anag = root.branch(u"Anagrafiche")
    anag.thpage(u"!!Committente", table="sgq.committente")
    anag.thpage(u"!!Impresa", table="sgq.anagrafica")
    anag.thpage(u"!!Compilatore", table="sgq.compilatore")

    setup = root.branch(u"Impostazioni")
    setup.thpage(u"!!Ruolo", table="sgq.ruolo")
    setup.thpage(u"!!Tipo Attivita", table="sgq.tipo_attivita")
    setup.thpage(u"!!Tipo Lavoro", table="sgq.tipo_lavoro")
    setup.thpage(u"!!Tipo Lavoro esecuzione", table="sgq.tipo_lavoro_esec")
    setup.thpage(u"!!Tipo Prova e Controllo", table="sgq.tipo_prova")
    setup.thpage(u"!!Tipo Non Conformità", table="sgq.tipo_non_conformita")
    setup.thpage(u"!!Attivita Piano Qualita", table="sgq.attivita_piano_qualita")
    setup.thpage(u"!!Connessione wifi", table="sgq.connessione_wifi")
    setup.webpage(u"!!Pagina Inclinometro", filepath="/sgq/wifi")
