from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- Chatbot logic ---
def get_response(user_input):
    user_input = user_input.lower()

    if "enrollment" in user_input:
        return "Enrollment for this semester will start on December 2, 2025."
    elif "hi" in user_input or "hello" in user_input:
        return "Hello! How can I help you today?"
    elif "thank" in user_input:
        return "You’re welcome! Is there anything else I can help you with?"
    elif user_input in ["bye", "exit", "quit"]:
        return "Thank you for chatting. Have a great day!"
    else:
        return "I’m sorry, I can only answer questions about enrollment right now."

# --- Routes ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"]
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
