class Storage:
    def __init__(self):
        self.task_holder = []
        self.id_count = 0

    def add_task(self, task):
        self.id_count += 1
        task.id = self.id_count
        self.task_holder.append(task)

    def get_task(self, task_id):
        for task in self.task_holder:
            if task.id == task_id:
                return task
        return None

    def get_all_tasks(self):
        return self.task_holder