import requests
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL # Set tamper priority 

def dependencies():
    pass

# Reads the token from the file ./token.txt and returns it
def get_token_from_file():
    with open("./token.txt", "r") as file:
        Updated_token = file.read()
    return Updated_token

# Overwrites the JWT with the Updated_token on all requests 
def tamper(payload, **kwargs):
    access_token = get_token_from_file()
    hdrs = kwargs.get("headers",{})
    hdrs["Authorization"] = "Bearer "+access_token
    return payload

# https://blog.telspace.co.za/2020/05/bypassing-refresh-tokens-with-sqlmaps_20.html
