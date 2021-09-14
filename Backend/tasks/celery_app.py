from Backend.common.celery_app import celery
from Backend.Models import *



@celery.task(name='create_user.task', bind=True)
def task_create_user(self, *name):
    print(f'\n\t>>>>>>>>>>>> task id \t{self.request.id.__str__()}<<<<<<<<<<<<<\n')
