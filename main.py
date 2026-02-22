from database import init_db, log_activity
from auth import login, create_user
from plugin_loader import load_plugins
from analytics import show_analytics
from config import VERSION

def main():
    init_db()

    print(VERSION)
    print("1 - Register")
    print("2 - Login")
    choice = input("Select: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        role = input("Role (admin/student/researcher): ")
        create_user(username, password, role)
        print("User created.")
        return

    username = input("Username: ")
    password = input("Password: ")

    role = login(username, password)

    if not role:
        print("Login failed.")
        return

    plugins = load_plugins()

    while True:
        print("\nAvailable Tools:")
        for i, name in enumerate(plugins.keys()):
            print(f"{i+1} - {name}")

        print("A - Analytics (admin only)")
        print("Q - Exit")

        choice = input("Select: ")

        if choice.lower() == "q":
            break

        elif choice.lower() == "a" and role == "admin":
            show_analytics()

        else:
            try:
                tool_name = list(plugins.keys())[int(choice)-1]
                plugins[tool_name].run(username)
                log_activity(tool_name, username)
            except:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
