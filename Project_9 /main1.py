from datetime import datetime
import time


def main():
    while True:
        now = datetime.now()

        current = now.strftime("%H:%M:%S")

        print(f"Current Time is : {current}")

        time.sleep(1)


if __name__ == '__main__':
    main()
