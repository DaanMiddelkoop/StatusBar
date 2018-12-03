from base import Base
import datetime


class Time(Base):
    def name(self):
        return "time"

    def full_text(self):
        return str(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))