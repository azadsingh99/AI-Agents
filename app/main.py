from services.llm import ask_agent

# Session memory
chat_history = []

while True:

    question = input("\nAsk your agent: ")

    if question.lower() == "exit":
        break

    # Send memory + question
    answer = ask_agent(question, chat_history)

    print("\nAgent:", answer)

    # Save conversation
    chat_history.append({
        "user": question,
        "assistant": answer
    })