# zulip-notification
### A simple Incoming webhook bot
This example of Zulip API sends a message to a specific stream. The message comes from the `stdin`
e.g. `echo 'hello' | python notify.py`
## Quick start

1. Clone this repo 
1. Create a virtual environment
1. Run `pip install -r REQUIREMENTS`
1. Copy `config.py.example` to `config.py` and edit it
Note: `ZULIP_SITE_URL` must contain the base URL of your Zulip installation e.g. `zulip.mydomain.tld`
Note: You must create an `Incoming webhook` Zulip bot. If you don't know how to do that check documentation here: https://zulipchat.com/help/add-a-bot-or-integration
1. Pipe the output of your program to zulip-notification

## License

This project is licensed under the MIT license, Copyright (c) 2019