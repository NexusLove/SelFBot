# SelFBot

Selfbot with various functionality

**Bot is in alpha status, so it lacks functionality for now.**

Functions, for now:
- Bot/system basic info
- [in-dev] GCC C/C++ compilation support
- Command info (docstrings)
- Basic Python commands - eval and exec, with all math package stuff
- Restarting

Next features to be implemented:
- Google Search support
- cppreference.com search support
- Permission system, to allow multi-user usage on fbchat

Feel free to contribute, either using pull requests or sending ideas or bugs using *Issues*

## Usage

First, create ``db`` directory next to ``__main__.py``. Put ``login.json`` file there, with this content:
```json
{
    "prefix": "bot_prefix",

    "email": "facebook_email",
    "pwd": "facebook_password",
    "owner": "bot_owner_id"
}
```

*Note: the Facebook stuff will be moved to separate object soon*

And then, run the bot in one of the modes:
- ``local`` mode will run the bot in command prompt. **Warning**: restarting bot there may break the command line (happens in PowerShell)
- ``fbchat`` mode will run bot as Facebook user, using chat as interface. For now, functionality is restricted to user with ID from ``owner`` key. You have to use ``prefix`` in order to execute a command.