import math

#Vi giver en værdi til hvert af de input brugeren skal give for dekryptere.
prim_p=input("primtal p = ")
prim_q=input("primtal q = ")
e_value=input("indsæt e værdi: ")

chipher_kode=input("indsæt cipher: ")
#Her omdanner vi de værdier som blev givet som str til int. 
print(type(prim_p))
p = int(prim_p)
print(type(prim_q))
q = int(prim_q)
print(type(e_value))
e = int(e_value)
#Udregner phi(n) ved brug af de to primtal fra inputtene 
phi = ((p-1) * (q-1))


#Euklids algoritme. 
#Der laves en def som bruges til at udregne vores d (private nøgle). Der defineres en variable 
def egcd (a,b):
    #Der tildeles nogle værdier til nogle variabler
    s = 0 ; old_s = 1
    t = 1 ; old_t = 0
    r = b ; old_r = a
    #Vi laver en løkke som skal kører en række udregninger for at returnere 3 værdier. 
    while r != 0:
        #Floor division, den returnere kvotienten, altså kommatallet. 
        kvotienten = old_r // r
        #Her finder vi resten r, resten = old_r - kvotienten * r. Vi sætter basically programmet igang med euklids algoritme. 
        old_r, r = r, old_r - kvotienten * r
        #Her sørger vi for at den kan gå tilbage, for at finde d. Da e·d (mod n) = 1 kan vi på den her måde udregne d med euklids algoritme. 
        old_s, s = s, old_s - kvotienten * s
        old_t, t = t, old_t - kvotienten * t
    return old_r, old_s, old_t

#Vi inplementere Euklids algoritme og sætter betingelser op hvis nu at værdien skulle være negativ. 
def modularInv (a,b):
    gcd, x, y = egcd(a,b)
    #Vi fortæller programmet at hvis x værdien er mindre end 0 skal den gøre følgende: 
    if x < 0:
        #Den skal lægge phi til x og udskrive værdien. 
        x += ((p-1) * (q-1))
    return x

#Vi definere funktionen decrypt som vi sætter nogle krav op for hvordan den skal dekryptere. 
def decrypt (d, n, cipher):
    #Vi definere d, som er ens første halvdel af den private nøgle, ifølge vores tidligere defineret formel, modularinv <- egcd 
    d = modularInv(e, phi)
    #Vi implementere cipherkoden. Altså det input man gav tidligere. 
    cipher = chipher_kode
    #Vi definere n som skal bruges til at dekryptere. (anden halvdel af den private nøgle)
    n = p * q
    #Vi fortæller at msg skal være str. 
    msg = " "
    
    #Vi bruger split() som opdeler cipheren i hver sin del. Laver en liste over alle variabler i ciphere.
    parts = cipher.split()
    #Vi har tildelt parts listen af værdier fra cipheren. Vi siger så at for hver del af cipheren skal den gøre følgene: 
    for part in parts: 
        if part: 
            #vi laver de forskellige dele af cipheren om til integers så vi kan regne på dem. 
            c = int(part)
            #vi tager vores besked og udfører denne formel, c^d (mod n) (pow, tager x^y og hvis z er en variabel tager den x^y (mod z))
            #dernæst tager vi og gør det modsastte af ord() funktionen, chr() som tager og omdanner bytes til string.
            msg += chr(pow(c, d, n))
    #Returner den dekryptere besked. 
    return msg 

#har integrere vi alle de dele vi tidligere har skrevet, for at dekryptere. 
def main():
    d = modularInv(e, phi)
    n = p * q
    dec = decrypt (d, n, chipher_kode)
    print(f"dekrypterede besked: {dec}")
main()