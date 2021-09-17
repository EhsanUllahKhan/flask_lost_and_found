email_create_schema = {
    "type": "object",
    "properties": {
        "sender_email": {"type": "string"},
        "receiver_email": {"type": "string"},
        "subject": {"type": "string"},
        "message": {"type": "string"},
    },
    "required": ["message", "subject", "receiver_email", "sender_email"]
}