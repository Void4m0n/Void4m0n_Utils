import requests
import os

# Function to generate a new JWT token
def New_token():
    url = "foo" # Authentication Endpoint 
    data_json = {"password":"foo","username":"foo"}
    Headers = {"Authorization": "Basic foo"} # Example of custom header
    r = requests.post(url, json=data_json, headers=Headers)
    return r.json()['access_token'] # The response is processed as a json and returns the access_token of the response. 

# If the code is 401 a new token is generated and saved in a file ./token.txt, if the file already exists it is deleted before saving the new JWT 
def postprocess(page, headers=None, code=None):
    if code == 401:
        token=New_token()
        if os.path.exists("./token.txt"):
          os.remove("./token.txt")
        else:
            pass
    
        with open("./token.txt", "w") as file:
            file.write(token)
    else: 
        pass
    return page, headers, code
