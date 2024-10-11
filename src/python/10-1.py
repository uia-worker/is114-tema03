# Eksperimentering med kode fra kap. 10.1 (DCIC) (platform = Apple M2 Pro + macOS Sonoma 14.3.1)
import pandas as pd

events_url = "https://raw.githubusercontent.com/data-centric-computing/dcic-public/main/materials/datasets/events.csv"
events = pd.read_csv(events_url, header=0,
                     names=['name','email','numtix','discount','delivery'])


# indice - an indication, sign, token.
# index - (in computing) To modify (an instruction or its address)
# by causing the contents of a specified index register to be added
# to the address before the instruction is executed; to provide with
# a number that brings about such modification; also, to carry out
# (a repetitive sequence of operations) by this means.



