#Creando un conjunto con set()
conjunto = set(["Dato1"])

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["Dato 1", "Dato 2"])
conjunto2 = {conjunto1, "Dato 3"}

#Teoria de conjunto 
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

resultado = conjunto2.issubset(conjunto1);
print(resultado)


print(conjunto2)