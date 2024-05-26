from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

app = Flask(__name__)
model = SentenceTransformer('sentence-transformers/LaBSE')

@app.route(rule='/', methods=['POST'])
def get_embeddings():
    request_data = request.get_json()
    target_words = request_data.get('words')

    if not target_words:
        return jsonify({'error': 'No words provided'}), 400
    try:
        if isinstance(target_words, str):
            target_words = [target_words]
        elif not isinstance(target_words, list):
            raise ValueError('words must be a string or a list of strings')

        embeddings = model.encode(target_words)
        result = {}
        for word, embedding in zip(target_words, embeddings):
            result[word] = embedding.tolist()
        return jsonify({'embeddings': result})

    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run()
