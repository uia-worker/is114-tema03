class TA:
    gr_resp: str
    name: str
    def __init__(self, gr_resp, name):
        self.name = name
        self.gr_resp = gr_resp
    

ta_1 = TA("Gr1, Gr2", "Tom")
ta_2 = TA("Gr3, Gr4", "Ane")
ta_3 = TA("Gr5, Gr6", "Ask")

class GroupWork:
    ta : TA
    room_id : str
    def __init__(self, ta, room_id):
        self.ta = ta
        self.room_id = room_id
    
gw_1 = GroupWork(ta_1, "F1 022")
gw_2 = GroupWork(ta_2, "F1 023")
gw_3 = GroupWork(ta_3, "F1 018")
gw = [gw_1, gw_2, gw_3]

# Hva er problematisk med denne koden?
def get_room_nr(ta_name : str, gw_list : list) -> str:
    for elt in gw_list:
        print(elt.ta.name)
        if elt.ta.name == ta_name:
            return elt.room_id
    return "no TA in list"

def test_get_room_nr():
    assert get_room_nr("Ask", gw) == "F1 018"
    assert get_room_nr("Ask", []) == "no TA in list"
    assert get_room_nr("Tom", gw) == "F1 022"
    assert get_room_nr("Ane", gw) == "F1 023"
    assert get_room_nr("Tor", gw) == "no TA in list"
    
