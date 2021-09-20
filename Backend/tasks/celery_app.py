import sys
from datetime import datetime

from Backend.common.celery_app import celery
from Backend.Models.User_model import User as UserModel
from Backend.Models.Item_model import Item as ItemModel
from Backend.Models.Email_model import Email as EmailModel
import app
from Backend.tasks.exceptions import EmailAlreadyExistException, UserDoesNotExistException, ItemNotFoundException
from Backend.tasks.api_task import create_task, update_task
import time
from sqlalchemy.exc import IntegrityError
from flask_mail import Message
from Backend import mail
from config import config


@celery.task(name='send_async_email', bind=True)
def send_async_email(self, *data):
    # create_task(
    #     task_id=self.request.id.__str__(),
    #     task_type='SEND_EMAIL',
    #     status=self.AsyncResult(self.request.id).state.upper()
    # )
    #
    # time.sleep(5)
    #
    # self.update_state(state='IN_PROGRESS')
    # update_task(
    #     task_id=self.request.id.__str__(),
    #     status=self.AsyncResult(self.request.id).state.upper()
    # )
    #
    # time.sleep(5)
    try:
        email = EmailModel(
            receiver_email=data[1]['receiver_email'],
            subject=data[1]['subject'],
            message=data[1]['message'],
            sender_email=data[1]['sender_email']
        )
        app.db.session.add(email)
        app.db.session.commit()

        msg = Message(data[0]['subject'],
                      sender=config.MAIL_DEFAULT_SENDER,
                      recipients=[data[0]['to']])
        msg.body = data[0]['body']

        with app.app_context():
            mail.send(msg)

        # update_task(task_id=self.request.id.__str__(), status="COMPLETED", result="SUCCESS", message="SENT-EMAIL")

    except Exception as ex:
        app.db.session.rollback()
        ex_type, ex_value, ex_traceback = sys.exc_info()
        # update_task(task_id=self.request.id.__str__(), status="COMPLETED", result="FAILURE", message=str(ex_type.__name__))
        raise ex

@celery.task(name='create_user_task', bind=True)
def task_create_user(self, *data):
    # print(f'\n\t>>>>>>>>>>>> create user id \t{self.request.id.__str__()}<<<<<<<<<<<<<\n')
    # print(f'\n\t.............. data of task ................ \t{data[0]}')
    create_task(
        task_id=self.request.id.__str__(),
        task_type='CREATE_USER',
        status=self.AsyncResult(self.request.id).state.upper()
    )

    time.sleep(5)

    self.update_state(state='IN_PROGRESS')
    update_task(
        task_id=self.request.id.__str__(),
        status=self.AsyncResult(self.request.id).state.upper()
    )

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
    create_task(
        task_id=self.request.id.__str__(),
        task_type='DELETE_USER',
        status=self.AsyncResult(self.request.id).state.upper()
    )

    time.sleep(5)

    self.update_state(state='IN_PROGRESS')
    update_task(
        task_id=self.request.id.__str__(),
        status=self.AsyncResult(self.request.id).state.upper()
    )

    time.sleep(5)
    try:
        _user = app.db.session\
            .query(UserModel)\
            .filter(UserModel.email == data[0])\
            .first()

        if not _user:
            raise UserDoesNotExistException(data[0])

        app.db.session.delete(_user)
        app.db.session.commit()

        update_task(task_id=self.request.id.__str__(), status="COMPLETED", result="SUCCESS", message="DELETED-USER")

    except Exception as ex:
        update_task(task_id=self.request.id.__str__(), status="COMPLETED", result="FAILURE", message=ex)
        raise ex


@celery.task(name='create_item_task', bind=True)
def task_create_user(self, *data):
    create_task(
        task_id=self.request.id.__str__(),
        task_type='CREATE_ITEM',
        status=self.AsyncResult(self.request.id).state.upper()
    )

    time.sleep(5)

    self.update_state(state='IN_PROGRESS')
    update_task(
        task_id=self.request.id.__str__(),
        status=self.AsyncResult(self.request.id).state.upper()
    )

    time.sleep(5)
    try:
        item = ItemModel(
                    name = data[0],
                    is_found = False,
                    lost_date = datetime.today().date(),
                    lost_by_user_id = data[1],
                    found_by_user_id = None
                )
        app.db.session.add(item)
        app.db.session.commit()
        update_task(task_id=self.request.id.__str__(), status="COMPLETED", result="SUCCESS", message="CREATED-ITEM")

    except IntegrityError as ex:
        app.db.session.rollback()
        ex_type, ex_value, ex_traceback = sys.exc_info()
        update_task(task_id=self.request.id.__str__(), status="COMPLETED", result="FAILURE", message=str(ex_type.__name__))
        raise ex


@celery.task(name='delete_item_task', bind=True)
def task_delete_user(self, *data):
    create_task(
        task_id=self.request.id.__str__(),
        task_type='DELETE_ITEM',
        status=self.AsyncResult(self.request.id).state.upper()
    )

    time.sleep(5)

    self.update_state(state='IN_PROGRESS')
    update_task(
        task_id=self.request.id.__str__(),
        status=self.AsyncResult(self.request.id).state.upper()
    )

    time.sleep(5)
    try:
        _item = app.db.session.query(ItemModel).filter(ItemModel.lost_item_id == data[0]).first()
        if not _item:
            raise ItemNotFoundException(data[0])
        app.db.session.delete(_item)
        app.db.session.commit()
        update_task(task_id=self.request.id.__str__(), status="COMPLETED", result="SUCCESS", message="DELETED-ITEM")

    except Exception as ex:
        update_task(task_id=self.request.id.__str__(), status="COMPLETED", result="FAILURE", message=str(ex))
        raise ex


@celery.task(name='found_item_task', bind=True)
def task_delete_user(self, *data):
    create_task(
        task_id=self.request.id.__str__(),
        task_type='FOUND_ITEM',
        status=self.AsyncResult(self.request.id).state.upper()
    )

    time.sleep(5)

    self.update_state(state='IN_PROGRESS')
    update_task(
        task_id=self.request.id.__str__(),
        status=self.AsyncResult(self.request.id).state.upper()
    )

    time.sleep(5)
    try:
        _item = app.db.session.query(ItemModel).filter(ItemModel.lost_item_id == data[0]).first()
        if not _item:
            raise ItemNotFoundException(status=400)

        _item.is_found = True
        _item.found_by_user_id = data[1]
        app.db.session.commit()
        update_task(task_id=self.request.id.__str__(), status="COMPLETED", result="SUCCESS", message="FOUND-ITEM")


    except IntegrityError as ex:
        app.db.session.rollback()
        ex_type, ex_value, ex_traceback = sys.exc_info()
        update_task(task_id=self.request.id.__str__(), status="COMPLETED", result="FAILURE", message=str(ex_type.__name__))
        raise ex



