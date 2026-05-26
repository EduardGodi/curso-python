ingreso_mensual = 72000
gasto_mensual = 80000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estas bien en cualquier parte del mundo")
    else:
        print("y pa, estas gastando una banda, hay que ver si te alcanza")
        
elif ingreso_mensual > 1000:
    print("Estas bien en latinoamerica")
else:
    print("Eres pobre")