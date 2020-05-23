from enum import Enum

class Authority(Enum):
    Super = 0
    Developer = 1
    Usual = 2
    Invalid = -1

class UserInfo:
    def __init__(self, name, password, accountID, authority, **kwargs):
        self.name = name
        self.password = password
        self.accountID = accountID
        self.authority = authority
        for k, v in kwargs.items():
            self.__dict__[k] = v