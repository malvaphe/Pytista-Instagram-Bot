# Dependencies
from threading import Timer
from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Initialize webdriver
options = Options()
options.add_argument("--headless")
webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                             options=options)

# CONFIGURATION START -----------------------------------------------------------------------------------------

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
commentSum = 2

# Number of follows to do
followSum = 0

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

# CONFIGURATION END -------------------------------------------------------------------------------------------


# Can follow a user every set amount of time
def timerfollow():
    global tfollow
    tfollow = 0
    global tf
    tf = Timer(followTime, timerfollowchange)
    tf.start()


# Switch to now it can follow
def timerfollowchange():
    global tfollow
    tfollow = 1


# Can like a post every set amount of time
def timerlike():
    global tlike
    tlike = 0
    global tl
    tl = Timer(likeTime, timerlikechange)
    tl.start()


# Switch to now it can like
def timerlikechange():
    global tlike
    tlike = 1


# Can comment a post every set amount of time
def timercomment():
    global tcomment
    tcomment = 0
    global tc
    tc = Timer(commentTime, timercommentchange)
    tc.start()


# Switch to now it can comment
def timercommentchange():
    global tcomment
    tcomment = 1


# Follow a user
def funfollow():
    global followSum
    global tfollow

    # Probability of following a user
    follow_prob = randint(20, 100)

    try:

        # User username
        username = webdriver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/span/a",
        ).text

        # Check if we are already following the user
        if (webdriver.find_element(
                By.XPATH,
                "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button",
        ).text == "Follow"):

            # If we can follow, we have not yet followed our target number and the probability is greater than x
            if tfollow == 1 and followSum > 0 and follow_prob > 40:

                # Follow the user
                try:
                    webdriver.find_element(
                        By.XPATH,
                        "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button",
                    ).click()
                    followSum -= 1
                    print(
                        "[SUCCESS] Following {}, number of remaining users to follow: {}"
                        .format(username, followSum))
                    timerfollow()
                    sleep(randint(20, 38))
                except:
                    print(
                        "[ERROR] Problem following the user, number of remaining users to follow:: {}"
                        .format(followSum))
    except:
        print(
            "[ERROR] Problem running the follow function, number of remaining users to follow:: {}"
            .format(followSum))


# Like a post
def funlike():
    global likeSum
    global tlike

    # Probability of liking a post
    like_prob = randint(1, 100)

    # If we can like, we have not yet followed our target number and the probability is greater than x
    if tlike == 1 and likeSum > 0 and like_prob > 20:

        # Like the post
        try:
            button_like = webdriver.find_element(
                By.XPATH,
                "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button",
            )
            button_like.click()
            likeSum -= 1
            print("[SUCCESS] Post liked, missing likes: {}".format(likeSum))
            timerlike()
            sleep(randint(20, 38))
        except:
            print("[ERROR] Problem liking the post, missing likes: {}".format(
                likeSum))


# Comment a post
def funcomment():
    global commentSum
    global tcomment
    global comments

    # Number of the comment in the comments array
    commentNumber = randint(0, len(comments))

    # If we can comment, we have not yet followed our target number
    if tcomment == 1 and commentSum > 0:

        # Comment the post
        try:
            webdriver.find_element(
                By.XPATH,
                "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea",
            ).click()
            comment_box = webdriver.find_element(
                By.XPATH,
                "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea",
            )
            comment_box.send_keys(comments[commentNumber])
            sleep(1)

            # Enter key to send the comment
            comment_box.send_keys(Keys.ENTER)
            commentSum -= 1
            print("[SUCCESS] New comment posted, missing comments: {}".format(
                commentSum))
            timercomment()
            sleep(randint(20, 38))
        except:
            print("[ERROR] Problem commenting the post, missing comments: {}".
                  format(commentSum))


# Click the arrow to see next post
def nextpost():
    try:
        try:
            webdriver.find_element(
                By.XPATH,
                "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button",
            ).click()
        except:
            webdriver.find_element(
                By.XPATH,
                "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button",
            ).click()
    except:
        print("[ERROR] Problem clicking the arrow to see the next post.")


# Go to the instagram login page and sing in
webdriver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
sleep(5)

# Cookie button click
webdriver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[2]").click()
sleep(2)

# Insert username and password
username = webdriver.find_element(By.NAME, "username")
username.send_keys(myUsername)
sleep(1)
password = webdriver.find_element(By.NAME, "password")
password.send_keys(myPassword)

# Click the login button after 2 seconds
sleep(2)
button_login = webdriver.find_element(
    By.XPATH,
    "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button",
)
button_login.click()
sleep(8)

# The bot output starts here
print("A total of {} images from {} tags will be displayed.".format(
    images * len(hashtagList), len(hashtagList)))

# Indicates if the bot can take an action at a certain time
tfollow = 1  # can follow
tcomment = 1  # can comment
tlike = 1  # can like

# Loop starts here
tag = -1  # do not change
for hashtag in hashtagList:

    # The tag we're going to explore
    tag += 1
    print("-----------------------------------------------[HASHTAG {}]".format(
        hashtagList[tag]))
    webdriver.get("https://www.instagram.com/explore/tags/" +
                  hashtagList[tag] + "/")
    sleep(5)
    try:

        # Click the first post in the hashtag page
        first_thumbnail = webdriver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a",
        )
        first_thumbnail.click()
    except:
        print("[ERROR] Problem with the hashtag.")
        continue

    sleep(5)
    x = 1
    try:
        while x < images + 1:

            # Go on only if we are not following the user of the post
            try:
                if (webdriver.find_element(
                        By.XPATH,
                        "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button",
                ).text == "Follow"):
                    print("Looking at photo number {}".format(x))
                    funfollow()
                    funlike()
                    funcomment()
                    nextpost()
                    x = x + 1
                    sleep(randint(20, 38))

                    # Stop if we have reached our target numbers
                    if likeSum == 0 and commentSum == 0 and followSum == 0:
                        break
                else:

                    # If we are already following the user of the post, go to the next post
                    nextpost()
                    sleep(randint(8, 12))
            except:
                try:
                    print("[ERROR] Problem analyzing the post.")
                    nextpost()
                    sleep(randint(8, 12))
                except:
                    print("[ERROR] Critical error, changing hashtag.")
                    x = images

        # Stop if we have reached our target numbers
        if likeSum == 0 and commentSum == 0 and followSum == 0:
            break
    except Exception as e:
        print("[ERROR] Problem in the loop: ", e)
        continue
