

def create_tables(db):
    """Create database table for the likes application
    given a database connection 'db'.
    Removes any existing data that might be in the
    database."""

    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS likes")
    cursor.execute("""
    CREATE TABLE likes (
       thing text
    )
    """)

def store_like(db, like):
    """Store a new like in the database"""

    cursor = db.cursor()
    cursor.execute("INSERT INTO likes (thing) VALUES (?)", [like])
    db.commit()


def get_likes(db):
   """Return a list of likes from the database"""

   cursor = db.cursor()
   cursor.execute("SELECT thing FROM likes")
   result = []
   for row in cursor:
       result.append(row['thing'])
   return result


