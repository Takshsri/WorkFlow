class Task:
    def __init__(self,task_id,title,description,assigned_to,status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.status = status

    def display_task_info(self):
        print(f"Task ID: {self.task_id}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Assigned To: {self.assigned_to}")
        print(f"Status: {self.status}")
        