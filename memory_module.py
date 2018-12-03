from base import Base
import psutil
import os


class MemoryModule(Base):
    def name(self):
        return "CPU"

    def full_text(self):
        mem = dict(psutil.virtual_memory()._asdict())

        #print(mem)
        return "Memory: " + str(mem['percent']) + "%"

    def color(self):
        return "#00FF00"
        # if self.cpu < 33:
        #     return "#00FF00"
        # elif self.cpu < 66:
        #     return "#FFFF00"
        # else:
        #     return "#FF0000"