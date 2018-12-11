from base import Base
import communicate


class CommsModule(Base):
    def name(self):
        return "comms"

    def full_text(self):
        result = ""
        data = communicate.request("daan")
        for key, val in data.items():
            result += "  " + key.split('_')[0] + ": " + val
        return result
