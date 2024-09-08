import datetime

def open_ovice():
    try:
        with open("/Users/kimura.shunya/Desktop/python_lesson/cron_test_log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: Cron job executed successfully.\n")
    except Exception as e:
        with open("/Users/kimura.shunya/Desktop/python_lesson/cron_test_log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: An error occurred: {e}\n")

if __name__ == "__main__":
    open_ovice()
