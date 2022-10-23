class View:

    def get_user_entry(self, msg_display, msg_error, value_type, assertions=None, embedment=None):
        while True:
            value = input(msg_display)
            if value_type == "selection":
                if value in assertions:
                    return value
                else:
                    print(msg_error)
                    continue
            elif value_type == "date":
                if self.verify_date(value):
                    return value
                else:
                    print(msg_error)
                    continue
            elif value_type == "numeric":
                if value.isnumeric():
                    return value
                else:
                    print(msg_error)
                    continue
            elif value_type == "strictly_positive_numeric":
                if value.isnumeric():
                    if int(value) > 0:
                        return value
                    else:
                        print(msg_error)
                        continue
                else:
                    print(msg_error)
                    continue
            elif value_type == "even_numeric":
                if value.isnumeric():
                    if int(value) % 2 == 0:
                        return value
                    else:
                        print(msg_error)
                        continue
                else:
                    print(msg_error)
                    continue
            elif value_type == "embedded_numeric":
                if value.isnumeric():
                    if embedment[0] <= int(value) <= embedment[1]:
                        return value
                    else:
                        print(msg_error)
                        continue
                else:
                    print(msg_error)
                    continue

    @staticmethod
    def verify_date(date):
        if "/" not in date:
            return False
        else:
            date = date.split("/")
            for d in date:
                if not d.isnumeric():
                    return False
            if len(str(date[0])) != 2 or len(str(date[1])) != 2 or len(str(date[2])) != 4:
                return False
            return True
