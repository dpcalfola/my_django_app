from datetime import datetime


class DateObj:
    def __init__(self):
        self.today_url = datetime.today().strftime("%Y-%m-%d")
        self.today_datetime = datetime.today()
