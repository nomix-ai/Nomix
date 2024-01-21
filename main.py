import logging
from time import sleep

from internal.logger import logger
from tasks.like_stories_of_likers_of_posts import like_stories_of_likers_of_posts

# Your Nomix token
token = ""
# Devices where the tasks will be sent to
device_uuids = ["be1gr8f3-eef8-4586-8b25-0421a1325634"]


def main():
    logger.setLevel(logging.INFO)

    # Execute "Like Stories Of Likers Of Posts" task on the specified devices in an infinite cycle
    while True:
        like_stories_of_likers_of_posts(
            token,
            device_uuids,
            posts_to_open=1,
            post_likers=1,
            search_prompt=""
        )
        sleep(5 * 60)  # Wait 5 minutes


if __name__ == '__main__':
    main()
