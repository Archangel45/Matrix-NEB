N E Bot
=======

This is a generic client bot for Matrix which supports plugins.

This is the Python 3 version that is enhanced with the latest Matrix specification (r0.3.0)

*NOTE*: Transitioning from Python 2 to 3 isn't yet done so you should still follow the setup below. By then, I will try my best to update the bot with the updated setup.

Setup
=====
Dependencies:
* python2.7
* matrix_client
* flask
* python-dateutil

Run:

    python neb.py -c <config location>

If the config file cannot be found, you will be asked to enter in the home server URL,
user ID and access token which will then be stored at this location.

Create a room and invite NEB to it, and then type ``!help`` for a list of valid commands.


Plugins
=======

Github
------
 - Processes webhook requests and send messages to interested rooms.
 - Supports secret token HMAC authentication.
 - Supported events: ``push``, ``create``, ``ping``, ``pull_request``
 
Jenkins
-------
 - Sends build failure messages to interested rooms.
 - Support via the Notification plugin.
 - Supports shared secret authentication.

JIRA
----
 - Processes webhook requests and sends messages to interested rooms.
 - Resolves JIRA issue IDs into one-line summaries as they are mentioned by other people.

Guess Number
------------
 - Basic guess-the-number game.

URL
---
 - Provides URL encoding/decoding.

B64
---
 - Provides base64 encoding/decoding.
