# endcord-message-grouping

An [endcord](https://github.com/sparklost/endcord) extension that groups consecutive messages from the same author, hiding the repeated username — similar to how Discord desktop renders message history.

## Before / After

**Before:**
```
[14:17] <Saphii    > | hey
[14:17] <Saphii    > | imagine how stupid would it be if i stripped everything down
[14:18] <Saphii    > | funny
[14:19] <Saphii    > | i think i could try!
```

**After:**
```
[14:17] <Saphii    > | hey
[14:17] <           | imagine how stupid would it be if i stripped everything down
[14:18] <           | funny
[14:19] <           | i think i could try!
```

The username is shown once per group. It reappears whenever the author changes, or after a reply or interaction.

## Installation

1. Copy `endcord_message_grouping/` into your endcord extensions directory:
   - **Binary** (`/usr/bin/endcord`): `~/.local/share/endcord/Extensions/`
   - **Dev** (`uv run main.py`): `~/.config/endcord/Extensions/`
2. Restart endcord.

## Compatibility

Built for endcord `1.4.2`. A version mismatch warning may appear for other versions, but the extension will still load.
