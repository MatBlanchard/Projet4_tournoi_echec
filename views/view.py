

class View:
    @staticmethod
    def verify_date(date):
        if "/" not in date:
            return False
        else:
            date = date.split("/")
            if len(date) != 3:
                return False
            for d in date:
                if not d.isnumeric():
                    return False
            if len(str(date[0])) != 2 or len(str(date[1])) != 2 or len(str(date[2])) != 4:
                return False
            return True
