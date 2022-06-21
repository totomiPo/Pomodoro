import time
from plyer import notification

pomodoro = 0
print("The pomodoro timer has started!")
if __name__ == "__main__":
    while True:

        time.sleep(1800)
        pomodoro += 1
        notification.notify(
            title = "Good work!",
            message = f"{str(pomodoro)} pomodoros",
        )

        time.sleep(600)
        notification.notify(
            title = "Back to work!",
        )
