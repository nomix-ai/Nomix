import json
from time import sleep

import requests

from internal.common import get_task_uuid_from_server_response, get_task_status_from_server_response, TaskStatus
from internal.const import IP_ADDRESS, PROTOCOL
from internal.logger import logger

_url = f"{PROTOCOL}://{IP_ADDRESS}:35000/api/v1/tasks"


def like_stories_of_likers_of_posts(
        token: str,
        device_uuids: [str],
        posts_to_open: int,
        post_likers: int,
        search_prompt: str = "",
        package: str = "com.instagram.android",
) -> bool:
    """
    Sends the "like_stories_of_likers_of_posts" task and returns when the task is completed.

    :param token: Nomix token
    :param device_uuids: devices to which the task will be sent
    :param posts_to_open: number of posts to open
    :param post_likers: number of likers of posts to open for each post
    :param search_prompt: search phrase to open suggested posts or "" to open recommendations
    :param package: "com.instagram.android" or a cloned app package
    :return: True if task completed successfully, False otherwise
    """
    headers = {
        'Content-Type': 'application/json',
        'X-Nomix-API-Key': f'{token}'
    }
    payload = json.dumps({
        "task-name": "like-post-likers-stories",
        "package-pattern": f"{package}",
        "device-uuids": device_uuids,
        "context": {
            "posts-to-open": posts_to_open,
            "post-likers": post_likers,
            "search_prompt": search_prompt
        }
    })

    response = requests.request("POST", _url, headers=headers, data=payload, verify=False)
    if not response.ok:
        logger.error(f"Failed to send \"like_stories_of_likers_of_posts\": {response.text}")
        return False

    task_uuid = get_task_uuid_from_server_response(response.text)
    logger.info(f"Task \"like_stories_of_likers_of_posts\" sent: {task_uuid}")

    task_status_url = f"{_url}/{task_uuid}"
    while True:
        logger.debug(f"Waiting for the task to complete: {task_uuid}")
        sleep(10)

        response = requests.request("GET", task_status_url, headers=headers, verify=False)
        if not response.ok:
            logger.error(f"Failed to check \"like_stories_of_likers_of_posts\" status: {response.text}")
            return False

        logger.debug(f"Task status: {response.text}")

        task_status = get_task_status_from_server_response(response.text)
        if task_status == TaskStatus.SUCCESS:
            logger.info(f"Task \"like_stories_of_likers_of_posts\" ({task_uuid}) completed successfully")
            return True
        elif task_status == TaskStatus.ERROR:
            logger.error(f"Task \"like_stories_of_likers_of_posts\" ({task_uuid} completed with error")
            return False
