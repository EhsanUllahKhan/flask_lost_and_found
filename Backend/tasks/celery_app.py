from Backend.common.celery_app import celery
from Backend.Models import *



@celery.task(name='create_user_task', bind=True)
def task_create_user(self, *name):
    print(f'\n\t>>>>>>>>>>>> create user id \t{self.request.id.__str__()}<<<<<<<<<<<<<\n')
    print(f'\n\t.............. status of task ................ \t{self.AsyncResult(self.request.id).state}')
    self.update_state(state='PROGRESS')
    print(f'\n\t.............. status of task ................ \t{self.AsyncResult(self.request.id).state}')


@celery.task(name='delete_user_task', bind=True)
def task_delete_user(self, *id):
    print(f'\n\t>>>>>>>>>>>> delete id \t{self.request.id.__str__()}<<<<<<<<<<<<<\n')


@celery.task(name='create_item_task', bind=True)
def task_create_user(self, *name):
    print(f'\n\t>>>>>>>>>>>> create item with task id \t{self.request.id.__str__()}<<<<<<<<<<<<<\n')


@celery.task(name='delete_item_task', bind=True)
def task_delete_user(self, *id):
    print(f'\n\t>>>>>>>>>>>> delete item with id \t{self.request.id.__str__()}<<<<<<<<<<<<<\n')

