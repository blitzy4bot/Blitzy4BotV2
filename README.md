# Blitzy4BotV2

In order to run the bot you have to follow a few steps to make it work:

1. Setup a MySQL server on the machine you want to run the bot.
2. Create a database on your MySQL server.
3. Edit /MySQL/.env to match your database name and login.
4. Run /MySQL/setup.py only !ONCE.
5. Paste your discord bot token in the enmpty string in "config.py".
6. Make sure that you have enabled ALL intents on your discord bot (website)

Use &help to list all available commands.

There are special commands for Bot-Superusers and for the bot owner.

&deductgold -> deducts gold from a user

&addgold -> adds gold to a user

&force -> enters a user to the DB

&shutdown -> shutdown the bot entirely

&block -> blocks all commands except for "unblock" and "shutdown"

&unblock -> unblocks all blocked commands

&uptime -> shows the uptime of the bot

&addsu -> adds a new superuser to the DB

&delsu -> removes a superuser from the DB
