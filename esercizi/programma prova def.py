def area_cilindro(raggio, altezza):
    pigreco = 3.14159
    area = pigreco*(raggio**2)
    circonferenza = 2*pigreco*raggio
    return 2*area + altezza*circonferenza

print area_cilindro(10, 5), area_cilindro(20, 10)

def hms(nsec):
    hh = nsec/3600
    nsec = nsec % 3600
    mm = nsec/60
    ss = nsec % 60
    print hh, mm, ss

print hms(4000), hms(100000)