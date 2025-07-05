from flask import Flask, request, jsonify, render_template
import os
import tempfile
from extractor import extract_fields_from_doc

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and file.filename.endswith('.docx'):
        temp_path = os.path.join(tempfile.gettempdir(), file.filename)
        file.save(temp_path)

        try:
            result = extract_fields_from_doc(temp_path)
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
    else:
        return jsonify({"error": "Invalid file type. Only DOCX files accepted"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)