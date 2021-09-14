from Backend.tasks import Task as task_routes
from Backend.Models.Task_model import Task as TaskModel
from flask import request, Response, jsonify
import json
import app


def create_task(task_id, task_type, status):
    try:
        task = TaskModel(
            task_id=task_id,
            task_type=task_type,
            status=status,
            task_result=None
        )
        app.db.session.add(task)
        app.db.session.commit()
        return {'status': 201}
    except:
        return {'error': "Something went wrong while creating task", 'status': 404}

def update_task(task_id, status, result, message):
    try:
        _task = app.db.session.query(TaskModel).filter(TaskModel.task_id == task_id).first()
        if not _task:
            return Response(status=400)

        _task.status = status
        _task.result = result
        _task.message = message
        app.db.session.commit()
        return {'status': 203}
    except:
        return {'error': "Something went wrong while updating task", 'status': 404}

@task_routes.route('/task/<task_id>', methods=['GET'])
def get_task_details(task_id):
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
