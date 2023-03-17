from flask import Flask, render_template, request
import banco

app = Flask(__name__)

@app.route('/')
def index():
    table_info = banco.get_collumns_name('servidores')
    table_data = banco.get_all()
    return render_template('index.html', 
                           table_data=table_data,
                           table_info=table_info)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        print("post recebido")
        return 200
    return "<h1> faça seu cadastro aqui </h1>"

@app.route('/centro/<nome>')
def centro_nome(nome):
    table_info = banco.get_collumns_name('servidores')
    table_data = banco.get_center(nome)
    return render_template('index.html', 
                           table_data=table_data,
                           table_info=table_info)


if __name__ == '__main__':
    app.run(debug=True)