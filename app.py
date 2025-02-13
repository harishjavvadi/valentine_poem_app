import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv
app = Flask(__name__)
CORS(app)  # Allows frontend to make API requests

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

@app.route("/")
def home():
    return render_template("index.html")  # Serves the main page

@app.route("/poem")
def poem_page():
    return render_template("poem.html")  # Serves the poem generator page

@app.route('/generate_poem', methods=['POST'])
def generate_poem():
    try:
        data = request.json
        name = data.get("name", "").strip()

        if not name:
            return jsonify({"error": "Name is required"}), 400

        # Construct prompt for Gemini API
        prompt = (
            f"Write a short, sweet, and wholesome Valentine's Day poem for {name}. "
            f"The poem should be lighthearted, family-friendly, and free of any explicit content."
        )

        # ✅ API request with "safetySettings" to reduce false positives
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "safetySettings": [
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"}
            ]
        }

        # Call Gemini API
        response = requests.post(
            f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",  #
            json=payload,
            headers={"Content-Type": "application/json"},
        )

        response_json = response.json()
        print("🔍 Gemini API Response:", response_json)  # Debugging step

        # Extract poem from response
        poem = response_json.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "").strip()

        if not poem:
            return jsonify({"error": "No poem generated from Gemini API"}), 500

        return jsonify({"poem": poem})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)