initial= str(input("Enter Altitude or Temperature. To determine pressure under isa conditions(Max 10000 ft)  "))

    
def iqh_temp(temperature):
    isa_dev = temperature - 15
    altitude = isa_dev*-500
    return altitude

def iqh_alt(altitude):
    temperature = 15 - (altitude/1000 * 2)
    indicated_pressure = 1013-altitude//30
    print("The pressure is ", indicated_pressure,    "hPa at an altitude of ", altitude , "feet AMSL with a temperature of ", temperature, "Celsius.(ISA conditions)" )
    return indicated_pressure

if initial == "altitude":
        altitude = int(input("Enter current altitude in feet(only numbers)   "))
        if altitude>10000:
            print("Altitude too high(Max 10000feet)")
        else:
            iqh_alt(altitude)
elif initial == "temperature":
        temperature = int(input("enter current temperature(In Celsius, only numbers)  " ))
        iqh_temp(temperature)
        altitude = iqh_temp(temperature)
        iqh_alt(altitude)
else:
    print(initial, "is an invalid value, try again.")
    






