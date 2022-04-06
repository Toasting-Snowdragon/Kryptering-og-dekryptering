from cmath import e
import math
import random

#´´først print 2 primtal´´ 

#Her tilføjer vi en værdi til en variabel, værdien er en liste over primtallene fra 2-349. 
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                31, 37, 41, 43, 47, 53, 59, 61, 67,
                71, 73, 79, 83, 89, 97, 101, 103,
                107, 109, 113, 127, 131, 137, 139,
                149, 151, 157, 163, 167, 173, 179,
                181, 191, 193, 197, 199, 211, 223,
                227, 229, 233, 239, 241, 251, 257,
                263, 269, 271, 277, 281, 283, 293,
                307, 311, 313, 317, 331, 337, 347, 349]
#Der definere vi en afhængig variabel (den afhænger af n), som generere et tilfældigt genereret tal mellem 2^(n-1)+1 og 2^n-1
def Randomtal (n):
    return(random.randrange(2**(n-1)+1, 2**n-1))
#Her definere vi en variabel som kommer til at være vores primtal. 
def lilleprime (n):
    #Der laves en løkke som tjekker om vores tal kan divideres med alle værdier i listen af primtal. 
    while True:
        pc = Randomtal(n)
        #Test om det kan divideres med vores allerede definerede primtal. 
        for divisor in prime_numbers:
            if pc % divisor == 0 and divisor**2 <= pc:
                break
        else: return pc
#Her definere vi en funktion, som skal tjekke sandsynligheden for at vores tal er et primtal. 
def primtaltest(mrc):
    maxDivisionsByTwo = 0
    ec = mrc-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    #Her laver vi en assert funktion som stopper programmet hvis den er sand. 
    assert(2**maxDivisionsByTwo * ec == mrc-1)
 
    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                return False
        return True
    #Her fastslår vi hvor mange gange vi skal kører primtalstesten. 
    numberOfRabinTrials = 20
    #Vi laver en løkke der teste vores primtaltest x antal gange.
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True
 
#Der defineres et input, som vælger størrelsen af primtallene. 
bit_nr = input("Hvor stor en bit nøgle skal det være?")
  
print(type(bit_nr))
  
#Konverter fra string til integer. 
int_num = int(bit_nr)
  
#her laver vi en if funktion som kombinere alle de definitioner og variabler vi har skrevet indtil videre. 
if __name__ == '__main__':
    #vi laver en en løkke hvor vi sørger for at vores primtal overholder de krav vi har sat for det. 
    while True:
        n = int_num
        prime_p = lilleprime(n)
        #if funktionenen sørger for at kører primtalstesten indtil vi får et tal der kommer igennem altså løkken breaker. 
        if not primtaltest(prime_p):
            continue
        else:
            print(prime_p)
            break


#Gør det samme som den ovenover for at få primtal nr 2. 
if __name__ == '__main__':
    while True:
        n = int_num
        prime_q = lilleprime(n)
      
        if not primtaltest(prime_q):
            continue
        else:
            print(prime_q)
            break

#Her inbringer vi Eulers Phi funktion som er bevist for. 
Phi = (prime_p-1)*(prime_q-1)

#Her regner vi første del af vores nøgler ud nemlig n værdien. 
key = (prime_q * prime_p)


#Generere et random tal, som er større end 1 men mindre en phi. 
x = 1
def Randomtal(x):
    return(random.randrange((x+1), Phi-1))
    

#Sætter betingelser op for e, da e ikke må være kongruent med phi og e skal være mindre end phi. 
#Vi opsætter en while true funktion der skal sørger for at vores e værdi overholder visse krav.
while True:
    e = Randomtal(x)
    E = math.gcd(Phi,e)  
        
    #Første krav er at gcd(Phi(n),e)=1 
    if E == 1:
        #Andet krav vi opsætter er at e ikke må være større end phi(n)
        if E < Phi:
            print(e)
            break
        elif E > Phi:
            continue
    elif E > 1:
        continue

#Funktion der definere den besked man vil kryptere. 
besked = input("input din besked til kryptering \n ")
#Vi definere en funktion som skal kryptere end besked på henblik på e og n værdien. 
def encrypt (e, key, besked): 
    
    cipher = " "
    #vi laver en løkke der implementere nedenstående funktioner på hver variabel i beskeden. Løkken stopper når alle variabler er kørt igennem.
    for c in besked:
        #Python funktionen ord() tager og omdanne string tekst til unicode. Altså integers. 
        m = ord(c)
        #Vi tager vores besked og udfører denne formel, m^e (mod n) (pow, tager x^y og hvis z er en variabel tager den x^y (mod z))
        cipher += str(pow(m, e, key)) + " "
    #Løkken stopper og returnere en færdig krypteret cipher.     
    return cipher

#Vi definere en sidste main funktion som skal forbinde vores input med krypteringen og printe de forskellige vigtige værdier.
def main():
    msg = besked
    enc = encrypt(e, key, msg)

    print(f"Message: {msg}")
    print(f"Din offentlige nøgle er - e: {e} og n: {key}")
    print (f"Primtal: p = {prime_p} og q = {prime_q}")
    print(f"encrypted: {enc}")
main()

#####DETTE HERUNDER ER IKKE EN DEL AF KODEN, DET ER TING OG FUNKTIONER DER BLEV AFPRØVET I KODEN MEN SOM IKKE VIRKEDE#####
####.....DET ER DERFOR IKKE EN DEL AF OPGAVEN......#####

#definer en tranlation 
#cipher = []
#denne fortæller at alle string variabler i skal oversættels til alphabetets integer der passer med den samme string værdier. 
#for i in enkrypt: 
    #Translation = alphabet[i] 
#brug c = translation ^e mod n (hvor e og n er vores offentlige nøgle)
    #c = (Translation**e)%key
    #cipher.append(c)

#den krypterede besked bliver printet. 
#print ('Cipherkode: {}'.format(cipher))





#enkrypt med nøglerne. 

# vi definere oversættelses alfabetet.
alphabet= {
        'a' : 2, 
        'b' : 3, 
        'c' : 4, 
        'd' : 5, 
        'e' : 6, 
        'f' : 7, 
        'g' : 8, 
        'h' : 9, 
        'i' : 10, 
        'j' : 11, 
        'k' : 12, 
        'l' : 13, 
        'm' : 14, 
        'n' : 15, 
        'o' : 16, 
        'p' : 17, 
        'q' : 18, 
        'r' : 19, 
        's' : 20, 
        't' : 21, 
        'u' : 22, 
        'v' : 23, 
        'w' : 24, 
        'x' : 25, 
        'y' : 26, 
        'z' : 27,
        'æ' : 28,
        'ø' : 29,
        'å' : 30,
        ' ' : 31,
        'A' : 32, 
        'B' : 33, 
        'C' : 34, 
        'D' : 35, 
        'E' : 36, 
        'F' : 37, 
        'G' : 38, 
        'H' : 39, 
        'I' : 40, 
        'J' : 41, 
        'K' : 42, 
        'L' : 43, 
        'M' : 44, 
        'N' : 45, 
        'O' : 46, 
        'P' : 47, 
        'Q' : 48, 
        'R' : 49, 
        'S' : 50, 
        'T' : 51, 
        'U' : 52, 
        'V' : 53, 
        'W' : 54, 
        'X' : 55, 
        'Y' : 56, 
        'Z' : 57,
        'Æ' : 58,
        'Ø' : 59,
        'Å' : 60,
        '1' : 61,
        '2' : 62,
        '3' : 63,
        '4' : 64,
        '5' : 65, 
        '6' : 66,
        '7' : 67,
        '8' : 68,
        '9' : 69,
        '0' : 70
    }
#enkrypt = input("input din besked til kryptering \n ")
#definer en tranlation 
#cipher = []
#denne fortæller at alle string variabler i skal oversættels til alphabetets integer der passer med den samme string værdier. 
#for i in enkrypt: 
#    Translation = alphabet[i] 
#brug c = translation ^e mod n (hvor e og n er vores offentlige nøgle)
#    c = (Translation**e)%key
#    cipher.append(c)

#den krypterede besked bliver printet. 
#print ('Cipherkode: {}'.format(cipher))

 
#afkrypter

Afkrypt_alphabet= {
        2 : 'a', 
        3 : 'b', 
        4 : 'c', 
        5 : 'd', 
        6 : 'e', 
        7 : 'f', 
        8 : 'g', 
        9 : 'h', 
        10 : 'i', 
        11 : 'j', 
        12 : 'k', 
        13 : 'l', 
        14 : 'm', 
        15 : 'n', 
        16 : 'o', 
        17 : 'p', 
        18 : 'q', 
        19 : 'r', 
        20 : 's', 
        21 : 't', 
        22 : 'u', 
        23 : 'v', 
        24 : 'w', 
        25 : 'x', 
        26 : 'y', 
        27 : 'z',
        28 : 'æ',
        29 : 'ø',
        30 : 'å',
        31 : ' ',
        32 : 'A', 
        33 : 'B', 
        34 : 'C', 
        35 : 'D', 
        36 : 'E', 
        37 : 'F', 
        38 : 'G', 
        39 : 'H', 
        40 : 'I', 
        41 : 'J', 
        42 : 'K', 
        43 : 'L', 
        44 : 'M', 
        45 : 'N', 
        46 : 'O', 
        47 : 'P', 
        48 : 'Q', 
        49 : 'R', 
        50 : 'S', 
        51 : 'T', 
        52 : 'U', 
        53 : 'V', 
        54 : 'W', 
        55 : 'X', 
        56 : 'Y', 
        57 : 'Z',
        58 : 'Æ',
        59 : 'Ø',
        60 : 'Å',
        61 : '1',
        62 : '2',
        63 : '3',
        64 : '4',
        65 : '5', 
        66 : '6',
        67 : '7',
        68 : '8',
        69 : '9',
        70 : '0'
    }

#dekrypt = input("Cipherkode input: \n ")
#definer en tranlation 
#for i in cipher: 
#    cipher2 = ((int(i)**int(find_d))%int(key))

#print (cipher2)

#print ('Original besked: {}'.format(besked))
#int_krypt = cipher(dekrypt)

#dekrypted = (int_krypt**d)%key

#for c in dekrypted: 
#    Translation2 = Afkrypt_alphabet[c] 


#definer en tranlation 
##string_cipher = ''
#denne fortæller at alle string variabler i skal oversættels til alphabetet der passer med den samme string værdier. 

#brug c = translation ^e mod n (hvor e og n er vores offentlige nøgle)
#for c in dekrypt: 
 #   Translation = Afkrypt_alphabet[i] 

##string_cipher += Afkrypt_alphabet[Translation]



#den krypterede besked bliver printet. 


