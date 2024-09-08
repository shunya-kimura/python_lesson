import subprocess

def open_meeting():
    url = "https://meet.google.com/vij-esbp-ajz"
    subprocess.Popen(["open", url])

if __name__ == "__main__":
    open_meeting()