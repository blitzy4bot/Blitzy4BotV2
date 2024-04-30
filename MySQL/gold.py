from MySQL.connection import maincursor


MAX_GOLD = 99999999


def addUserToGoldDB(user, gold):
    if gold > MAX_GOLD:
        gold = MAX_GOLD
    try:
        maincursor.execute("INSERT INTO gold (userID, ammount) VALUES (%s, %s)", (user, gold))
        return 0
    except:
        pass

def checkGoldForUser(user):
    try:
        maincursor.execute(f"SELECT ammount FROM gold WHERE userID = {user}")
        x = maincursor.fetchone()
        for i in x:
            return i
    except:
        return False

def addGoldToUser(user, ammount):
    if checkGoldForUser(user) == False:
        return 1
    if int(checkGoldForUser(user)) + ammount > MAX_GOLD:
        return 2
    try:
        maincursor.execute(f"UPDATE gold SET ammount = ammount + {ammount} WHERE userID = {user}")
        return 0
    except:
        pass

def deductGoldFromUser(user, ammount):
    if checkGoldForUser(user) == False:
        return 1
    if int(checkGoldForUser(user)) - ammount < 0:
        return 2
    try:
        maincursor.execute(f"UPDATE gold SET ammount = ammount - {ammount} WHERE userID = {user}")
        return 0
    except:
        pass

def getGlobalLeaderboard(limit):
    try:
        maincursor.execute(f"SELECT * FROM gold ORDER BY ammount DESC LIMIT {limit}")
        x = maincursor.fetchall()
        return [i for i in x]
    except:
        return []
