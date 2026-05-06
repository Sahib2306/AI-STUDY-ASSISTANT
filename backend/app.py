import os
from flask import Flask, request, jsonify
from flask_cors import CORS

from backend.loader import load_pdf
from backend.splitter import split_text
from backend.embeddings import get_embeddings
from backend.vector_store import create_vector_store
from backend.retriever import get_retriever
from backend.rag_pipeline import answer_question
from backend.llm import load_llm

app = Flask(__name__)
CORS(app)

# Global state for the RAG pipeline
vector_store = None
retriever = None
llm = load_llm()

@app.route("/upload", methods=["POST"])
def upload():
    global vector_store, retriever
    
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
        
    file = request.files["file"]
    
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
        
    if file and file.filename.endswith(".pdf"):
        os.makedirs("data", exist_ok=True)
        file_path = "data/temp.pdf"
        file.save(file_path)
        
        try:
            documents = load_pdf(file_path)
            chunks = split_text(documents)
            embeddings = get_embeddings()
            vector_store = create_vector_store(chunks, embeddings)
            retriever = get_retriever(vector_store)
            
            return jsonify({"message": "PDF uploaded and processed successfully!"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    return jsonify({"error": "Invalid file format, please upload a PDF"}), 400

@app.route("/ask", methods=["POST"])
def ask():
    global retriever, llm
    
    if not retriever:
        return jsonify({"answer": "Please upload a PDF first."}), 400
        
    data = request.json
    question = data.get("question")
    
    if not question:
        return jsonify({"answer": "Please ask a question."}), 400
        
    try:
        answer = answer_question(question, retriever, llm)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"answer": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)