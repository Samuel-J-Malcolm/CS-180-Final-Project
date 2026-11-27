import requests, json, datetime

# Credit to https://github.com/noahrinehart/purdue-dining-bitbar/blob/master/purduedining.12h.py for this code 
locations = ["Wiley", "Ford", "Hillenbrand", "The Gathering Place", "Earhart", "Windsor"]
url = "http://api.hfs.purdue.edu/menus/v2/locations/"
header={"Accept":"application/json"}

def fetch_menu(location: str,delta: datetime.timedelta):
    time = datetime.datetime.now() + delta
    ftime = time.strftime("%m-%d-%Y")
    try:
        r =  requests.get(url+location+"/"+ftime+"/", headers=header)
        return r.json()
    except requests.ConnectionError:
        print("Failed to connect!")
#end credit 
if (True):
    print("start")
    data = fetch_menu(locations[1],datetime.timedelta(7))
    with open("data/data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


