from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/ask-planner", methods=["POST"])
def ask_planner():
    task = request.json.get("task", "")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Atau "gpt-4" kalau kamu pakai GPT-4
        messages=[
            {"role": "system", "content": "Kamu adalah Niu Niu, asisten lucu dan manja yang bantu Kapten Nano membuat planner harian."},
            {"role": "user", "content": task}
        ]
    )
    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
