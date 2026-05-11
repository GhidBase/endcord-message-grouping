# endcord-message-grouping

An [endcord](https://github.com/sparklost/endcord) extension that groups consecutive messages from the same author, hiding the repeated username — similar to how Discord desktop renders message history.

## Before / After

**Before:**
```
[14:17] <Alice     > | hey everyone
[14:17] <Alice     > | just pushed the new build
[14:18] <Alice     > | let me know if anything looks off
[14:19] <Alice     > | should be good to test now
```

**After:**
```
[14:17] <Alice     > | hey everyone
[14:17] <           | just pushed the new build
[14:18] <           | let me know if anything looks off
[14:19] <           | should be good to test now
```

The username is shown once per group. It reappears whenever the author changes, or after a reply or interaction.

## Installation

1. Copy `endcord_message_grouping/` into your endcord extensions directory:
   - **Binary** (`/usr/bin/endcord`): `~/.local/share/endcord/Extensions/`
   - **Dev** (`uv run main.py`): `~/.config/endcord/Extensions/`
2. Restart endcord.

## Compatibility

Built for endcord `1.4.2`. A version mismatch warning may appear for other versions, but the extension will still load.
