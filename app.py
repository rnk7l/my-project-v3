print("أهلاً بك في مشروعنا البرمجي!")
user_name = input("enter your name: ")

if user_name.strip() == "":
    user_name = "guest"
    print("no name entered. defaulting to guest.")

print(f"hello, {user_name}!")
