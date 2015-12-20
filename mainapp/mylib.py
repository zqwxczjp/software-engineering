class AddFriendReq:
    username = ''
    id = -1
    ReqDir = 0
    def __init__(self, x_name, x_id, x_ReqDir):
        self.username = x_name
        self.id = x_id
        self.ReqDir = x_ReqDir