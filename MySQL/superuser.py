from MySQL.connection import db, maincursor


def addSuperuser(user):
    try:
        maincursor.execute("INSERT INTO superusers (userID) VALUES (%s)", (user,))
    except:
        pass

def delSuperuser(user):
    try:
        maincursor.execute(f"DELETE FROM superusers WHERE userID = {user}")
    except:
        pass

def checkSuperuser(user):
    try:
        maincursor.execute(f"SELECT EXISTS(SELECT * FROM superusers WHERE userID = {user})")
        x = maincursor.fetchone()
        return 1 in [i for i in x]
    except:
        pass
