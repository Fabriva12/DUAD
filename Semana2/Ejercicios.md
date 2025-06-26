Ejercicios

1. Cree un pseudocódigo que pida al usuario el `precio de un producto`, calcule su descuento y muestre el precio final teniendo en cuenta eso:
    1. Si el precio es inferior a 100, el descuento es del 2%.
    2. Si el precio es mayor o igual a 100, el descuento es del 10%.
    3. *Ejemplos*:
        1. 120 → 108
        2. 40 → 39.2
1. Inicio
2. Definir `precio_producto`
3. Definir `descuento`
4. Definir `precio_final`
5. Mostrar ¨Ingresar precio producto¨
6. Pedir `precio_producto`
7. Si (`precio_producto` <100) entonces:

         a.`descuento`=`precio_producto`*0.02

1.  Sino

          a.Si (`precio_producto>100`) entonces:

              i.`descuento`=`precio_producto`*0.1

          b.FinSi

1. FinSi
2. `precio_final`=`precio_producto`-`descuento`
3. Mostrar ¨precio_final es¨
4. Mostrar `precio_final`
5. Fin

1. Crear un pseudocódigo que pida al usuario un `tiempo en segundos` y calcule si es menor o mayor que 10 minutos. Si es menor, muestra cuántos segundos se tardaría en llegar a los 10 minutos. Si es mayor, muestra*"Mayor*". Si es exactamente igual, muestra*"Igual*".
    1. *Ejemplos*:
        1. 1040 → Mayor
        2. 140 → 460
        3. 600 → Igual
        4. 599 → 1

 1. Inicio

1. Definir `tiempo_en_segundos`
2. Definir `mayor`
3. Definir `igual`
4. Definir `segundos_faltantes`
5. Mostrar "Introducir tiempo en segundos
6. Solicitar `tiempo_en_segundos`
7. Si (`tiempo_en_segundos` <600) entonces:

         a. 600 -`tiempo_en_segundos` = `segundos_faltantes`

         b. Mostrar`segundos_faltantes`

 9. Sino

        a. Si (`tiempo_en_segundos>600`) entonces:

              i. `tiempo_en_segundos`= `mayor`

        b. Mostrar `mayor`.

        c. FinSi

10. Sino 

      a. Si (`time_in_seconds=600`) entonces:

            i. `tiempo_en_segundos` = `igual`. 

      b. Mostrar `igual`.

      c.FinSi

1. FinSi
2. Fin

3.Crea un algoritmo que pida al usuario un número, y realice una suma de cada número desde 1 hasta ese número introducido. A continuación, muestre el resultado de la suma.

1. 3 → 6 (1 + 2 + 3)
2. 5 → 15 (1 + 2 + 3 + 4 + 5)
3. 12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)

1. Inicio
2. Definir `número`
3. Definir `resultado`
4. Mostrar ¨ ingresar número¨
5. Pedir `número`
6. `resultado` = `número`*(número+1)/2
7. Mostrar ¨resultado de la suma¨
8. Mostrar `resultado`
9. Fin

4.Crea un algoritmo que pida al usuario 2 números, los almacene en dos variables diferentes`(primera` y `segunda`) y los ordene de menor a mayor en dichas variables.

1. Ejemplos:
    1. A: 56, B: 32 → A: 32, B: 56.
    2. A: 24, B: 76 → A: 24, B: 76.
    3. A: 45, B: 12 → A: 12, B: 45

1. Inicio 
2. Definir `primero`
3. Definir `segundo`
4. Definir `A`
5. Definir `B`
6. Mostrar ¨ingresar primer numero¨
7. Pedir `primero`
8. Mostrar ¨ingresar segundo numero¨
9. Pedir `segundo`
10. Si ( `primero`> `segundo` ) entonces:

        a. `primero` = `A`

        b. `segundo`= `B`

1. Sino

        a. Si ( `primero`< `segundo`) entonces:

           i. `primero` = `B`

           ii. `segundo` = `A`

        b. FinSi

1. FinSi
2. Mostrar ¨el orden los numeros es ¨
3. Mostrar `A` y `B`
4. Fin

5.Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s. Recuerda que `1 km == 1000m` y `1 hora == 60 minutos * 60 segundos`.

1. *Ejemplos*:
    1. 73 → 20.27
    2. 50 → 13.88
    3. 120 → 33.33

1. Inicio
2. Definir `velocidad_km/h`
3. Definir `velocidad_m/s`
4. Mostrar ¨Igrese velocidad en km/h
5. Pedir `velocidad_km/h`
6. `velocidad_m/s` = `velocidad_km/h`/3.6 
7. Mostrar ¨la velocidad en m/s es¨
8. Mostrar `velocidad_m/s`
9. Fin

6..Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, ingresando 1 si es mujer o 2 si es hombre, y muestre al final el porcentaje de mujeres y hombres.

1. *Ejemplos*:
    1. 1, 1, 1, 2, 2, 2 → 50% mujeres y 50% hombres
    2. 1, 1, 2, 2, 2, 2 → 33.3% mujeres y 66.6% hombres
    3. 1, 1, 1, 1, 1, 2 → 84.4% mujeres y 16.6% hombres

1. Inicio
2. Definir `h`
3. Definir `m`
4. Definir `contador`
5. Definir `contador_m`
6. Definir `contador_h`
7. Definir `porcentaje_mujeres`
8. Definir `porcentaje_hombres`
9. `contador`=0
10. Mientras  `contador`<= 6) entonces:

         a.Mostrar ¨igrese m si es mujer o h si es hombre¨

         b.Pedir `m` o `h`

1. Si (ingreso `m`) entonces:

         a.`contador_m` + 1

         b. `contador` =`contador` +1

1. Sino 

         a.Si (ingreso `h`) entonces:

            i.`contador_h` +1

            ii. `contador` =`contador` +1

         b.FinSi

1. FinSi
2. FinMientras
3. `porcentaje_mujeres`=`contador_m`/6 * 100
4. `porcentaje_hombres`=`contador_h`/6 * 100
5. Mostrar ¨ el porcentajes de mujeres y hombres es¨
6. Mostrar `porcentaje_mujeres` y `porcentaje_hombres`
7. Fin