from base import Base
from os import statvfs


class DiskSpaceFreeModule(Base):
    def name(self):
        return "time"

    def full_text(self):
        char = "B"
        stat = statvfs("/")

        block_size = stat.f_bsize
        free = stat.f_bfree * block_size

        percentage = stat.f_bfree / stat.f_blocks

        if free >= 1024:
            free /= 1024
            char = "KB"

        if free >= 1024:
            free /= 1024
            char = "MB"

        if free >= 1024:
            free /= 1024
            char = "GB"

        return "Free: " + str(free)[:5] + char + " " + str(percentage * 100)[:5] + "%"
