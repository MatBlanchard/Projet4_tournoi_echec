from datetime import *

class View:
    @staticmethod
    def get_date(value):
        if "-" not in value:
            raise ValueError("Expected format : DD-MM-YYYY")
        values = value.split("-")
        return date(int(values[2]), int(values[1]), int(values[0]))

    @staticmethod
    def verify_hour(hour):
        if ":" not in hour:
            return False
        else:
            hour = hour.split(":")
            if len(hour) != 2:
                return False
            for h in hour:
                if not h.isnumeric():
                    return False
            if int(hour[0]) < 0 or int(hour[1]) < 0:
                return False
            if int(hour[0]) > 23 or int(hour[1]) > 59:
                return False
            return True
