EXT_NAME = "Message Grouping"
EXT_VERSION = "1.0.0"
EXT_ENDCORD_VERSION = "1.4.2"
EXT_DESCRIPTION = "Hides repeated usernames for consecutive messages from the same author, Discord-style."

class Extension:
    def __init__(self, app):
        self.app = app

    def on_main_start(self):
        app = self.app
        tui = app.tui
        _orig = tui.update_chat

        def _patched(chat, chat_format):
            chat_map = getattr(app, 'chat_map', None)
            messages = getattr(app, 'messages', None)
            if chat_map and messages:
                _suppress(chat, chat_format, chat_map, messages)
            _orig(chat, chat_format)

        tui.update_chat = _patched

def _suppress(chat, chat_format, chat_map, messages):
    prev_author = None

    # Iterate top-to-bottom on screen = high index to low index (oldest to newest)
    for i in range(len(chat_map) - 1, -1, -1):
        entry = chat_map[i]

        if entry is None:
            # Image placeholder or spacing line — don't break the author chain
            continue

        msg_num, username_range, is_reply, *_ = entry

        if msg_num is None:
            # System line (unread separator, etc.)
            prev_author = None
            continue

        if username_range is None:
            # Continuation line, reply preview (is_reply=True), or interaction header (is_reply=2)
            # Reply/interaction headers visually break the group, so reset the chain.
            if is_reply in (True, 2):
                prev_author = None
            continue

        # This is the first line of a message (username_range is a (start, end) tuple).
        if not (0 <= msg_num < len(messages)):
            prev_author = None
            continue

        author = messages[msg_num].get('username') or ''

        if author and author == prev_author:
            # Same author as the message above — suppress the username.
            start, end = username_range
            line = chat[i]
            if len(line) >= end:
                chat[i] = line[:start] + ' ' * (end - start) + line[end:]
            # Remove the username color range from the format list (cosmetic, spaces are invisible).
            if i < len(chat_format):
                chat_format[i] = [
                    f for f in chat_format[i]
                    if not (len(f) == 3 and f[1] == start and f[2] == end)
                ]
        else:
            prev_author = author
