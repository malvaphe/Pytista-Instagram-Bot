# Pytista Instagram Bot

A bot for instagram that aims to automate the advertising process of your profile:

- Explores posts in the hashtags you decide.
- Follows users.
- Comments posts.
- Likes posts.

The goal is also to preserve the safety of the profile,
trying to do everything in a humane way.
Each action cannot be repeated for a minimum fixed period of time,
after this time the action will be done on a statistical basis based on a probability.

## Run it

First of all clone the project:

```bash
  git clone https://github.com/malvaphe/Pytista-Instagram-Bot
```

Install Python3 and all the dependencies, then:

```bash
  cd Pytista-Instagram-Bot
  python3 Pytista.py
```

#### Use the bot wisely. Don't overdo the numbers. An excessive use of the bot, with little variety in the comments, too many follows and likes could lead to the reporting of the profile or suspension by instagram.

## Configuration

Before starting the project, configure it however you like and enter your credentials.

```python
# Credentials
myUsername = "username"
myPassword = "password"

# Hashtag list
hashtagList = [
    "love",
    ]

# Number of likes to give
likeSum = 10

# Number of comments to do
commentSum = 10

# Number of follows to do
followSum = 10

# Number of posts to watch for every hashtag
images = 40

# How often in seconds a certain action can be done
likeTime = 60  # 1 minute
commentTime = 60  # 1 minute
followTime = 300  #  5 minutes

# List of comments to do
comments = [
    "Really nice pic!",
    "Sweet!",
    "Beautiful!",
    "This is so beutiful!",
    "Such a charming picture!",
    "Very beautiful!",
    "Nice stuff!",
    "So cool!",
    "Cutie!",
    "Nice pic!",
    "The definition of beauty!",
    "This looks mesmerizing!",
    "Love this dude!",
    "Pretty!",
    "You're great dude!",
    "This photo is really good!",
    "Amazing photo :)",
    "Awesome!",
    "Great!",
    "Marvelous!",
    "Superb!",
    "Supreme!",
    "Super!",
    "Splendid!",
    "Spectacular!",
    ]
```

## Authors

- [@malvaphe](https://www.github.com/malvaphe)
