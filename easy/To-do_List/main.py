import json
import os

class Task:
    
    file = 'tasks.json'

    def __init__(self, taskName, done, desc):
        self.taskName = taskName
        self.description = desc
        self.done = done
    def to_dict(self):
        return {
            "taskName": self.taskName,
            "description": self.description,
            "done": self.done
        }
    @staticmethod
    def load():
        if os.path.exists(Task.file):
            with open(Task.file, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
    def add(self):
        tasks = Task.load()

        tasks.append(self.to_dict())

        with open('tasks.json', 'w') as file:
            json.dump(tasks,file, indent=1)

    @staticmethod
    def view():
        iteration = 10
        
        tasks = Task.load()

        for i in range(iteration):
            print("*", end='')
        print()
        for task in tasks:
            print(f"Name: {task['taskName']}")
            print(f"Description: {task['description']}")
            print(f"Done: {task['done']}")
            for i in range(iteration):
                print("-", end='')
            print()
        
        return
    
    @staticmethod
    def mark_done(name):
        tasks = Task.load()

        print("----------")
        for task in tasks:
            if task['taskName'].lower() == name:
                task['done'] = "done"
                print(f"Task {task['taskName']} was set to {task['done']}")
                with open(Task.file, "w") as f:
                    f.write(json.dumps(tasks, indent=4))
                return
        print("Task not found")
    @staticmethod
    def delete(name):
        tasks = Task.load()

        print("----------")
        for task in tasks:
            if task['taskName'].lower() == name:
                tasks.remove(task)
                with open(Task.file, "w") as f:
                    f.write(json.dumps(tasks, indent=4))
                print("Task was deleated")
                return
        print("Task not found")
    
def main():
    print("To-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task\n")

    choice = input("Enter your choice: ").strip()
    if(choice == '1'):
        task_name = input("Name: ").strip()
        task_desc = input("Description: ").strip()
        task = Task(taskName=task_name, done="false", desc=task_desc)
        task.add()
        print(f"Task '{task_name}' added successfully!")
    elif(choice == '2'):Task.view()
    elif(choice == '3'): Task.mark_done(input("Name of the task: ").lower())
    elif(choice == '4'): Task.delete(input("Name of the task: ").lower())

        

    

if __name__ == "__main__":
    main()