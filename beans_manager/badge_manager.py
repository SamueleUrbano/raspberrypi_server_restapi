from beans.badge import Badge
from database.database import Database
from database.util.resource_manager import ResourceManager

class BadgeManager:
    
    database        : Database
    resource_manager: ResourceManager

    TABLE = 'BADGE'

    def __init__( self ):

        self.database         = Database()
        self.resource_manager = ResourceManager()

        self.database.cursor.row_factory = lambda cursor, row: Badge( *row )

    
    def select_all_badges( self ):
        result: list['Badge'] = self.database.cursor.execute( self.resource_manager.get_record_query( table = self.TABLE, statement = 'SELECT_ALL' ) ).fetchall()
        
        return result
    
    def select_all_active_badges ( self ):
        result: list['Badge'] = self.database.cursor.execute( self.resource_manager.get_record_query( table = self.TABLE, statement = 'SELECT_ALL_ACTIVE' ) ).fetchall()

        return result