from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)
#Modelagem
#Produto(id, name, price, description)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Integer é o tipo de dado INTEIRO
    name = db.Column(db.String(120), nullable=False) #Quer obrigrar que todo produto tenha nome. String vc limita o tamanho do texto
    price = db.Column(db.Float, nullable=False) #É obrigatorio todo produto ter o preço. Float é usado para valores decimais
    description = db.Column(db.Text, nullable=True) #Descrição é opcional. Text é ILIMITADO, difetente da String aonde vc tem limitações


#Definir uma rota raíz (página inicial) e a função que será executada ao requisitar
@app.route('/')
def hello_word():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True) 