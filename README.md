# Clash Royale Command-Line Interface
[![Build Status](https://api.travis-ci.com/tungyueh/clashroyaleapi.svg?branch=master)](https://travis-ci.com/tungyueh/clashroyaleapi)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

CLI using Clash Royale API

## Usage
1. Go to https://developer.clashroyale.com/#/ to create a key
2. Paste the key into a file
3. python cli/cli.py -a [file_path] [-v]

## auth file format
Please refer sample_auth.json

```
{
    "player_tag": "",
    "clan_tag": "",
    "token": ""
}
```
