from flask import Flask, request, jsonify
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

@app.route('/api/products/add', methods=['POST']) #Rota com o mesmo nome que no caso está no Postman
def add_product(): # Função que será executada ao requisitar a rota
    data = request.json #Pega o corpo da requisição que está em JSON
    if 'name' in data and 'price' in data: # Verifica se os campos 'name' e 'price' estão presentes no JSON
        product = Product(name=data['name'], price=data['price'], description=data.get('description', ''))
        db.session.add(product) # Adiciona o produto à sessão do banco de dados
        db.session.commit() # Salva o produto no banco de dados
        return jsonify({'message': 'Product added successfully!'}) 
    return jsonify({'message': 'Invalid product data'}), 400

@app.route('/api/products/delete/<int:products_id>', methods=['DELETE'])# Rota para deletar um produto
def delete_product(products_id):
    # Recuperar o produto da base de dados
    product = Product.query.get(products_id)
    # Verificar se o produto existe
    # Se não existir, retornar erro 404
    product = Product.query.get(products_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully!'}) 
    return jsonify({'message': 'Product not found'}), 404

#Definir uma rota raíz (página inicial) e a função que será executada ao requisitar
@app.route('/')
def hello_word():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True) 