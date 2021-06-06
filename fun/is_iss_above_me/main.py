import requests
import datetime as dt
import time
import geocoder

MY_LOC= list(geocoder.ip('me').latlng)

MY_LAT = MY_LOC[0] # Your latitude
MY_LONG =MY_LOC[1] # Your longitude

def is_iss_overhead():
    global MY_LAT, MY_LONG
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT -5 < iss_latitude < MY_LAT +5  and MY_LONG -5 < iss_longitude < MY_LONG +5:
        return True
    else:
        return False


def is_night(sunrise, sunset, now_hour):
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now(dt.timezone.utc)

    if sunrise > sunset:
        if sunset < now_hour < sunrise:
            return True
        else:
            return False
    else: # if sunset < sunset
        if sunset < now_hour < sunset:
            return True
        else:
            return False

while True:
    if is_iss_overhead() == True and is_night (sunset, sunrise, int(time_now.hour)) == True :
        print('Look up the sky!  The ISS is above you!')
    else:
        print("Bummer, the ISS is not here yet")

    print('Waiting for 10 minutes to check again...')
    time.sleep(600)
