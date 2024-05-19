# Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.
# Si compra+ de 12  unidades (y hasta 24 unidades), el costo:  descuento del 10%.
# Si compra más de 24 unidades, el descuento es del 15%. 
# La promoción de jubilados es sumarle un 10% de descuento extra.
# 1000 pesos la unidad.

valor_leche = 1000
cantidadUnidades = int(input("Ingrese la cantidad de unidades que desea comprar: "))
jubilado = int(input("Eres jubilado? Si:1 / No:2  "))
precio_sin_descuento = cantidadUnidades * valor_leche

descuento_no_jubilado1 = precio_sin_descuento * 0.90
descuento_no_jubilado2 = precio_sin_descuento * 0.85

descuento_jubilado1 = precio_sin_descuento * 0.90
descuento_jubilado2 = precio_sin_descuento * 0.80
descuento_jubilado3 = precio_sin_descuento * 0.75


if jubilado == 1: 
 if cantidadUnidades <12:
   print(f"El precio final es ${descuento_jubilado1}") 
 else: 
   if cantidadUnidades >12 and cantidadUnidades <=24:
          print(f"El precio final es ${descuento_jubilado2}")
   else: 
          print(f"El precio final es ${descuento_jubilado3}")
else:   
 if cantidadUnidades <=12: 
      print(f"El total es ${precio_sin_descuento}")
 else: 
    if cantidadUnidades >12 and cantidadUnidades <=24:
       print(f"El total es ${descuento_no_jubilado1}")
    else:
       print(f"El total es ${descuento_no_jubilado2}")





      
