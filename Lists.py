#a = [2,4,5, -4]
#print(a)
#print(len(a))

#b = ["a1", "b1", "c1"]
#print(b[0])
#print(b[-1])

#b = ["a1", "b1", "c1"]
#print(b[0:2])

#b = ["a1", "b1", "c1", "d"]
#b[0:3] = ["test", "test1", "test2"]
#print(b)

#b = ["a1", "b1", "c1", "d"]
#print("a1" in b)

#b = ["a1", "b1", "c1", "d"]
#for  kaka in b:
 #   print(kaka)
""""
b = ["a1", "b1", "c1", "d"]
b.insert(1,"test")
b.remove("a1")
print(b)
languages1 = b.copy()
print(b)

mixed_list = ["hello", -34, "Java", True]
print("1.", mixed_list[-1])
mixed_list[1] = "Hi"
print("2.", mixed_list )

mixed_tuple = (1,3,4,5)
mixed_tuple[1] = 100
print("3.", mixed_tuple)
"""



"""
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
            print("Altitude(", altitude, ") is too high(Max 10000feet)!")
        else:
            iqh_alt(altitude)
elif initial == "temperature":
        temperature = int(input("enter current temperature(In Celsius, only numbers)  " ))
        if temperature<-5 or temperature>35:
            print("The temperature entered(" , temperature, ") is not valid. Please enter a value between -5 and 35!")
        else:
            iqh_temp(temperature)
            altitude = iqh_temp(temperature)
            iqh_alt(altitude)
else:
    print(initial, "is an invalid value, try again.")
    """





