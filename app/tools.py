from sqlite3 import connect


class Database:
    def __init__(self, database_path):
        self.database_path = database_path

    def execute(self, command):
        with connect(self.database_path) as database:
            cur = database.cursor()
            result = cur.execute(command).fetchall()
        return result


class Store(Database):
    def __init__(self):
        super().__init__('app/database//store.db')
        self.fields = 'title, price, license_type, is_sold, tags, badges,' +\
            'preview, bpm, tonality, genre, mood'

    def sell(self, beat_id):
        self.execute(f'UPDATE store SET is_sold = 1 WHERE id = {beat_id}')

    def get_info(self, beat_id, info_type='all'):
        if info_type == 'all':
            return self.execute(f'SELECT * from store WHERE id = {beat_id}')
        return self.execute(
            f'SELECT {info_type} from store WHERE id = {beat_id}')

    def get_all(self):
        return self.execute('SELECT * from store')

    def update(self, beat_id, title=None, price=None, license_type=None,
               is_sold=None, tags=None, badge=None, preview=None, bpm=None,
               tonality=None, genre=None, mood=None):
        if title != None:
            self.execute(
                f"UPDATE store SET title = '{title}' WHERE id = {beat_id}")
        if price != None:
            self.execute(
                f"UPDATE store SET price = {price} WHERE id = {beat_id}")
        if license_type != None:
            self.execute(
                f"UPDATE store SET license_type = '{license_type}' WHERE id = {beat_id}")
        if is_sold != None:
            self.execute(
                f"UPDATE store SET is_sold = {is_sold} WHERE id = {beat_id}")
        if tags != None:
            self.execute(
                f"UPDATE store SET tags = '{tags}' WHERE id = {beat_id}")
        if preview != None:
            self.execute(
                f"UPDATE store SET preview = '{preview}' WHERE id = {beat_id}")
        if bpm != None:
            self.execute(
                f"UPDATE store SET bpm = {bpm} WHERE id = {beat_id}")
        if tonality != None:
            self.execute(
                f"UPDATE store SET tonality = '{tonality}' WHERE tonality = {beat_id}")
        if genre != None:
            self.execute(
                f"UPDATE store SET genre = '{genre}' WHERE id = {beat_id}")
        if mood != None:
            self.execute(
                f"UPDATE store SET mood = '{mood}' WHERE id = {beat_id}")

    def add_beat(self, title, price, license_type, is_sold=0, tags='',
                 badges='', preview='', bpm='', tonality='',
                 genre='', mood=''):
        self.execute(
            f"INSERT INTO store({self.fields}) VALUES('{title}', {price},\
            '{license_type}', {is_sold}, '{tags}', '{badges}', '{preview}',\
            '{bpm}', '{tonality}', '{genre}', '{mood}');")


