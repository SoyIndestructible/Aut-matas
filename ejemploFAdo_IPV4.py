"""ejemploFAdo_basico.py   Evalua una string con un automata finito deterministico
Descripción.
            -Muestra como evaluar una cadena de caracteres hasta evaluar posible estado de aceptación
            -
            https://ed.sjuanrio.tecnm.mx/pluginfile.php/118066/mod_folder/content/0/matemticas-discretas-6edi-johnsonbaugh.pdf
            
"""
from FAdo.fa import *
from FAdo.reex import *
from FAdo.fio import *

def evaluar():
    ip = input("Introduce una dirección IPv4: ")  
    clean_ip = ip.replace(".", "").replace(" ", "")
    m3 = DFA()
    m3.setSigma([str(i) for i in range(10)])  
    num_states = len(clean_ip) + 1  
    for i in range(num_states):
        m3.addState(f's{i}')
    m3.setInitial('s0')
    m3.addFinal(f's{len(clean_ip)}')  
    for i, char in enumerate(clean_ip):
        m3.addTransition(f's{i}', char, f's{i+1}')
    print("\nCadena limpia evaluada:", clean_ip)
    print("Verdadero o falso:", m3.evalWordP("19222234"))
    print("Always adicto al dick bien hard "+chr(9829))

