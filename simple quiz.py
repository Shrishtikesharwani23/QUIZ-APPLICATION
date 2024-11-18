import random

# Dictionary to store users (username as key, password as value)
users = {}

# Questions pool for Python, Java, and C++
questions = [
    # Python Questions
    {"question": "What is the output of print(2 * 3)?", "choices": ["1. 5", "2. 6", "3. 8"], "answer": "2"},
    {"question": "Which of the following is a mutable data type in Python?", "choices": ["1. List", "2. String", "3. Tuple"], "answer": "1"},
    {"question": "What does 'def' keyword do in Python?", "choices": ["1. Defines a function", "2. Declares a variable", "3. Imports a library"], "answer": "1"},
    {"question": "Which of the following is the correct syntax for a while loop in Python?", "choices": ["1. while (condition):", "2. while condition", "3. while {condition}"], "answer": "1"},
    {"question": "What is the default return value of a function in Python that does not explicitly return anything?", "choices": ["1. None", "2. 0", "3. False"], "answer": "1"},
    {"question": "How do you create a set in Python?", "choices": ["1. set = {}", "2. set = []", "3. set = ()"], "answer": "1"},
    {"question": "What is the purpose of the 'self' parameter in Python methods?", "choices": ["1. It refers to the current instance of the class", "2. It refers to the previous instance of the class", "3. It is not used in Python"], "answer": "1"},
    {"question": "How can you remove an item from a list in Python?", "choices": ["1. list.remove(item)", "2. list.delete(item)", "3. list.removeAt(item)"], "answer": "1"},
    {"question": "What is the output of len([1, 2, 3])?", "choices": ["1. 3", "2. 2", "3. 4"], "answer": "1"},
    {"question": "Which of the following is NOT a valid Python identifier?", "choices": ["1. variable1", "2. 1variable", "3. variable_1"], "answer": "2"},
    # Java Questions
    {"question": "What is the default value of an int in Java?", "choices": ["1. 0", "2. null", "3. undefined"], "answer": "1"},
    {"question": "Which of these is a valid Java class?", "choices": ["1. public class MyClass", "2. class MyClass", "3. MyClass public class"], "answer": "1"},
    {"question": "Which method is the entry point for any Java application?", "choices": ["1. main", "2. start", "3. run"], "answer": "1"},
    {"question": "Which keyword is used to create a subclass in Java?", "choices": ["1. extends", "2. implements", "3. super"], "answer": "1"},
    {"question": "Which method is used to get the length of an array in Java?", "choices": ["1. array.size()", "2. array.length", "3. array.length()"], "answer": "2"},
    {"question": "Which of these is a valid data type in Java?", "choices": ["1. int", "2. number", "3. float64"], "answer": "1"},
    {"question": "What is the scope of a static variable in Java?", "choices": ["1. Global", "2. Local to the class", "3. Local to the method"], "answer": "2"},
    {"question": "Which of these is used for object creation in Java?", "choices": ["1. new", "2. create", "3. object"], "answer": "1"},
    {"question": "Which of these is NOT a valid Java access modifier?", "choices": ["1. public", "2. private", "3. secret"], "answer": "3"},
    {"question": "Which collection class in Java allows only unique elements?", "choices": ["1. List", "2. Set", "3. Map"], "answer": "2"},
    # C++ Questions
    {"question": "What is the correct syntax to declare a pointer in C++?", "choices": ["1. int ptr", "2. int ptr", "3. *int ptr"], "answer": "1"},
    {"question": "Which of these is used for memory allocation in C++?", "choices": ["1. malloc()", "2. new", "3. alloc()"], "answer": "2"},
    {"question": "What is the correct way to comment in C++?", "choices": ["1. // This is a comment", "2. /* This is a comment */", "3. Both of the above"], "answer": "3"},
    {"question": "Which of these is the correct syntax for defining a function in C++?", "choices": ["1. void function()", "2. function void()", "3. def function()"], "answer": "1"},
    {"question": "Which of the following is a valid way to declare a string in C++?", "choices": ["1. string str;", "2. str string;", "3. char[] str;"], "answer": "1"},
    {"question": "Which function is used to get the length of a C++ string?", "choices": ["1. length()", "2. size()", "3. getLength()"], "answer": "2"},
    {"question": "What is the default access specifier for a class in C++?", "choices": ["1. public", "2. private", "3. protected"], "answer": "2"},
    {"question": "Which keyword is used to create an object in C++?", "choices": ["1. new", "2. create", "3. class"], "answer": "1"},
    {"question": "What is the use of the 'virtual' keyword in C++?", "choices": ["1. For memory management", "2. To allow method overriding", "3. To declare a constant"], "answer": "2"},
    {"question": "Which of these operators is used for dynamic memory deallocation in C++?", "choices": ["1. delete", "2. free", "3. deallocate"], "answer": "1"},
]

# Registration function
def register():
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Try a different one.")
        return
    password = input("Enter a password: ")
    users[username] = password
    print("Registration successful!")

# Login function
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print(f"Welcome {username}!")
        return True
    else:
        print("Invalid username or password.")
        return False

# Quiz function
def attempt_quiz():
    score = 0
    selected_questions = random.sample(questions, 5)  # Select 5 random questions
    for q in selected_questions:
        print(q["question"])
        for choice in q["choices"]:
            print(choice)
        answer = input("Enter your choice (1/2/3): ")
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}\n")
    print(f"Your final score is: {score}/5")

# Main function to drive the program
def main():
    while True:
        print("\nWelcome to the Quiz App")
        print("1. Register")
        print("2. Login")
        print("3. Attempt Quiz")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            if login():
                print("Login successful!")
            else:
                print("Login failed.")
        elif choice == "3":
            attempt_quiz()
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()