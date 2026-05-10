class Task:
    id_counter = 1
    
    def __init__(self, title, description, priority):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed
        }

tasks = []

def get_all_tasks():
    return tasks

def add_task(title, description, priority):
    new_task = Task(title, description, priority)
    tasks.append(new_task)
    return new_task

def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t.id != task_id]
    return True

def complete_task(task_id):
    for t in tasks:
        if t.id == task_id:
            t.completed = not t.completed
            return True
    return False