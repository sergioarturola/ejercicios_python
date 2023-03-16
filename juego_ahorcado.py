import random

lista_escondida = []#para que al inicio muestre guiones bajos con el tamaño de la palabra seleccionada
indice_letras = []
para_adivinar = ["perro", "casa", "autobus", "libro", "gato", "auto"]

def iniciar(): #inicia el juego y retorna la palabra seleccionada
    
    print("Iniciando juego")
    seleccionada = random.choice(para_adivinar)
    return seleccionada


seleccionada_jugar = iniciar() #guardo la palabra escogida al azar en seleccionada_jugar
taman = len(seleccionada_jugar)#obtengo el tamaño para saber cuantos guiones bajos poner 

for i in range(taman):#ciclo for para impirmir los guiones bajos, 
    lista_escondida.append(" _ ")


print(lista_escondida)

while True:#inicio del ciclo hasta que se adivine la palabra 

    letra_user = input("Escribe una letra: ")

    for i, caracteres in enumerate(seleccionada_jugar): #enumero la palabra seleccionada
        if caracteres == letra_user:
            indice_letras.append(i) #si encuentra la letra o letras, vamos a guardar sus indices en esta lista

#ahora sustituyendo los indices por las letras en la lista_escondida
    for i in indice_letras:
        lista_escondida[i] = letra_user

    
    indice_letras.clear() #para borrar los indices y vuelva a quedar vacia la lista
    
    print(lista_escondida) #se van mostrando las letras en lugar de los guiones
    
    se_va_formando = "".join(lista_escondida)
    if se_va_formando == seleccionada_jugar: #cuando la palabra formada sea igual a la seleccionada se rompe el ciclo
        break
    


#Mensaje final
print("Felicidades ganaste!!!")




