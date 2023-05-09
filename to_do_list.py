class ToDoList:
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self, task):
        """Add a task to the list."""
        self.tasks.append(task)
        print(f"Task added successfully!")

    def view_tasks(self):
        """Display all task available in the list."""
        if self.tasks == []:
            print(f"To-Do list is empty.")
        else:
            print(f"Available tasks in the list:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def delete_task(self, task_number):
        """Display a task from the list using task number."""
        try:
            del self.tasks[task_number-1]
            print(f"Task deleted successfully!")
        except IndexError:
            print(f"Invalid task number. Please try again.")

    def main(self):
        """To Do Application Loop"""
        while True:
            print(f"\nTo-Do List")
            print(f"1. Add a task")
            print(f"2. Delete a task")
            print(f"3. View all tasks")
            print(f"4. Quit")

            choice = input("Enter the number of choice: ")

            if choice == "1":
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == "2":
                task_number = int(input("Enter the task number to delete: "))
                self.delete_task(task_number)
            elif choice == "3":
                self.view_tasks()
            elif choice == "4":
                print(f"Thanks for using the To-Do List App! Goodbye.")
                break
            else:
                print(f"Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    app = ToDoList()
    app.main()