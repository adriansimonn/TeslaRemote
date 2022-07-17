import teslapy
from teslapy import Tesla

print("<=     TeslaRemote     =>")
print("Developed by Adrian Simon")
print()
print()
teslaRemotePowerStatus = False

print("Log in to your Tesla account:")
email = input("Email: ")
redirectConsentPassFillerVar = input("Press enter to continue")

with teslapy.Tesla(email) as tesla:
    teslaRemotePowerStatus = True
    print("Logged into tesla account: " + email)
    vehicles = tesla.vehicle_list()
    # vehicles[0].sync_wake_up()
    # vehicles[0].command('ACTUATE_TRUNK', which_trunk='front')
    print(str(len(vehicles)) + " Registered Vehicles Detected:")
    for i in range(len(vehicles)):
        print("Vehicle Number " + str(i+1) + ":")
        print("Name: " + vehicles[i].get_vehicle_data()['display_name'])
        print("ID: " + str(vehicles[i].get_vehicle_data()['id']))
        print("Vehicle ID: " + str(vehicles[i].get_vehicle_data()['vehicle_id']))
        print("VIN: " + str(vehicles[i].get_vehicle_data()['vin']))
        print("Current State: " + vehicles[i].get_vehicle_data()['state'])
        print()
    print("Use -help command to see a list of commands")
    print()
    while teslaRemotePowerStatus:
        i = input("")
        if i == "-help":
            print("-honk (Vehicle Number) = Honks specified vehicle")
            print("-flash (Vehicle Number) = Flashes the exterior lights of specified vehicle")
            print("-lock (Vehicle Number) = Locks specified vehicle")
            print("-unlock (Vehicle Number) = Unlocks specified vehicle")
            print("-acoff (Vehicle Number) = Turns off air conditioning in specified vehicle")
            print("-acon (Vehicle Number) = Turns on air conditioning in specified vehicle")
            print("-temp (Vehicle Number) (Temperature) = Sets air conditioning temperature to specified number in specified vehicle")
            print("-openchargeport (Vehicle Number) = Opens charge port of specified vehicle")
            print("-closechargeport (Vehicle Number) = Closes charge port of specified vehicle")
            print("-startcharge (Vehicle Number) = Starts charging specified vehicle")
            print("-stopcharge (Vehicle Number) = Stops charging specified vehicle")
            print("-remotestart (Vehicle Number) = Remotely starts specified vehicle")
            print("-trunk (Vehicle Number) (front/rear = Activates specified trunk door on specified vehicle")
        elif i == "-exit":
            teslaRemotePowerStatus = False
        elif i[0:6] == "-honk ":
            vehicles[int(i[6:len(i)])-1].sync_wake_up()
            vehicles[int(i[6:len(i)])-1].command('HONK_HORN')
        elif i[0:7] == "-flash ":
            vehicles[int(i[7:len(i)])-1].sync_wake_up()
            vehicles[int(i[7:len(i)])-1].command('FLASH_LIGHTS')
        elif i[0:6] == "-lock ":
            vehicles[int(i[6:len(i)]) - 1].sync_wake_up()
            vehicles[int(i[6:len(i)]) - 1].command('LOCK')
        elif i[0:8] == "-unlock ":
            vehicles[int(i[8:len(i)]) - 1].sync_wake_up()
            vehicles[int(i[8:len(i)]) - 1].command('UNLOCK')
        elif i[0:7] == "-acoff ":
            vehicles[int(i[7:len(i)]) - 1].sync_wake_up()
            vehicles[int(i[7:len(i)]) - 1].command('CLIMATE_OFF')
        elif i[0:6] == "-acon ":
            vehicles[int(i[6:len(i)]) - 1].sync_wake_up()
            vehicles[int(i[6:len(i)]) - 1].command('CLIMATE_ON')
        elif i[0:6] == "-temp ":
            ia = i.split()
            vehicles[int(ia[1]) - 1].sync_wake_up()
            vehicles[int(ia[1]) - 1].command('CHANGE_CLIMATE_TEMPERATURE_SETTING', driver_temp=int(ia[2]), passenger_temp=int(ia[2]))
        elif i[0:15] == "-openchargeport ":
            vehicles[int(i[15:len(i)]) - 1].sync_wake_up()
            vehicles[int(i[15:len(i)]) - 1].command('CHARGE_PORT_DOOR_OPEN')
        elif i[0:15] == "-closechargeport ":
            vehicles[int(i[15:len(i)]) - 1].sync_wake_up()
            vehicles[int(i[15:len(i)]) - 1].command('CHARGE_PORT_DOOR_CLOSE')
        elif i[0:13] == "-startcharge ":
            vehicles[int(i[13:len(i)]) - 1].sync_wake_up()
            vehicles[int(i[13:len(i)]) - 1].command('START_CHARGE')
        elif i[0:12] == "-stopcharge ":
            vehicles[int(i[12:len(i)]) - 1].sync_wake_up()
            vehicles[int(i[12:len(i)]) - 1].command('STOP_CHARGE')
        elif i[0:13] == "-remotestart ":
            vehicles[int(i[13:len(i)]) - 1].sync_wake_up()
            vehicles[int(i[13:len(i)]) - 1].command('REMOTE_START')
        elif i[0:6] == "-trunk ":
            ia = i.split()
            vehicles[int(ia[1]) - 1].sync_wake_up()
            vehicles[int(ia[1]) - 1].command('ACTUATE_TRUNK', which_trunk=ia[2])
        else:
            print("Error")