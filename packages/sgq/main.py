#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='sgq package',sqlschema='sgq',sqlprefix=True,
                    name_short='Sgq', name_long='Sistema Gestione Qualità', name_full='Sgq')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
