def iqh_temp(temperature, msl_temp):                                                                                                                                                                             #altitude based on temperature
        temp_difference =temperature - msl_temp
        altitude = temp_difference*-500
        return altitude
def iqh_alt_p(altitude,qnh):                                                                                                                                                                                     #indicated pressure based on altitude and qnh + print txt
        temperature = 15 - (altitude/1000 * 2)
        indicated_pressure = qnh-altitude//30
        print("The pressure is ", indicated_pressure ,    "hPa at an altitude of ", altitude , "feet AMSL with a temperature of ", temperature, "Celsius.(With a QNH of", qnh,"hPa)")
def iqh_alt(altitude,qnh):                                                                                                                                                                                       #indicated pressure based on altitude and qnh
        temperature = 15 - (altitude/1000 * 2)
        indicated_pressure = qnh-altitude//30
        return indicated_pressure
def dev_qnh(qnh):                                                                                                                                                                                                   #pressure deviation based on qnh
    press_dev = qnh - 1013
    return press_dev 
def alt_iqh_qnh(iqh,qnh):                                                                                                                                                                                           #altitude based on iqh and qnh
    altitude = (qnh-iqh)*30
    return altitude           #temperature deviation
start = str(input("What do you want to calculate?(Pressure or altitude)   "))                                                                                                                                       #Enter value to calculate
start = start.upper()
qnh = int(input("Enter current QNH(hPa)   "))                                                                                                                                                                        #enter QNH
dev_qnh(qnh)
press_dev = dev_qnh(qnh)                                                                                                                                                                                            #calculate pressure deviation from standart(ISA) pressure
msl_temp = int(input("Enter temperature at mean sea level(MSL) in Celsius.   "))                                                                                                                                     #Enter MSL temperature
temp_dev = msl_temp - 15    
if str(start) == "PRESSURE":                                                                                                                                                                                          #starts 'if' cycle if value to calculate is pressure
    initial = str(input("Enter the known value(Altitude or Temperature). To determine pressure under isa conditions(Max 10000 ft)   "))                                                                           #asks for a value that is known
    initial = initial.upper()   
    if initial == "ALTITUDE":                                                                                                                                                                                            #starts 'if' cycle if altitude is the known value 
            altitude = int(input("Enter current altitude in feet(only numbers)   "))                                                                                                                                #allows entry of known altitude
            if altitude>10000:                                                                                                                                                                                      #Checks if altitude is within limits
                print("Altitude(", altitude, ") is too high(Max 10000feet)!")                                                                                                                                   #outputs error message if altitude out of limits
            else:   
                iqh_alt_p(altitude,qnh)                                                                                                                                                                               #starts "indicated pressure based on altitude and qnh and print txt" function
    elif initial == "TEMPERATURE":                                                                                                                                                                                   #Else if temperature is the known value, starts 'elif' cycle
            temperature = int(input("enter current temperature(In Celsius, only numbers)   " ))                                                                                                                      #Allows entry of OAT temperature
            iqh_temp(temperature,msl_temp)                                                                                                                                                                       #starts "altitude based on temperature" function
            altitude = iqh_temp(temperature, msl_temp)
            iqh_alt(altitude,qnh)       
            iqh = iqh_alt(altitude, qnh)          
            print("The pressure is ", iqh, "hPa.")                                                                                                                                                                 #starts "indicated pressure based on altitude and qnh + print txt"
    else:                               
        initial.lower()                 
        print(initial, "is an invalid value, try again.")                                                                                                                                                              #Outputs error message if invalid data is inputed

elif  str(start) == "ALTITUDE":                                                                                                                                                                                         #starts 'elif' cycle if the value to be calculated is altitude
        initial = str(input("Enter the known value(pressure(IQH)) or Temperature(OAT). To determine altitude under isa temperature conditions(Max 10000 ft)   "))                                                       #allows entry of a already known value
        initial = initial.upper()
        if initial == "TEMPERATURE":                                                                                                                                                                                  #starts 'if' cycle if temperature is the known value
            temperature = int(input("Enter known temperature(In Celsius)(OAT)   "))                                                                                                                                 #allows entry of the known temperature
            iqh_temp(temperature, msl_temp)                                                                                                                                                                           #starts "altitude based on temperature" function
            altitude = iqh_temp(temperature, msl_temp)
            print("The altitude is " ,altitude," feet AMSL." )                                                                                                                                                      #prints the resulting altitude       
        elif initial == "PRESSURE":                                                                                                                                                                                  #starts 'elif' cycle if the known value is pressure
            iqh = int(input("Enter current indicated pressure(hPa).   "))                                                                                                                                               #Allows entry of indicated pressure
            alt_iqh_qnh(iqh, qnh)                                                                                                                                                                                     #starts "altitude based on iqh and qnh" function
            altitude = alt_iqh_qnh(iqh, qnh)        
            print("The altitude is ", altitude, " feet AMSL.")                                                                                                                                                        #prints resulting altitude
        else:
            print(initial, " is an invalid entry, try again. ")                                                                                                                                                          #prints error message if entered value is invalid

else:
    print(start, " is not a valid entry.Try again")                                                                                                                                                                   #prints error message if entered value is invalid











