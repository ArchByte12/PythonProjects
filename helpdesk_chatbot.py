def chatbot():
    print("Student Helpdesk Chatbot")
    print("-" * 40)
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Bot: Thank you for chatting. Have a great day!")
            break

        elif "enrollment" in user_input:
            print("Bot: Enrollment for this semester will start on December 2, 2025.")

        elif "hi" in user_input or "hello" in user_input:
            print("Bot: Hello! How can I help you today?")

        elif "thank" in user_input:
            print("Bot: You’re welcome! Is there anything else I can help you with?")

        else:
            print("Bot: I’m sorry, I can only answer questions about enrollment right now.")

if __name__ == "__main__":
    chatbot()
