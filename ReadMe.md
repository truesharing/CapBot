# CapBot
A discord bot that tracks who has capped at the clan citadel in my RS3 clan.

## Commands
`/cap-list [days]` - which will show the users who have capped in the last [days] days (defaults to 7).

![Screenshot of the /cap-list command](/images/caplist.png)

`/user-status [rsn]` - shows more detailed info about a user such as their last alog entry date, when they last capped, if their alog is private and when the bot last checked their alog. 

![Screenshot of the user-status command](/images/user-status.png)

If no rsn is provided it will dump the full clan as a large table.
![Screenshot of the full user-status command](/images/full-user-status.png)

`/list-private-alogs` - Lists all users who have their alog set to private.

![Screenshot of the list-private-alogs](/images/private-a-log.png)
