from flask import Flask, render_template, jsonify
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def home():
    # Renderiza o arquivo HTML diretamente
    return render_template('python_poo_guide.html')

@app.route('/python-demo')
def python_demo():
    # Exemplo de função Python que será chamada pelo front-end
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_num = random.randint(1, 100)
    
    # Criando um objeto Python que será convertido para JSON
    response_data = {
        "message": "Esta mensagem veio do servidor Python!",
        "timestamp": current_time,
        "random_number": random_num,
        "status": "success"
    }
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)