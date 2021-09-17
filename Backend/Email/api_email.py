from Backend.Email import Email as email_routes
from Backend.Models.Email_model import Email as EmailModel
from flask import request, Response, jsonify
import json
import app
from Backend.Email.schema_email import email_create_schema
from Backend.validate_json import validate_json
from Backend.common.celery_app import celery
from Backend.tasks.celery_app import send_async_email
import uuid

@email_routes.route('/email', methods=['GET'])
def get_all_emails():
    try:
        emails = app.db.session.query(EmailModel).all()
        if not emails:
            return Response(status=204)

        emails_list = list()
        for email in emails:
            emails_list.append(email.to_json())
        return Response(json.dumps(emails_list), mimetype='application/json')
    except:
        return {'error': "Something went wrong", 'status': 404}


@email_routes.route('/email', methods=['POST'])
@validate_json(email_create_schema)
def new_email():
    data = request.get_json(force=True)
    task_name = "send_email_task"
    email_data = {
        'subject': data['subject'],
        'to': data['receiver_email'],
        'body': data['message'],
    }
    task_id = uuid.uuid4()
    send_async_email.apply_async(args=(data['receiver_email'], data['subject'], data['message']), task_id=task_id)
    # task = celery.send_task(task_name, args=[email_data, data])

    return dict(
            id=task_id,
            url='http://0.0.0.0:5000/task/{}'.format(task_id)
        )


