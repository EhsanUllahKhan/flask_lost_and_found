lost_item_create_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "lost_by_user_id" : {"type": "integer"}
    },
    "required": ["name", "lost_by_user_id"]
}