from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    
    # Aqui é onde a lógica de resposta vai
    resposta = f"Você disse: {user_input}"

    return jsonify({'response': resposta})

if __name__ == '__main__':
    app.run(debug=True)
    