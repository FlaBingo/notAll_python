# Define the main class for the to-do list
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Added task: {task}')

    def remove_task(self, index):
        try:
            removed_task = self.tasks.pop(index)
            print(f'Removed task: {removed_task}')
        except IndexError:
            print('Error: Invalid task number')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks in the to-do list.')
        else:
            print('To-Do List:')
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}. {task}')

# Function to display the menu and handle user input
def display_menu():
    todo_list = TodoList()
    while True:
        print('\nTo-Do List Menu:')
        print('1. View tasks')
        print('2. Add task')
        print('3. Remove task')
        print('4. Exit')
        choice = input('Choose an option (1-4): ')

        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '3':
            try:
                index = int(input('Enter the task number to remove: ')) - 1
                todo_list.remove_task(index)
            except ValueError:
                print('Error: Please enter a valid task number')
        elif choice == '4':
            print('Exiting the to-do list program.')
            break
        else:
            print('Invalid choice. Please choose a valid option.')

# Entry point of the program
if __name__ == '__main__':
    display_menu()



# print(
# '''
# Basic ToDo List:
# "a" to add an element
# "r" to remove a specific element
# "c" to clear the list
# '''
# )

# todos = {}

# action = input("Enter: ")
# if action == "a":
#     todos.update()