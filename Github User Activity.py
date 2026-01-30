import sys
import json
import urllib.request
from http import HTTPStatus

index=-1
name = ""


if len(sys.argv) >1:
    name= sys.argv[1]
    giturl=f"https://api.github.com/users/{name}/events"
    try:
        with urllib.request.urlopen(giturl) as response:
            data = response.read()
            actions = json.loads(data)
            if (response.getcode() == HTTPStatus.OK):
                for i in actions:
                    index +=1
                    type = actions[index]["type"]
                    url = actions[index]["repo"]["name"]
                    if type == "PushEvent":
                        print(f"pushed to {url}")
                    elif type == "IssuesEvent":
                        print(f"Created a new issue in {url}")
                    elif type == "WatchEvent":
                        print(f"Starred {url}")
                    elif type == "ForkEvent":
                        print(f"Forked {url}")
                
                
    except:
        print("User not found")