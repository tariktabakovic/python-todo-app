# Keep track of todos using a list.
todo_list = []

# I need to print my todos
def print_todos():
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

delete_todo(0)
print(todo_list)
delete_todo(0)
print(todo_list)


# Show user the main menu.
