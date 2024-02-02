from .task import Task   #task = module and Task=class.here without using class we import(create task only one at a time)
def create_task(title,description,category=None):
    new_task=Task(title,description,category)
    return new_task