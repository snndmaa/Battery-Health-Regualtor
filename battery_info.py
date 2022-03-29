import psutil
from plyer import notification
import time

#import sensors battery class from psutils which contains battery remaining info
switch = 1
while(switch):
    battery = psutil.sensors_battery()
    percent = battery.percent
    # time_left = battery.secsleft      #seconds left
    is_charging = battery.power_plugged

    if( (is_charging) & (percent > 97) ):
       while((is_charging) & (percent > 97)):
            notification.notify(
            title = "Battery Full!!!",
            message = f"Percentage = {str(percent)}%. UNPLUG!",
            timeout=30,
            )
            time.sleep(10)
            
            #new object instance
            battery = psutil.sensors_battery()
            is_charging = battery.power_plugged
            if(is_charging == False):
                break
    elif(is_charging):
        notification.notify(
        title = "Battery Charging!",
        message = f"Battery Currently at - {str(percent)}%",
        timeout=10,
        )
    else:
        notification.notify(
        title = "Battery In Use.",
        message = f"Battery Remaining - {str(percent)}%",
        timeout=10,
        )
    

    #program repeats execution after every (min * 60mins)
    time.sleep(15*60)


    #continue to restart loop
    continue