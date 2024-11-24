import os

from datetime           import datetime
from dotenv             import load_dotenv
from get_project_root   import root_path
from supabase           import create_client
from typing             import Optional, List



#load env for supabase
root: str = root_path()

load_dotenv(root + '/.env.local', override=True)

supabase = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_KEY')
)



class Model_player:
    def __init__(
            self,
            id          : int,
            username    : str,
            mail        : str,
            created_at  : datetime,
            updated_at  : datetime
        ) -> None:

        self.id         = id
        self.username   = username
        self.mail       = mail
        self.created_at = created_at
        self.updated_at = updated_at



    @classmethod
    def _database_to_player(cls, response) -> Optional['Model_player']:
        #check response
        if not response.data:
            return None

        #return Player object
        results = response.data[0]

        return cls(
            id          = results['id'],
            username    = results['username'],
            mail        = results['mail'],
            created_at  = datetime.fromisoformat(results['created_at']),
            updated_at  = datetime.fromisoformat(results['updated_at'])
        )



    @classmethod
    def from_id(cls, id: int) -> Optional['Model_player']:
        response = supabase.table('player').select('*').eq('id', id).execute()

        return cls._database_to_player(response)



    @classmethod
    def from_username(cls, username: str) -> Optional['Model_player']:
        response = supabase.table('player').select('*').eq('username', username).execute()

        return cls._database_to_player(response)



    @classmethod
    def from_mail(cls, mail: str) -> Optional['Model_player']:
        response = supabase.table('player').select('*').eq('mail', mail).execute()

        return cls._database_to_player(response)



    @classmethod
    def create(cls, username: str, mail: str) -> 'Model_player':
        #set attributes
        created_at = datetime.timezone.utc.now()
        updated_at = datetime.timezone.utc.now()

        items: dict = {
            'username'      : username,
            'mail'          : mail,
            'created_at'    : created_at.isoformat(),
            'updated_at'    : updated_at.isoformat()
        }

        #insert to database and check response
        response = supabase.table('player').insert(items).execute()

        if not response.data:
            print('Error: failed to create player to database')
            return None

        #return Player object
        return cls._database_to_player(response)



    def save(self) -> None:
        #set self attributes
        self.updated_at = datetime.timezone.utc.now()

        items: dict = {
            'username'  : self.username,
            'mail'      : self.mail,
            'update_at' : self.updated_at.isoformat()
        }

        #update to database and check response
        response = supabase.table('player').update(items).eq('id', self.id).execute()

        if not response.data:
            print('Error: failed to update player to database')

        return None



    @staticmethod
    def get_players() -> List['Model_player']:
        #get all players from database and check response
        response = supabase.table('player').select('*').execute()

        #return [] when response is empty
        if not response.data:
            return []

        #create a list of Player objects
        players = []

        for results in response.data:
            players.append(Model_player(
                id          = results['id'],
                username    = results['username'],
                mail        = results['mail'],
                created_at   = datetime.fromisoformat(results['created_at']),
                updated_at   = datetime.fromisoformat(results['updated_at'])
            ))

        return players
