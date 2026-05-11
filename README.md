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

Clone directly into your endcord extensions directory. The folder **must** be named `endcord_message_grouping` (underscores, not hyphens):

**Binary** (`/usr/bin/endcord`):
```sh
git clone https://github.com/GhidBase/endcord-message-grouping ~/.local/share/endcord/Extensions/endcord_message_grouping
```

**Dev** (`uv run main.py`):
```sh
git clone https://github.com/GhidBase/endcord-message-grouping ~/.config/endcord/Extensions/endcord_message_grouping
```

Then restart endcord.

## Compatibility

Built for endcord `1.4.2`. A version mismatch warning may appear for other versions, but the extension will still load.
