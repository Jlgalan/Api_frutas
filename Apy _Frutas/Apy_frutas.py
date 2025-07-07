from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para almacenar las frutas en memoria
frutas = []
next_id = 1  # Para generar IDs únicos

# Ruta principal donde se muestran y agregan frutas
@app.route('/', methods=['GET', 'POST'])
def index():
    global next_id

    if request.method == 'POST':  # Si se envía el formulario
        nombre = request.form['nombre']  # Tomamos el nombre de la fruta

        if not nombre:
            return "El nombre de la fruta es obligatorio", 400

        # Añadimos la nueva fruta con ID autogenerado
        frutas.append({"id": next_id, "nombre": nombre})
        next_id += 1

        return redirect(url_for('index'))  # Recargamos la página

    # Si es GET, mostramos la plantilla con la lista de frutas
    return render_template('index.html', frutas=frutas)

# Ruta para editar una fruta por su ID
@app.route('/editar/<int:id_fruta>', methods=['POST'])
def editar_fruta(id_fruta):
    nuevo_nombre = request.form.get('nombre')

    if not nuevo_nombre:
        return "El nombre es obligatorio", 400

    for fruta in frutas:
        if fruta['id'] == id_fruta:
            fruta['nombre'] = nuevo_nombre
            break
    else:
        return "Fruta no encontrada", 404

    return redirect(url_for('index'))

# Ruta para eliminar una fruta por su ID
@app.route('/eliminar/<int:id_fruta>', methods=['POST'])
def eliminar_fruta(id_fruta):
    global frutas
    frutas = [f for f in frutas if f['id'] != id_fruta]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)