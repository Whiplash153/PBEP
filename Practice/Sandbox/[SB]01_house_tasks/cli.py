from storage import Storage
from models import HomeTask

def main():

    storage = Storage("archive.json")

    while True:
        print("\n=== MENU ===")
        print("1. Add task")
        print("2. Tasks list")
        print("3. Get task by ID")
        print("4. Quit")

        choice = input("\nChoose your number: ").strip()

        if choice == "1":
            # ADD TASK
            title = input("Enter task title: ").strip()
            responsible = input("Enter owner's name: ").strip()
            task = HomeTask(title, responsible)
            storage.add_task(task)
            print("\nTask successfully added!")

        elif choice == "2":
            # TASKS LIST
            tasks_list = storage.get_all_tasks()

            if not tasks_list:
                print("\nNo tasks yet.")
            else:
                print("\nTasks list:")
                for task in tasks_list:
                    print(task)

        elif choice == "3":
            # GET TASK BY ID

            try:
                task_id = int(input("Enter task id:"))
                task = storage.get_task_by_id(task_id)
                if not task:
                    print("\nNo such task")
                else:
                    print(task)
            except (ValueError):
                print("Invalid data")

        elif choice == "4":
            # QUIT
            print("\nGood bye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

