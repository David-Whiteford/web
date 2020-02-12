
import DBcm


config = { 
    'host': 'localhost',
    'user': 'gameuser',
    'password': 'gameuser;1934',
    'database': 'game_review',
}

def add_game(name, gamestudio, genre, releasedate):
    with DBcm.UseDatabase(config) as cursor:  
        SQL = "insert into games (name, gamestudio, genre, releasedate) values (%s, %s, %s, %s)"
        cursor.execute(SQL, (name, gamestudio, genre, releasedate))

def get_reviews():
    with DBcm.UseDatabase(config) as cursor:
        SQL = "select id, name, gamestudio, genre, releasedate from games order by id"
        cursor.execute(SQL)
        data = cursor.fetchall()
    return [(row[0], row[1], row[2], row[3], row[4]) for row in data ]

 
def add_review(numberoflikes, numberofdislikes, rank, comments):
    with DBcm.UseDatabase(config) as cursor:  
        SQL = "insert into reviews (numberoflikes, numberofdislikes, rank, comments) values (%s, %s, %s, %s)"
        cursor.execute(SQL, (name, gamestudio, genre, releasedate))