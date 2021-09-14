from Backend.tasks import Task as task_routes
from Backend.Models.Task_model import Task as TaskModel
from flask import request, Response, jsonify
import json
import app
from Backend.common.celery_app import celery

def create_task(task_id, task_type, status):

    try:
        task = TaskModel(
            task_id=task_id,
            task_type=task_type,
            task_status=status,
            task_result=None,
            message=None
        )
        app.db.session.add(task)
        app.db.session.commit()
        print('task created')
    except Exception as ex:
        raise ex

def update_task(task_id, status, result=None, message=None):
    try:
        _task = app.db.session.query(TaskModel).filter(TaskModel.task_id == task_id).first()
        if not _task:
            return Response(status=400)

        _task.task_status = status
        _task.task_result = result
        _task.message = message
        app.db.session.commit()
        print('task updated')
    except Exception as ex:
        raise ex

@task_routes.route('/task/<task_id>', methods=['GET'])
def get_task_details(task_id):
    # return dict(task_status=celery.AsyncResult(task_id).state)

    try:
        tasks = app.db.session.query(TaskModel).filter(TaskModel.task_id == task_id).first()
        if not tasks:
            return Response(status=204)

        tasks_list = list()
        # for item in items:
        tasks_list.append(tasks.to_json())
        return Response(json.dumps(tasks_list, indent=4, sort_keys=True, default=str), mimetype='application/json')
    except:
        return {'error': "Something went wrong while deleting task", 'status': 404}
