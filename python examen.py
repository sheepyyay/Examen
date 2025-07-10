#donde los productos son listados

productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
    'FS1230HD': ['HP', 15.6, '4GB', 'SSD', '256GB', 'Intel Celeron', 'integrada']
}
#aqui estaria el stock

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 2],
    '123FHD': [298090, 2],
    '342FHD': [444990, 7],
    'GF75HD': [499990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0]
}
#la variable de marca

def stock_marca(marca):
    marca = marca.lower()
    for modelo in productos:
        if productos[modelo][0].lower() == marca:
            print(f"{modelo}: {stock[modelo][1]} unidades")

#variable de precio

def busqueda_precio(p_min, p_max):
    try:
        p_min = int(p_min)
        p_max = int(p_max)
        lista_resultados = []

        for modelo in stock:
            precio, cantidad = stock[modelo]
            if p_min <= precio <= p_max and cantidad > 0:
                marca = productos[modelo][0]
                lista_resultados.append(f"{marca}--{modelo}")

#los resultados que seran dictados dependiendo de que cosa sea ingresada

        if lista_resultados:
            for item in sorted(lista_resultados):
                print(item)
        else:
            print("No hay notebooks en ese rango de precios.")
    except:
        print("Debe ingresar valores enteros!!")

#actualizar precio 

def actualizar_precio(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0] = nuevo_precio
        return True
    else:
        return False                    

#el menu completo, con todo lo anterior implementado

while True:
    print("\n*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")

    opcion = input("Ingrese opción: ")

    if opcion == "1":
        marca = input("Ingrese la marca: ")
        stock_marca(marca)

    elif opcion == "2":
        p_min = input("Ingrese precio mínimo: ")
        p_max = input("Ingrese precio máximo: ")
        busqueda_precio(p_min, p_max)

    elif opcion == "3":
        modelo = input("Ingrese modelo: ")
        try:
            nuevo_precio = int(input("Ingrese nuevo precio: "))
            actualizado = actualizar_precio(modelo, nuevo_precio)
            if actualizado:
                print("Precio actualizado!!")
            else:
                print("El modelo no existe!!")
        except:
            print("Debe ingresar un precio válido.")

        respuesta = input("¿Desea actualizar otro precio? (si/no): ").lower()
        if respuesta != "si":
            continue

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Debe seleccionar una opción válida!!")
