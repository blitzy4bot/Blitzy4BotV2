from MySQL.connection import db, maincursor


def createTables():
    maincursor.execute("CREATE TABLE moderation (serverID bigint, userID bigint)")
    maincursor.execute("CREATE TABLE gold (userID bigint PRIMARY KEY, ammount bigint)")
    maincursor.execute("CREATE TABLE superusers (userID bigint PRIMARY KEY)")
    db.commit()


# Run this only ONCE after creating a Database