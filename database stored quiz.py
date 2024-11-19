import mysql.connector
import random

# Database Connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",      # Replace with your MySQL host
        user="root",           # Replace with your MySQL username
        password="yourpassword",  # Replace with your MySQL password
        database="quiz_app"    # Replace with your MySQL database name
    )

# Database setup
def create_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        enrollment VARCHAR(50) UNIQUE NOT NULL,
        contact_number VARCHAR(15) NOT NULL,
        password VARCHAR(100) NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        question_id INT AUTO_INCREMENT PRIMARY KEY,
        question_text TEXT NOT NULL,
        option_a VARCHAR(255) NOT NULL,
        option_b VARCHAR(255) NOT NULL,
        option_c VARCHAR(255) NOT NULL,
        option_d VARCHAR(255) NOT NULL,
        correct_option CHAR(1) NOT NULL,
        language VARCHAR(50) NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        score_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        score INT NOT NULL,
        language VARCHAR(50) NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    );
    """)

    conn.commit()
    conn.close()

# Insert predefined questions
def insert_sample_questions():
    conn = get_connection()
    cursor = conn.cursor()

    questions = [
        # Python Questions
        ("What is the output of 2 ** 3 in Python?", "6", "8", "9", "7", "b", "python"),
        ("Which keyword is used to define a function in Python?", "function", "def", "lambda", "fun", "b", "python"),
        ("What is a correct way to create a list?", "list = []", "list()", "list = {}", "list = ()", "a", "python"),
        ("What does the len() function do?", "Find the length of a string", "Find the length of a list", "Both a and b", "None of the above", "c", "python"),
        ("What is the output of print('Hello' + 'World')?", "HelloWorld", "Hello World", "Error", "None", "a", "python"),
        ("Which of these is a correct data type in Python?", "String", "Integer", "Both a and b", "None", "c", "python"),
        ("What is the result of 10 // 3 in Python?", "3.3", "3", "4", "Error", "b", "python"),
        ("Which of these is not a Python library?", "NumPy", "Pandas", "React", "Matplotlib", "c", "python"),
        ("Which method is used to get user input?", "scan()", "input()", "read()", "write()", "b", "python"),
        ("What is the default Python version suffix?", ".py", ".pyc", ".pyx", ".pyz", "a", "python"),
        
        # Java Questions
        ("Which of these is not a Java keyword?", "public", "static", "String", "void", "c", "java"),
        ("Java is:", "Object-Oriented", "Platform Independent", "Secure", "All of the above", "d", "java"),
        ("What is the size of int in Java?", "4 bytes", "2 bytes", "8 bytes", "Depends on OS", "a", "java"),
        ("Which method is used to print in Java?", "console.log()", "print()", "System.out.println()", "echo()", "c", "java"),
        ("Which of these is the correct syntax to create an object in Java?", "new Object();", "Object obj = new Object();", "Object obj();", "Object obj = new Object;", "b", "java"),
        ("What does JVM stand for?", "Java Variable Machine", "Java Virtual Machine", "Java Versatile Machine", "None", "b", "java"),
        ("Which of these is not a primitive type in Java?", "String", "int", "float", "char", "a", "java"),
        ("What is the default value of an int in Java?", "0", "null", "undefined", "None", "a", "java"),
        ("Which operator is used for inheritance in Java?", ":", "::", "extends", "inherits", "c", "java"),
        ("Which loop is used for iteration in Java?", "foreach", "for", "while", "All of the above", "d", "java"),

        # C++ Questions
        ("Which of the following is a valid C++ comment?", "// comment", "/* comment", "# comment", "All of the above", "a", "c++"),
        ("What is the output of 'cout << 2 + 3;' in C++?", "5", "2 + 3", "Error", "None", "a", "c++"),
        ("Which of these is a correct syntax to include a header file in C++?", "#include <filename>", "#include filename", "include <filename>", "#include [filename]", "a", "c++"),
        ("Which of these is not a C++ keyword?", "class", "struct", "main", "None of the above", "c", "c++"),
        ("Which operator is used to allocate memory in C++?", "malloc", "new", "alloc", "allocate", "b", "c++"),
        ("What is the size of a float in C++?", "4 bytes", "2 bytes", "8 bytes", "None", "a", "c++"),
        ("What is the default return type of the main() function in C++?", "void", "int", "string", "None", "b", "c++"),
        ("Which of these supports multiple inheritance in C++?", "class", "struct", "Both a and b", "None", "c", "c++"),
        ("What is the output of cout << 10/3;?", "3.33", "3", "4", "Error", "b", "c++"),
        ("Which is used for exception handling in C++?", "catch", "try", "throw", "All of the above", "d", "c++"),
    ]

    for question in questions:
        cursor.execute("""
        INSERT INTO questions (question_text, option_a, option_b, option_c, option_d, correct_option, language)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """, question)

    conn.commit()
    conn.close()
    print("Sample questions added successfully!")


def register_user():
    conn = get_connection()
    cursor = conn.cursor()

    name=input("enter your name:")
    enrollment=input("enter your enrollment number:")
    contact_number=input("enter your contact number:")
    password=input("enter your password:")

    cursor.execute(""" INSERT INTO USERS(name,enrollment,contact_number,password)
             VALUES(%s,%s,%s,%s);
                   """,(name,enrollment,contact_number,password))
    
    conn.commit()
    conn.close()
    print("Registration successfully!")


def login_user():
    conn = get_connection()
    cursor = conn.cursor()

    enrollment=input("enter your enrollment number:")
    password=input("enter your password:")

    cursor.execute(""" SELECT user_id FROM users WHERE enrollment =%s AND password =%s;
                   """,(enrollment,password))
    
    result = cursor.fetchone()
    conn.close()

    if result:
        print("Login successful!")
        return result[0]
    else:
        print("Invalid enrollment number or password.")
        return None
    

def show_results(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""SELECT score,language FROM scores WHERE user_id =%s;
                   """,(user_id))
    results = cursor.fetchall()

    if not results:
        print("No quiz results found.")
    else:
        print("\nYour Previous Quiz Result:")
        for result in results:
            print(f"Language: {result[1]}, Score: {result[0]}/5")

            conn.close()    


# Take quiz
def take_quiz(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    language = input("Select quiz language (Python/Java/C++): ").lower()
    cursor.execute("SELECT * FROM questions WHERE language = %s ORDER BY RAND() LIMIT 5;", (language,))
    questions = cursor.fetchall()

    if not questions:
        print(f"No questions available in {language.capitalize()}.")
        return

    score = 0
    
    for question in questions:
        print(f"\n{question[1]}")
        print(f"a) {question[2]}  b) {question[3]}  c) {question[4]}  d) {question[5]}")
        answer = input("Your answer (a/b/c/d): ").lower()
        
        if answer == question[6].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question[6]}.")

    # Store the score
    cursor.execute("""
    INSERT INTO scores (user_id, score, language)
    VALUES (%s, %s, %s);
    """, (user_id, score, language))
    conn.commit()
    conn.close()
    print(f"\nYour final score is: {score}/5")

# Main menu
def main():
    create_database()
    insert_sample_questions()  # Add sample questions if needed
    print("Welcome to the Quiz App with MySQL!")

    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            user_id = login_user()
            if user_id:
                take_quiz(user_id)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "_main_":
    main()
