import json
from enum import Enum


def get_task_uuid_from_server_response(response: str) -> str:
    return json.loads(response)["tasks"][0]["task-uuid"]


def get_task_status_from_server_response(response: str) -> 'TaskStatus':
    status = json.loads(response)["status"]
    if status == "SUCCESS":
        return TaskStatus.SUCCESS
    elif status == "SCHEDULED":
        return TaskStatus.SCHEDULED
    else:
        return TaskStatus.ERROR


class TaskStatus(Enum):
    SUCCESS = 1
    SCHEDULED = 0
    ERROR = -1
