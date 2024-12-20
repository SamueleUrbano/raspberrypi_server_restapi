import configparser
from label.label import Labels

class ResourceManager:

    parser: None


    INI_FILE = 'database/util/database_query.ini'

    def __init__( self ):
        self.parser = configparser.ConfigParser()


    def get_table_query( self, table_name ):
        self.parser.read( self.INI_FILE )

        if 'TABLES' in self.parser and table_name in self.parser['TABLES']:
            return self.parser.get( 'TABLES', table_name )
        else:
            raise Exception( Labels.CORRUPTED_CONFIGURATION_FILE_EXCEPTION.value )
    
    def get_record_query( self, operation, target ):
        pass