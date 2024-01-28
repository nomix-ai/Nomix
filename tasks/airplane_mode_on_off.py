import json
from time import sleep

import requests

from internal.common import get_task_uuid_from_server_response, get_task_status_from_server_response, TaskStatus
from internal.const import IP_ADDRESS, PROTOCOL
from internal.logger import logger

_url = f"{PROTOCOL}://{IP_ADDRESS}:35000/api/v1/tasks"


def airplane_mode_on_off(
        token: str,
        device_uuids: [str],
) -> bool:
    """
    Sends the "airplane_mode_on_off" task and returns when the task is completed.

    :param token: Nomix token
    :param device_uuids: devices to which the task will be sent
    :return: True if task completed successfully, False otherwise
    """
    headers = {
        'Content-Type': 'application/json',
        'X-Nomix-API-Key': f'{token}'
    }
    payload = json.dumps({
        "task-name": "airplane-mode-on-off",
        "device-uuids": device_uuids,
        "context": {}
    })

    response = requests.request("POST", _url, headers=headers, data=payload, verify=False)
    if not response.ok:
        logger.error(f"Failed to send \"airplane_mode_on_off\": {response.text}")
        return False

    task_uuid = get_task_uuid_from_server_response(response.text)
    logger.info(f"Task \"airplane_mode_on_off\" sent: {task_uuid}")

    task_status_url = f"{_url}/{task_uuid}"
    while True:
        logger.debug(f"Waiting for the task to complete: {task_uuid}")
        sleep(10)

        response = requests.request("GET", task_status_url, headers=headers, verify=False)
        if not response.ok:
            logger.error(f"Failed to check \"airplane_mode_on_off\" status: {response.text}")
            return False

        logger.debug(f"Task status: {response.text}")

        task_status = get_task_status_from_server_response(response.text)
        if task_status == TaskStatus.SUCCESS:
            logger.info(f"Task \"airplane_mode_on_off\" ({task_uuid}) completed successfully")
            return True
        elif task_status == TaskStatus.ERROR:
            logger.error(f"Task \"airplane_mode_on_off\" ({task_uuid} completed with error")
            return False
