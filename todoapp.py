# Keep track of todos using a list.
todo_list = []

# I need to print my todos
def print_todos():
    if len(todo_list) == 0:
    print("you have nothing to do!")
    else:
        for todo in todo_list:
            print(todo)

# I need a way to add todos.
def add_todo(todo):
    # We recieve a todo which is a string.
    todo_list.append(todo)

# Print the empty todo list.
print_todos()
# Add a todo by calling our function.
add_todo("feed the cat")
# Print the todo list again, making sure my todo got added.
print_todos()

# I need to be able to delete todos.
def delete_todo(index):
    #del todo_list[index] <- another way to pop
    try:
        todo_list.pop(index)
    except IndexError:
        print("Sorry, no todo at that index.")

#delete_todo(0)
#print(todo_list)
#delete_todo(0)
#print(todo_list)


# Show user the main menu.
def main():
    menu = """
The Best Todo App Ever
======================
0. Quit
1. Print the Todos
2. Add a Todo
3. Complete a Todo
"""
    is_running = True
    while is_running:
        print(menu)
        user_choice= input("Choose one: ")
        if user_choice == "0":
            is_running= False
            print("Thank you for using the todo app")
        elif user_choice == "1":
            print_todos()
        elif user_choice == "2":
            #prompt them for what they want to do 
            new_todo = input("What do you need to do?")
            add_todo(new_todo)
        elif user_choice == "3":
            pass
        else:
            print("Please enter a number for your choice.")

main()