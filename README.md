# SelFBot

Selfbot for facebook with various functionality.

Actual functionality

- Bot info
- [in-dev] GCC support

To run it, you have to create ``login.json`` file in ``db`` directory, with this structure:

```json
{
    "email": "facebook_email",
    "pwd": "facebook_password",
    "owner": "bot_owner_id",
    "prefix": "bot_prefix"
}
```

Call the bot using prefix - if your prefix is ``!``, you can call ``info`` function like that: ``!info``
Right now, the functionality is restricted for owner. I'll put an option to switch this behaviour in future.