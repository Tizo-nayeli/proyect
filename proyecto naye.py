import tkinter as tk 
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import PhotoImage 
import random  

#Funciones para el Convertidor de Unidades tab3
def binario_a_decimal(binario):
    try:
        decimal = int(binario, 2)
        return decimal
    except ValueError:
        return "Entrada inválida, por favor ingrese un número binario válido."

def decimal_a_binario(decimal):
    try:
        binario = bin(int(decimal))[2:]
        return binario
    except ValueError:
        return "Entrada inválida, por favor ingrese un número decimal válido."

def newtons_a_libras(newtons):
    try:
        libras = float(newtons) * 0.224809
        return libras
    except ValueError:
        return "Entrada inválida, por favor ingrese un valor numérico válido."

def libras_a_newtons(libras):
    try:
        newtons = float(libras) / 0.224809
        return newtons
    except ValueError:
        return "Entrada inválida, por favor ingrese un valor numérico válido."

def ejecutar_conversion():
    opcion = combo_opciones.get()
    
    if opcion == "Binario a Decimal":
        binario = entrada.get()
        resultado = binario_a_decimal(binario)
    elif opcion == "Decimal a Binario":
        decimal = entrada.get()
        resultado = decimal_a_binario(decimal)
    elif opcion == "Newtons a Libras":
        newtons = entrada.get()
        resultado = "{:.4f} libras".format(newtons_a_libras(newtons))
    elif opcion == "Libras a Newtons":
        libras = entrada.get()
        resultado = "{:.4f} newtons".format(libras_a_newtons(libras))
    else:
        resultado = "Opción no válida."
    
    etiqueta_resultado.config(text="Resultado: " + str(resultado))

#calculo de areas tab 1
def calcular_area():
    opcion = AreaOption.get()
    
    if opcion == 1:  # Cuadrado
        lado = float(entry_lado.get())
        area = lado ** 2
        LabelOP2.config(text=f"El área del cuadrado de lado = {lado} es de AREA = {area:.2f}")
    
    elif opcion == 2:  # Rectángulo
        lado1 = float(entry_lado1.get())
        lado2 = float(entry_lado2.get())
        area = lado1 * lado2
        LabelOP2.config(text=f"El área del rectángulo de lado1 = {lado1} y lado2 = {lado2} es de AREA = {area:.2f}")
    
    elif opcion == 3:  # Triángulo
        base = float(entry_base.get())
        altura = float(entry_altura.get())
        area = (base * altura) / 2
        LabelOP2.config(text=f"El área del triángulo de base = {base} y altura = {altura} es de AREA = {area:.2f}")
    
    elif opcion == 4:  # Círculo
        radio = float(entry_radio.get())
        area = (radio ** 2) * 3.1416
        LabelOP2.config(text=f"El área del círculo de radio = {radio} es de AREA = {area:.2f}")
    
    elif opcion == 5:  # Polígono regular
        lados = int(entry_lados.get())
        longitud = float(entry_longitud.get())
        apotema = float(entry_apotema.get())
        area = (lados * longitud * apotema) / 2
        LabelOP2.config(text=f"El área del polígono de {lados} lados, longitud = {longitud} y apotema = {apotema} es de AREA = {area:.2f}")
    
    else:
        LabelOP2.config(text="Opción no válida.")

# calculadora basica tab2
def click_boton(valor):
    actual = entrada_calculadora.get()
    entrada_calculadora.delete(0, tk.END)
    entrada_calculadora.insert(tk.END, actual + str(valor))

def limpiar():
    entrada_calculadora.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada_calculadora.get())
        entrada_calculadora.delete(0, tk.END)
        entrada_calculadora.insert(tk.END, str(resultado))
    except:
        entrada_calculadora.delete(0, tk.END)
        entrada_calculadora.insert(tk.END, "Error")
        
def mostrar_frase_aleatoria():
    frases = [
        "¡La perseverancia es la clave del éxito!",
        "La creatividad es la inteligencia divirtiéndose.",
        "erick traicionero",
        "El único modo de hacer un gran trabajo es amar lo que haces.",
        "El futuro pertenece a quienes creen en la belleza de sus sueños."
    ]
    frase_aleatoria = random.choice(frases)
    etiqueta_frase.config(text=frase_aleatoria)

#creacion de la ventana con su tema
ventanita = ThemedTk(theme="black")
ventanita.title("Calculadora Científica")
ventanita.geometry("500x500")


notebook = ttk.Notebook(ventanita)
notebook.pack(pady=10, expand=True, fill='both')

# creamos los tab o pestañas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)

notebook.add(tab1, text="Opciones de Áreas")
notebook.add(tab2, text="Calculadora")
notebook.add(tab3, text="Convertidor de Unidades")
notebook.add(tab4, text="Equipo")

#configuracion del primer tab
AreaOption = tk.IntVar()

ttk.Radiobutton(tab1, text="Calcular área de Cuadrado", variable=AreaOption, value=1).pack(anchor='w')
entry_lado = ttk.Entry(tab1)
entry_lado.pack(pady=5, fill='x')

ttk.Radiobutton(tab1, text="Calcular área de Rectángulo", variable=AreaOption, value=2).pack(anchor='w')
entry_lado1 = ttk.Entry(tab1)
entry_lado1.pack(pady=5, fill='x')
entry_lado2 = ttk.Entry(tab1)
entry_lado2.pack(pady=5, fill='x')

ttk.Radiobutton(tab1, text="Calcular área de Triángulo", variable=AreaOption, value=3).pack(anchor='w')
entry_base = ttk.Entry(tab1)
entry_base.pack(pady=5, fill='x')
entry_altura = ttk.Entry(tab1)
entry_altura.pack(pady=5, fill='x')

ttk.Radiobutton(tab1, text="Calcular área de Círculo", variable=AreaOption, value=4).pack(anchor='w')
entry_radio = ttk.Entry(tab1)
entry_radio.pack(pady=5, fill='x')

ttk.Radiobutton(tab1, text="Calcular área de Polígono Regular", variable=AreaOption, value=5).pack(anchor='w')
entry_lados = ttk.Entry(tab1)
entry_lados.pack(pady=5, fill='x')
entry_longitud = ttk.Entry(tab1)
entry_longitud.pack(pady=5, fill='x')
entry_apotema = ttk.Entry(tab1)
entry_apotema.pack(pady=5, fill='x')

ttk.Button(tab1, text="Calcular Área", command=calcular_area).pack(pady=10)

LabelOP2 = ttk.Label(tab1, text="Resultado: ")
LabelOP2.pack(pady=5)

#configuracion del tab 2
entrada_calculadora = ttk.Entry(tab2, width=35)
entrada_calculadora.pack(pady=10, fill='x')

botones = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']

for i in range(0, len(botones), 4):
    frame_fila = ttk.Frame(tab2)
    frame_fila.pack(fill='x')
    
    for j in range(4):
        boton_texto = botones[i + j]
        if boton_texto == "=":
            b = ttk.Button(frame_fila, text=boton_texto, command=calcular)
        else:
            b = ttk.Button(frame_fila, text=boton_texto, command=lambda b=boton_texto: click_boton(b))
        b.pack(side='left', expand=True, fill='both', padx=5, pady=5)

frame_botones_adicionales = ttk.Frame(tab2)
frame_botones_adicionales.pack(fill='x')
ttk.Button(frame_botones_adicionales, text="Limpiar", command=limpiar).pack(side='left', expand=True, fill='both', padx=5, pady=5)

# configuracion del tab3
opciones = ["Binario a Decimal", "Decimal a Binario", "Newtons a Libras", "Libras a Newtons"]
combo_opciones = ttk.Combobox(tab3, values=opciones, state="readonly")
combo_opciones.pack(pady=5, fill='x')

entrada = ttk.Entry(tab3)
entrada.pack(pady=5, fill='x')

boton_convertir = ttk.Button(tab3, text="Convertir", command=ejecutar_conversion)
boton_convertir.pack(pady=5)

etiqueta_resultado = ttk.Label(tab3, text="Resultado: ")
etiqueta_resultado.pack(pady=5)

# configuracion del tab4

frame_hector = ttk.Frame(tab4)
frame_hector.pack(side='top', anchor='w')


imagen_hector = PhotoImage(file="C:/perifericos/E.png")  
ttk.Label(frame_hector, image=imagen_hector).pack(side='left', padx=5)


frame_info_hector = ttk.Frame(frame_hector)
frame_info_hector.pack(side='left', padx=5)

ttk.Label(frame_info_hector, text="Hector Gabriel Perez Atonal").pack(pady=2)
ttk.Label(frame_info_hector, text="Matrícula: 221403131").pack(pady=2)
ttk.Label(frame_info_hector, text="Número de lista: 15").pack(pady=2)


etiqueta_frase = ttk.Label(frame_info_hector, text="", wraplength=150)
etiqueta_frase.pack(pady=2)


boton_frase = ttk.Button(frame_info_hector, text="Mostrar Frase", command=mostrar_frase_aleatoria)
boton_frase.pack(pady=5)


frame_nayeli = ttk.Frame(tab4)
frame_nayeli.pack(side='top', anchor='w')

imagen_nayeli = PhotoImage(file="C:/perifericos/D.png") 
ttk.Label(frame_nayeli, image=imagen_nayeli).pack(side='left', padx=5)

frame_info_nayeli = ttk.Frame(frame_nayeli)
frame_info_nayeli.pack(side='left', padx=5)

ttk.Label(frame_info_nayeli, text="Nayeli Tizo Sanchez").pack(pady=2)
ttk.Label(frame_info_nayeli, text="Matrícula: 231403166").pack(pady=2)
ttk.Label(frame_info_nayeli, text="Número de lista: 22").pack(pady=2)
ttk.Label(frame_info_nayeli, text="Hola, soy Nayeli").pack(pady=2)
ttk.Label(frame_info_nayeli, text="Comentarios sobre mi:").pack(pady=2)
texto_nayeli = tk.Text(frame_info_nayeli, height=4, width=30)
texto_nayeli.pack(pady=2)


ventanita.mainloop()
