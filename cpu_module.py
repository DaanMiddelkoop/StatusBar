from base import Base
import psutil
import os


class CpuPercent:
    cpu = psutil.cpu_percent(percpu=True)

    def refresh_cpu(self):
        self.cpu = psutil.cpu_percent(percpu=True)
        return self.cpu

    def get_cpu(self):
        return self.cpu

cpu = CpuPercent()


class CpuModule(Base):
    cpu = 0.0
    core = 0

    def __init__(self, core):
        self.core = core

    def name(self):
        return "CPU"

    def full_text(self):
        self.cpu = cpu.get_cpu()[self.core]
        return "Core " + str(self.core) + ": " + str(self.cpu) + "%"

    def color(self):
        if self.cpu < 33:
            return "#00FF00"
        elif self.cpu < 66:
            return "#FFFF00"
        else:
            return "#FF0000"

    def min_width(self):
        return "Core 0: 100.0%"


class OwnCpuUsage(Base):
    cpu = 0.0
    process = psutil.Process(os.getpid())

    def name(self):
        return "OwnCPU"

    def full_text(self):
        self.cpu = self.process.cpu_percent()
        return "Status Bar cpu usage: " + str(self.cpu)

    def color(self):
        if self.cpu < 33:
            return "#00FF00"
        elif self.cpu < 66:
            return "#FFFF00"
        else:
            return "#FF0000"