import json
from time import sleep

import requests

from internal.common import get_task_uuid_from_server_response, get_task_status_from_server_response, TaskStatus
from internal.const import IP_ADDRESS, PROTOCOL
from internal.logger import logger

_url = f"{PROTOCOL}://{IP_ADDRESS}:35000/api/v1/tasks"


def like_post_by_link(
        token: str,
        device_uuids: [str],
        link: str,
        package: str = "com.instagram.android",
) -> bool:
    """
    Sends the "like_post_by_link" task and returns when the task is completed.

    :param token: Nomix token
    :param device_uuids: devices to which the task will be sent
    :param link: link to the post/reel to like
    :param package: "com.instagram.android" or a cloned app package
    :return: True if task completed successfully, False otherwise
    """
    headers = {
        'Content-Type': 'application/json',
        'X-Nomix-API-Key': f'{token}'
    }
    payload = json.dumps({
        "task-name": "like-post-by-link",
        "package-pattern": f"{package}",
        "device-uuids": device_uuids,
        "context": {
            "link": link
        }
    })

    response = requests.request("POST", _url, headers=headers, data=payload, verify=False)
    if not response.ok:
        logger.error(f"Failed to send \"like_post_by_link\": {response.text}")
        return False

    task_uuid = get_task_uuid_from_server_response(response.text)
    logger.info(f"Task \"like_post_by_link\" sent: {task_uuid}")

    task_status_url = f"{_url}/{task_uuid}"
    while True:
        logger.debug(f"Waiting for the task to complete: {task_uuid}")
        sleep(10)

        response = requests.request("GET", task_status_url, headers=headers, verify=False)
        if not response.ok:
            logger.error(f"Failed to check \"like_post_by_link\" status: {response.text}")
            return False

        logger.debug(f"Task status: {response.text}")

        task_status = get_task_status_from_server_response(response.text)
        if task_status == TaskStatus.SUCCESS:
            logger.info(f"Task \"like_post_by_link\" ({task_uuid}) completed successfully")
            return True
        elif task_status == TaskStatus.ERROR:
            logger.error(f"Task \"like_post_by_link\" ({task_uuid} completed with error")
            return False
