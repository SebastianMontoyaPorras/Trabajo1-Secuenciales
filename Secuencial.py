#Hecho por:Sebastian Montoya Porras
#Grupo-1


'''1)Suponga que un individuo desea invertir su capital en un banco y desea saber cuanto
dinero ganara después de un mes si el banco paga a razón de 2% mensual.'''

cap_inv=float(input("digite capital"))
gan=cap_inv * 0.2
print(gan)

'''2) Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el
vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres
ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo
base y comisiones.'''
sueldo_base=int(input("Ingrese sueldo base: "))
venta1=int(input("Ingrese venta 1: "))
venta2=int(input("Ingrese venta 2: "))
venta3=int(input("Ingrese venta 3: "))
total_ventas=venta1+venta2+venta3
comision=total_ventas*0.10
total_pagar=sueldo_base+comision
print("Su sueldo del mes es: ", total_pagar)

'''3) Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea
saber cuanto deberá pagar finalmente por su compra.'''

total_compra=int(input("ingrese valor del producto: "))
descuento=total_compra*0.15
total_pagar=total_compra-descuento
print("El valor total es: ", total_pagar)

'''4) Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha
calificación se compone de los siguientes porcentajes:'''

calificacion1=int(input("ingrese nota 1: "))
calificacion2=int(input("ingrese nota 2: "))
calificacion3=int(input("ingrese nota 3: "))
Examen=int(input("ingrese nota Examen: "))
TrabajoFinal=int(input("ingrese nota trabajo final: "))
promedioParciales= (calificacion1+calificacion2+calificacion3)/3
NotaParciales=promedioParciales*0.55
NotaExamen=Examen*0.30
NotaTrabajo=TrabajoFinal*0.15
CalificacionFinal=NotaParciales+NotaExamen+NotaTrabajo
print("Nota Final es: ",CalificacionFinal)

'''5) Un maestro desea saber que porcentaje de hombres y que porcentaje de mujeres hay en
un grupo de estudiantes.'''

numero_hombres=int(input("digite numero de hombres: "))
numero_mujeres=int(input("digite numero de mujeres: "))
total_alumnos=numero_hombres+numero_mujeres
Porcentaje_hombres=(numero_hombres*100)/total_alumnos
Porcentaje_mujeres=(numero_mujeres*100)/total_alumnos
print("El porcentaje de hombres es: ",Porcentaje_hombres)
print("El porcentaje de mujeres es: ",Porcentaje_mujeres)

'''6) Realizar un algoritmo que calcule la edad de una persona.'''
Año_actual=int(input("digite fecha de actual: "))
Año_nacimiento=int(input("digite fecha de nacimiento: "))
edad=Año_actual-Año_nacimiento
print("La edad es: " , edad)

#parte2
'''1) Dada un cantidad en pesos, obtener la equivalencia en dólares, asumiendo que la unidad
cambiaría es un dato desconocido.'''

peso=int(input("digite pesos:"))
dolares=0.0002657
E_dolares= peso * dolares
print(E_dolares)

'''2) Leer un numero y escribir el valor absoluto del mismo.'''
numero= int(input("ingrese numero: "))
if numero < 0:
    numero= -numero
    print("valor absoluto es: ",numero)

else:
    numero >0
    print("valor absoluto es:",numero)

'''3) La presión, el volumen y la temperatura de una masa de aire se relacionan por la
formula: masa = (presión * volumen)/(0.37 * (temperatura + 460))'''

presion=int(input("ingrese presion: "))
volumen=int(input("ingrese volumen: "))
temperatura=int(input("ingrese temperatura: "))
masa=(presion * volumen)/(0.37 * (temperatura+460))
print("el valor de la masa es: ", masa)

'''4) Calcular el numero de pulsaciones que una persona debe tener por cada 10 segundos de
ejercicio, si la formula es:   num. pulsaciones = (220 - edad)/10'''


nombre=input("ingrese su nombre: ")
edad=int(input("ingrese edad: "))
num_pulsaciones= (220 - edad)/10
print("numero de pulsaciones es: ",num_pulsaciones)

'''5) Calcular el nuevo salario de un obrero si obtuvo un incremento del 25% sobre su salario
anterior.'''

Salario_anterior=int(input("ingrese salario anterior: "))
Salario_nuevo=(Salario_anterior*0.25) + Salario_anterior
print("Su salario nuevo es: ",Salario_nuevo)

'''6) En un hospital existen tres áreas: Ginecología, Pediatría, Traumatologia. El presupuesto
anual del hospital se reparte conforme a la sig. tabla:

rea Porcentaje del presupuesto
Ginecología 40%
Traumatologia 30%
Pediatría 30%'''

Presupuesto=int(input("ingrese presupuesto: "))
Ginecologia=Presupuesto*0.40
Traumatologia=Presupuesto*0.30
Pediatria=Presupuesto*0.30
print("El presupuesto para Ginecologia es: ",Ginecologia)
print("El presupuesto para Pediatria es: ",Pediatria)
print("El presupuesto para Traumatologia es: ",Traumatologia)

'''7) El dueño de una tienda compra un articulo a un precio determinado. Obtener el precio
en que lo debe vender para obtener una ganancia del 30%.'''

Valor_predeterminado= int(input("Ingrese valor predeterminado: "))
Precio_Vender=(Valor_predeterminado * 0.30) + Valor_predeterminado
print("Valor a vender es: ", Precio_Vender)


'''8) Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra los
tiempos obtenidos. Determinar el tiempo promedio que la persona tarda en recorrer la
ruta en una semana cualquiera.'''
Lunes=float(input("ingrese total de tiempo del lunes: "))
Miercoles=float(input("ingrese total de tiempo del miercoles: "))
Viernes=float(input("ingrese total de tiempo del viernes: "))
Promedio_semanal= (Lunes + Miercoles + Viernes) / 3
print("el tiempo promedio de la semana es: ",Promedio_semanal)


'''9) Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas
invierte una cantidad distinta. Obtener el porcentaje que cada quien invierte con
respecto a la cantidad total invertida.'''
socio1=int(input("socio numero 1 ingrese inversion:"))
socio2=int(input("socio numero 2 ingrese inversion:"))
socio3=int(input("socio numero 3 ingrese inversion:"))
Valor_total= socio1 + socio2 + socio3
porcentaje1= ( socio1 * 100) /Valor_total
porcentaje2= ( socio2 * 100) /Valor_total
porcentaje3= ( socio3 * 100) /Valor_total
print("el porcentaje del socio numero 1 es: ",porcentaje1)
print("el porcentaje del socio numero 2 es: ",porcentaje2)
print("el porcentaje del socio numero 3 es: ",porcentaje3)

'''10) Un alumno desea saber cual será su promedio general en las tres materias mas difíciles
que cursa y cual será el promedio que obtendrá en cada una de ellas. Estas materias se
evalúan como se muestra a continuación:'''

Examen=int(input("Ingrese nota examen Matematicas: "))
TareaMate1=int(input("Ingrese nota Tarea Matematicas 1: "))
TareaMate2=int(input("Ingrese nota Tarea Matematicas 2: "))
TareaMate3=int(input("Ingrese nota Tarea Matematicas 3: "))
Nota_Tareas=(TareaMate1+TareaMate2+TareaMate3)/3
Valor_examen=Examen*0.90
Valor_Tareas=Nota_Tareas*0.10
Nota_Matematicas=Valor_examen+Valor_Tareas
print("Promedio nota definitiva de Matematicas es: ",Nota_Matematicas)

Examen=int(input("Ingrese nota examen Fisica: "))
TareaFisica1=int(input("Ingrese nota Tarea Fisica 1: "))
TareaFisica2=int(input("Ingrese nota Tarea Fisica 2: "))
Nota_TareasF=(TareaFisica1+TareaFisica2)/2
Valor_examenF=Examen*0.80
Valor_TareasF=Nota_TareasF*0.20
Nota_Fisica=Valor_examenF+Valor_TareasF
print("Promedio nota definitiva de Fisica es: ",Nota_Fisica)

Examen=int(input("Ingrese nota examen Quimica: "))
TareaQuimica1=int(input("Ingrese nota Tarea Quimica 1: "))
TareaQuimica2=int(input("Ingrese nota Tarea Quimica 2: "))
TareaQuimica3=int(input("Ingrese nota Tarea Quimica 3: "))
Nota_TareasQ=(TareaQuimica1+TareaQuimica2+TareaQuimica3)/3
Valor_examenQ=Examen*0.85
Valor_TareasQ=Nota_TareasQ*0.15
Nota_Quimica=Valor_examenQ+Valor_TareasQ
print("Promedio nota definitiva de Quimica es: ",Nota_Quimica)
Promedio_Materias=(Nota_Quimica+Nota_Matematicas+Nota_Fisica)/3
print("Promedio nota definitiva de Matematicas es: ",Nota_Matematicas)
print("Promedio nota definitiva de Fisica es: ",Nota_Fisica)
print("Promedio nota definitiva de Quimica es: ",Nota_Quimica)
print("Promedio De las Materias es: ", Promedio_Materias)








