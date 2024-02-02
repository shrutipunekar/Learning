from task_package.create_task import create_task
from task_package.edit_task import edit_task
from task_package.categorize_task import categorize_task

#create a task
task1=create_task("complete your assignment","finish the task management system")

#display the task
print("Task 1:",task1)

#edit the task
edit_task(task1,new_title="updated assignment",new_description="review and submit to Rashmi Ma'am")

#display the updated task
print("updated task 1:",task1)

#categorize the task
categorize_task(task1,"zappkode academy")

#display the categorize task
print("categorize task 1:",task1)