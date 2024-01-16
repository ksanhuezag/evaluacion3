from flask import render_template, request
from . import app

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Procesar los datos del formulario del Ejercicio 1
        # Calcular promedio, verificar condiciones y enviar resultados a la plantilla
        pass
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        # Procesar los datos del formulario del Ejercicio 2
        # Encontrar el nombre más largo y enviar resultados a la plantilla
        pass
    return render_template('ejercicio2.html')
