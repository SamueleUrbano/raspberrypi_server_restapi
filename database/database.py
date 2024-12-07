import sqlite3

from database.util.resource_manager import ResourceManager

class Database:

    connection: None
    cursor    : None

    resource_manager: ResourceManager


    DATABASE = 'database/database.db'
    TABLES   = [
        'access',
        'door',
        'badge',
        'user',

        'log_access',
        'log_user'
    ]

    def __init__( self ):
        self.connection = sqlite3.connect( self.DATABASE )
        self.cursor     = self.connection.cursor()

        self.resource_manager = ResourceManager()

        self.init_database()

    
    def init_database( self ):

        for table in self.TABLES:

            try:
                print( f'@Debug: Creating "{ table }" table...' )

                self.cursor.execute( self.resource_manager.get_create_table_query( table_name = table ) )
                self.connection.commit()

            except Exception as exception:
                print( f'@Debug: exception = {exception}' )

    