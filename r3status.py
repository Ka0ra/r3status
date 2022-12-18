import requests as rq
import json as js
import sys
import datetime as dt
from dataclasses import dataclass

class Sensor:
    def __init__(self, data):
        if "description" in data:
            self.description = data["description"]
        if "location" in data:
            self.location = data["location"]
        if "name" in data:
            self.name = data["name"]
        if "value" in data:
            self.value = data["value"]
        if "timestamp" in data:
            self.timestamp = dt.datetime.fromtimestamp(data["timestamp"])
        if "unit" in data:
            self.unit = data["unit"]

# @dataclass
# class Window:
#     inner: Sensor
#     outer: Sensor
#
#     def even(self):
#         if
#
#     def valid(self):
#         if self.even():
#             if self.inner.value and self.outer.value:
#



try:
    response = rq.get('https://realraum.at/status.json')
except Exception:
    print("network error")
    sys.exit(2)

if not response:
    print('Not found')
    sys.exit(1)

loaded_res = js.loads(response.text)


def getSensorByName(sensor_type, name):
    for sensor in loaded_res["sensors"][sensor_type]:
        if sensor["name"] == name:
            return Sensor(sensor)
    raise Exception("no value data found for sensor {} of type {}".format(name, sensor_type))

def isDoorLocked(name):
    if getSensorByName("door_locked", name).value:
        return "locked"
    else:
        return "unlocked"

def isDoorWindowClosed(name):
    if getSensorByName("ext_door_ajar", name).value:
        return "closed"
    else:
        return "open"

# def windowPairClosed(inner_window, outer_window):
#     if isDoorWindowClosed(inner_window).value and isDoorWindowClosed(outer_window).value:
#         return True

#Leute anwesend?

#Whg 1 Leute anwesend general (+timestamp)
if getSensorByName("door_locked", "Space1Empty").value:
    print("Nobody in W1.")
else:
    print("There are people in W1.")

#Whg 1 LoTHR temp
lothr_temp = getSensorByName("temperature", "Temp@LoTHR")
lothr_hum = getSensorByName("humidity", "Humidity@LoTHR")
print("LoTHR: {}°C with {}% humidity at {:%A, %d. %B %Y - %H:%M:%S}.".format(lothr_temp.value, lothr_hum.value, lothr_temp.timestamp))



#Whg 2 Leute anwesend general
if getSensorByName("door_locked", "Space2Empty").value:
    print("Nobody in W2.")
else:
    print("There are people in W2.")




#sanity check
def sanityCheck():


    #####door status#######
    #Whg 1 Front door unlocked/locked and open/close?
    print("W1 frontdoor is {} and {}.".format(isDoorLocked("LockW1Torwaechter"), isDoorWindowClosed("AjarW1Torwaechter")))

    #Whg 1 backdoor blue locked
    print("Backdoor blue is {} and {}.".format(isDoorLocked("LockBackdoorBlue"), isDoorWindowClosed("AjarBackdoorBlue")))

    #Whg 2 Front door unlocked/locked and open/close?
    print("W2 door is {} and {}.".format(isDoorLocked("LockW2Door"), isDoorWindowClosed("AjarW2Door")))

    ######window status#####



    #Whg 1 Masha inner window

    # if windowPairClosed("AjarWindowMaSha", "AjarWindowoutr MaSha"):
    #     print("All MaSha windows closed.")
    # elif isDoorWindowClosed("AjarWindowMaSha").value:
    #     print("MaShas
    #
    #Whg 1 Masha outer window

    #Whg 1 OLGA window
    print("OLGA window is {}.".format(isDoorWindowClosed("AjarWindowOLGA")))


    #Wh2 2 realfunk window
    print("RealFunk window is {}.".format(isDoorWindowClosed("AjarWindowRealFunk")))
    #Whg 2 kitchen window
    print("Kitchen window is {}.".format(isDoorWindowClosed("AjarWindowKitchen")))
    #Whg 2 r2w2 window left

    #Whg 2 r2w2 window right
