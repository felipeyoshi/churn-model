from flask import Flask, request, jsonify
import mlflow.pyfunc

app = Flask(__name__)

# Carregar o modelo do MLflow
logged_model = 'runs:/c942840a43c24c2289a1b808e41ff80e/modelo_regressao_logistica'
# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Obter os dados da requisição
            data = request.get_json()
            # Assegurar que os dados estão no formato correto
            if 'data' in data:
                # Converter os dados para o formato adequado
                input_data = data['data']
                # Realizar a previsão
                predictions = loaded_model.predict(input_data)
                # Retornar a resposta
                return jsonify(predictions.tolist())
            else:
                return jsonify({"error": "Dados inválidos"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)