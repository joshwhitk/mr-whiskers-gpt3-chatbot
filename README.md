# mr whiskers gpt3 chatbot

A command-line character-chat experiment: a cat discusses children's books using a prompted language model.

## Scope and status

- joshChat.py loads the character template from prompt_chat.txt and accumulates conversation turns in memory.
- The script uses the legacy openai.Completion interface and a hardcoded model choice; compatibility with today's API has not been established. Modernizing the client is required before treating this as a supported application.
- Although the introduction says to type exit, the reviewed loop does not implement an exit branch. Stop the process with Ctrl+C.

Documentation reviewed from source and available project history on 2026-09-27. The application was not started or acceptance-tested as part of this documentation update.
