print("Welcome to Shop Chatbot")
print("Type 'bye' to exit\n")

while True:

    user = input("You: ").lower()

    # Greetings
    if user == "hi" or user == "hello":

        print("Bot: Hello! How can I help you?")

    # Product Price
    elif "laptop" in user:

        print("Bot: Laptop price is Rs.50000")

    elif "mobile" in user:

        print("Bot: Mobile price is Rs.20000")

    elif "headphones" in user:

        print("Bot: Headphones price is Rs.2000")

    # Shop timing
    elif "time" in user or "open" in user:

        print("Bot: Shop is open from 9 AM to 9 PM")

    # Location
    elif "location" in user or "address" in user:

        print("Bot: Our shop is in Nashik")

    # Contact
    elif "contact" in user or "phone" in user:

        print("Bot: Contact number is 9876543210")

    # Exit
    elif user == "bye":

        print("Bot: Thank you! Visit again.")
        break

    # Default reply
    else:

        print("Bot: Sorry, I don't understand.")