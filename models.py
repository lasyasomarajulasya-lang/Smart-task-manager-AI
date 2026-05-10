class Task:
    def __init__(self, id, title, description, priority):
        self.id = id
        self.title = title 
        self.description = description
        self.priority = priority  # High, Medium, Low
        self.completed = False

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description, 
            'priority': self.priority,
            'completed': self.completed
        }