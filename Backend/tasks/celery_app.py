from Backend.common.celery_app import celery
from Backend.Models.User_model import User as UserModel
from Backend.Models.Task_model import Task as TaskModel
import app
from Backend.tasks.exceptions import EmailAlreadyExistException, UserDoesNotExistException
from Backend.tasks.api_task import create_task, update_task
import time

# def create_task(task_id, task_type, status):
#     # try:
#     task = TaskModel(
#             task_id=task_id,
#             task_type=task_type,
#             task_status=status,
#             task_result=None,
#             message=None
#     )
#     app.db.session.add(task)
#     app.db.session.commit()
#     print('task created')
        # return {'status': 201}
    # except:
    #     return {'error': "Something went wrong while creating task", 'status': 404}

@celery.task(name='create_user_task', bind=True)
def task_create_user(self, *data):
    print(f'\n\t>>>>>>>>>>>> create user id \t{self.request.id.__str__()}<<<<<<<<<<<<<\n')
    print(f'\n\t.............. data of task ................ \t{data[0]}')
    create_task(task_id=self.request.id.__str__(), task_type='CREATE_USER', status=self.AsyncResult(self.request.id).state.upper())

    time.sleep(5)

    self.update_state(state='IN_PROGRESS')
    update_task(task_id=self.request.id.__str__(), status=self.AsyncResult(self.request.id).state.upper())

    time.sleep(5)
    try:
        _user = app.db.session\
            .query(UserModel)\
            .filter(UserModel.email == data[0])\
            .first()

        if _user:
            raise EmailAlreadyExistException(data[0])

        user = UserModel(
            email = data[0]
        )
        app.db.session.add(user)
        app.db.session.commit()
        update_task(task_id=self.request.id.__str__(), status="COMPLETED", result="SUCCESS", message="CREATED-USER")

    except Exception as ex:
        update_task(task_id=self.request.id.__str__(), status="COMPLETED", result="FAILURE", message=ex)
        raise ex


@celery.task(name='delete_user_task', bind=True)
def task_delete_user(self, *data):
    print(f'\n\t>>>>>>>>>>>> delete id \t{self.request.id.__str__()}<<<<<<<<<<<<<\n')
    print(f'\n\t.............. data of task ................ \t{data[0]}')
    create_task(task_id=self.request.id.__str__(), task_type='DELETE_USER', status=self.AsyncResult(self.request.id).state.upper())

    time.sleep(5)

    self.update_state(state='IN_PROGRESS')
    update_task(task_id=self.request.id.__str__(), status=self.AsyncResult(self.request.id).state.upper())

    time.sleep(5)
    try:
        _user = app.db.session\
            .query(UserModel)\
            .filter(UserModel.email == data[0])\
            .first()

        if not _user:
            raise UserDoesNotExistException(data[0])

        # _user = app.db.session.query(UserModel).filter(UserModel.email == data[0]).first()
        app.db.session.delete(_user)
        app.db.session.commit()

        update_task(task_id=self.request.id.__str__(), status="COMPLETED", result="SUCCESS", message="DELETED-USER")

    except Exception as ex:
        update_task(task_id=self.request.id.__str__(), status="COMPLETED", result="FAILURE", message=ex)
        raise ex


@celery.task(name='create_item_task', bind=True)
def task_create_user(self, *name):
    print(f'\n\t>>>>>>>>>>>> create item with task id \t{self.request.id.__str__()}<<<<<<<<<<<<<\n')


@celery.task(name='delete_item_task', bind=True)
def task_delete_user(self, *id):
    print(f'\n\t>>>>>>>>>>>> delete item with id \t{self.request.id.__str__()}<<<<<<<<<<<<<\n')

