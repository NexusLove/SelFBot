# SelFBot

Selfbot for facebook with various functionality.

Actual functionality

- Bot info
- [in-dev] GCC support
- Commands info (using docstrings)
- Automatic command list generation
- restart/eval/exec commands

Incoming features:

- cppreference and google search
- Anything what goes throught my head

Feel free to give me the ideas "what should i implement" using "issues". Or just create a feature, and make a pull request.

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