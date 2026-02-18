from models import HomeTask

def close_task(actor, task):
    if actor != task.responsible:
        raise ValueError("Only responsible users can close the task")

    task.close()