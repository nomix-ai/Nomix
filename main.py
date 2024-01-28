import logging
from time import sleep

from internal.logger import logger
from tasks.airplane_mode_on_off import airplane_mode_on_off
from tasks.follow_by_link import follow_by_link
from tasks.like_post_by_link import like_post_by_link
from tasks.like_stories_of_likers_of_posts import like_stories_of_likers_of_posts

# Your Nomix token
token = ""
# Devices where the tasks will be sent to
device_uuids = ["be1gr8f3-eef8-4586-8b25-0421a1325634"]


def main():
    logger.setLevel(logging.INFO)

    # Execute tasks one by one in an infinite cycle
    while True:
        like_stories_of_likers_of_posts(
            token,
            device_uuids,
            posts_to_open=1,
            post_likers=1,
            search_prompt=""
        )

        airplane_mode_on_off(
            token,
            device_uuids
        )

        like_post_by_link(
            token,
            device_uuids,
            link="https://www.instagram.com/p/BJcxX5NDRKl"
        )

        airplane_mode_on_off(
            token,
            device_uuids
        )

        follow_by_link(
            token,
            device_uuids,
            link="https://www.instagram.com/platon_yurich_classic"
        )

        sleep(60 * 5)


if __name__ == '__main__':
    main()
