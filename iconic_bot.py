import random
from datetime import datetime

print("=" * 40)
print("🤖 Welcome to Mini Iconic Bot")
print("Made by Rashmi")
print("=" * 40)

name = input("Enter your name: ")

while True:
    print("\n===== MENU =====")
    print("1. Chat")
    print("2. Calculator")
    print("3. Percentage Calculator")
    print("4. Date & Time")
    print("5. Joke")
    print("6. Motivational Quote")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        msg = input("You: ").lower()

        if "hi" in msg or "hello" in msg:
            print("Bot: Hello,", name + "!")
        elif "how are you" in msg:
            print("Bot: I am fine. Thanks for asking!")
        elif "bye" in msg:
            print("Bot: Goodbye! Have a nice day.")
        else:
            replies = [
                "Interesting!",
                "Tell me more.",
                "I'm still learning.",
                "That's nice!"
            ]
            print("Bot:", random.choice(replies))

    elif choice == "2":
        try:
            a = float(input("First Number: "))
            op = input("Operator (+ - * /): ")
            b = float(input("Second Number: "))

            if op == "+":
                print("Answer =", a + b)
            elif op == "-":
                print("Answer =", a - b)
            elif op == "*":
                print("Answer =", a * b)
            elif op == "/":
                if b == 0:
                    print("Cannot divide by zero.")
                else:
                    print("Answer =", a / b)
            else:
                print("Invalid operator.")
        except:
            print("Invalid input.")

    elif choice == "3":
        try:
            obtained = float(input("Marks Obtained: "))
            total = float(input("Total Marks: "))
            print("Percentage =", round((obtained / total) * 100, 2), "%")
        except:
            print("Invalid input.")

    elif choice == "4":
        now = datetime.now()
        print("Date:", now.strftime("%d-%m-%Y"))
        print("Time:", now.strftime("%I:%M:%S %p"))

    elif choice == "5":
        jokes = [
            "Why don't programmers like nature? It has too many bugs!",
            "Why did the computer go to the doctor? Because it had a virus!",
            "Why was the math book sad? Because it had too many problems!"
        ]
        print(random.choice(jokes))

    elif choice == "6":
        quotes = [
            "Believe in yourself.",
            "Dream big and work hard.",
            "Practice makes progress.",
            "Success begins with small steps."
        ]
        print(random.choice(quotes))

    elif choice == "7":
        print("Thank you for using Mini Iconic Bot!")
        break

    else:
        print("Invalid choice. Try again.")
