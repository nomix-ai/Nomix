# Nomix
Hey there! Nomix is a **new automation tool** which automates actions in Instagram (follows, likes of posts and stories, replying to new followers, etc.) also supporting IP rotation and cloned apps. The key benefit is that Nomix is completely safe and undistinguishable from human, because it does not use PC or connection to PC unlike most other services. Actions are performed directly on the phones via **Nomix Android app**.

<img width="1024" src="https://github.com/nomix-ai/Nomix/assets/22825859/10af07ca-0ce1-47b7-bc46-653a3ec23ad2">

## Getting Started
You will need your personal "token" to run Nomix. Since it's an early beta testing, as an early tester you can get your token for free. Later the tokens are going to become a paid "entry" to Nomix.

### Installation
1. Install the latest [Nomix Android app](https://drive.google.com/drive/u/0/folders/1fA84Ahwz-pGTVDaI41gHYxL4SfVsYG0L) on your phone.
2. Install Python 3 on your PC.
3. Install requirements: `python3 -m pip install -r requirements.txt`.
4. Get your token (please write [@alexal1](https://t.me/alexal1) *"Hey, I'd like to get token to test Nomix"*) and once you get the token, enter it both in Nomix Android app and in the script in `main.py`.
6. Run the script: `python3 main.py`

### Usage
To modify the behavior, edit `main.py`. Inside `main()` function you can call "tasks" from the [tasks folder](https://github.com/nomix-ai/Nomix/tree/master/tasks). A task is an action to be executed on the specified devices. E.g. "like a specific post", "follow a specific account", etc. You can also add pauses and schedule execution to specific hours.

The list of available tasks:

|            Task             |                          Description                           |      Method name      |
|-----------------------------|----------------------------------------------------------------|-----------------------|
|Like post by link            |Opens a post or reel by a link and likes it                     |`like_post_by_link`    |
|Follow account by link       |Opens an account by link and follows it                         |`follow_by_link`       |
|Airplane mode turn on and off|Turns airplane mode on the phone on and off to rotate IP address|`airplane_mode_on_off` |
|Like stories of likers of posts in Explore|Like stories of accounts, who liked the same content as you see in your Explore section. I.e. utilise Instagram to find audience similar to your account. If "search prompt" is provided, then will use "For you" section based on this prompt.|`like_stories_of_likers_of_posts`|

## Community
Nomix is in it's beta currently. The plans are to add more tasks:
- [ ] Follow the followers of specific accounts
- [ ] Follow the likers of posts of specific accounts
- [ ] Unfollow accounts which do not follow back
- [ ] Liking posts of specific accounts
- [ ] Sending "welcome DMs" to new followers

and to add some technical improvements:
- [ ] Create a Telegram bot which will do the same as this script, but via simple settings and buttons
- [ ] Automatic tokens generation
- [ ] Add reports on how many and which actions (watches, likes, follows, etc.) were made by Nomix

To have your fingers on the pulse, feel free to join **Nomix Beta Testers** channel in Telegram.

<a href="https://t.me/nomixai">
  <img width="256" src="https://github.com/nomix-ai/Nomix/assets/22825859/ebc1fa64-a5e9-4d5f-9b99-7366761640da">
</a>
