class TA:
    gr_resp: str
    name: str
    def __init__(self, gr_resp, name):
        self.name = name
        self.gr_resp = gr_resp
    

ta_1 = TA("Gr1, Gr2", "Tom")

class GroupWork:
    ta : TA
    room_id : str
    def __init__(self, ta, room_id):
        self.ta = ta
        self.room_id = room_id
    
gw_1 = GroupWork(ta_1, "F1 022")

print(gw_1.ta.name)