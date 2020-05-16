#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    cifrado = string.ascii_letters + string.punctuation +string.hexdigits
    miclave=''.join(random.choice(cifrado) for letra in range(passLen))
    return miclave
    
clave=RandomPasswordGenerator(passLen=10)
print(clave)

def ClaveAleatoria(tamano):
    cifrado=string.ascii_letters + string.digits + string.punctuation
    miclave = ''.join(random.choice(cifrado) for letra in range(tamano))
    return miclave

contraseña = ClaveAleatoria(10)
print(contraseña)
