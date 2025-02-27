from agent import chat_with_ai

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    response = chat_with_ai(user_input)
    print(f"AI: {response}")
