import sqlite3

from database.util.resource_manager import ResourceManager

class Database:

    connection: None
    cursor    : None

    resource_manager: ResourceManager


    DATABASE = 'database/database.db'
    TABLES   = [
        'person',
        'badge'
    ]

    def __init__( self ):
        self.connection = sqlite3.connect( self.DATABASE )
        self.cursor     = self.connection.cursor()

        self.resource_manager = ResourceManager()

        self.init_database()

    
    def init_database( self ):
        query = 'SELECT name FROM sqlite_master WHERE type = "table"'

        result = self.cursor.execute( query ).fetchall()
        print( '@Debug: result = ' + str( result ) )

        if not result:
            for table in self.TABLES:
                
                if table == 'person':
                    print( f'@Debug: Creating "{ table }" table executing query = { self.resource_manager.get_table_query( table_name=table ) }' )
                    ## self.cursor.execute( self.resource_manager.get_table_query( table_name=table ) )

                elif table == 'badge':
                    print( f'@Debug: Creating "{ table }" table...' )
