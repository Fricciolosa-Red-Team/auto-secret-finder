
## Based on [m4ll0k/Secret-Finder](https://github.com/m4ll0k/SecretFinder)

Basically it runs Secret-Finder on multiple urls, edit the last line of
`auto-secret-finder.py` as you want to fit your goals.

### Installation

1. `git clone https://github.com/Fricciolosa-Red-Team/auto-secret-finder.git autosecretfinder`
2. `cd autosecretfinder`
3. `python -m pip install -r requirements.txt` or `pip install -r requirements.txt`

### Usage 
`python3 auto-secret-finder.py subs.txt` (where subs.txt is a list of domains).

or 

`./for.sh subs.txt`

Remember to edit as you want the last line of [auto-secret-finder](https://github.com/Fricciolosa-Red-Team/auto-secret-finder/blob/main/auto-secret-finder.py#L31) to customize the command.
