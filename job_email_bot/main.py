from sources import get_jobs
from emailer import send_email

def main():
    jobs = get_jobs()

    if jobs:
        send_email(jobs)

if __name__ == "__main__":
    main()
