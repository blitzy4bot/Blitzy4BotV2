from MySQL.connection import maincursor


def addModeration(server, user):
    try:
        maincursor.execute("INSERT INTO moderation (serverID, userID) VALUES (%s,%s)", (server, user))
    except:
        pass

def removeModeration(server, user):
    try:
        maincursor.execute(f"DELETE FROM moderation WHERE (serverID = {server} AND userID = {user})")
    except:
        pass

def checkModeration(server, user):
    try:
        maincursor.execute(f"SELECT EXISTS(SELECT * FROM moderation WHERE (serverID = {server} AND userID = {user}))")
        x = maincursor.fetchone()
        return 1 in [i for i in x]
    except:
        pass

def getAllModerations(server):
    try:
        maincursor.execute(f"SELECT userID FROM moderation WHERE serverID = {server}")
        x = maincursor.fetchall()
        return [i for i in x]
    except:
        pass
