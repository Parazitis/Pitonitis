vards = str(input("Ievadiet Vardu"))
uzvards = str(input("Ievadiet uzvardu"))
vecums = int(input("Ievadiet vecumu(skaitlis)"))
klase = int(input("ievadiet klasi(cipars)"))
dzimums = str(input("Ievadiem dzimumu(vards)")) 
klases_nr = str(input("Ievadiet klases burtu(burts)"))
def bvsk_info(*args, **kwargs):
    value1= args
    value2= kwargs
    return value1,value2
bvsk_info(klase , klases_nr, vards = vards,uzvards = uzvards, vecums = vecums, dzimums=dzimums)
value1 = bvsk_info(vards = vards,uzvards = uzvards,vecums = vecums,dzimums = dzimums)
value2 = bvsk_info(klase = klase, paralelklase = klases_nr)
personigais_info = value1
skolas_info = value2
print("BVSK neinterese ", skolas_info)
print("BVSK interese ", personigais_info)


