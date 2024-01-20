import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
accessPoints = wlan.scan()

for ap in accessPoints:
    print(ap)
    
wlan.connect('POCO','mike6350')
print(wlan.isconnected())
print(wlan.ifconfig()[0])