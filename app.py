from flask import Flask

app = Flask(__name__) # Padrão, sempre vai ser assim

#Definir uma rota raíz (página inicial) e a função que será executada ao requisitar
@app.route('/')
def hello_word():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True) 