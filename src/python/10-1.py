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

events['numtix']         # extract the numtix column as a series
events['numtix'][2]      # get the value in the numtix column, row 2
events.loc[6]            # extract row with label 6 from the DataFrame
events.loc[6]['numtix']  # get the value in row with label 6, numtix column
events.loc[6, 'numtix']  # the same as the previous, other notation
events.iloc[6]           # extract the row with index/position 6
events.loc[4, 'delivery']

keep = [True, False, True, False, False, False, True] # this is called a mask
events[keep] # we get rows for which the corresponding row (by position) is True
events['discount'] # we get column or row with the label
# Make discount codes consistant
events['discount'] = events['discount'].str.lower()

# Experiment to understand difference between labels and indicies/posistions
# of rows and columns in pandas DataFrame object
# fevents - filter events
# Filtering is a common operation in data analysis as we usually need to work
# on isolated parts of tables
fevents01 = events[keep]
fevents01['numtix'][0] # '2'
#fevents01['numtix'][1] # KeyError: 1
fevents01['numtix'][2] # '5'
#fevents01['numtix'][3] # KeyError: 3
#fevents01['numtix'][4] # KeyError: 4
#fevents01['numtix'][5] # KeyError: 5
fevents01['numtix'][6] # 'three'
fevents01.iloc[0]      # Series object representing first row
fevents01.iloc[1]      # Series object representing second row
#fevents01.iloc[3]      # IndexError: single positional indexer is out-of-bounds
fevents01.iloc[:,0]    # Series object representing first column
fevents01.iloc[:,4]    # Series object representing fifth, last column
#fevents01.iloc[:,5]    # IndexError: single positional indexer is out-of-bounds

# Experiment to understand masks
mask_delivery_email = events['delivery'] == 'email' # Series object with elements of type bool
events[mask_delivery_email]

# Problem: valid discount codes are birthday, student.
# Replace non-valid discount codes with an empty string.
# Plan:
# 1) create a mask of rows with known discount codes
# we do not know "unknown"
valid_codes = ['birthday', 'student']
mask_known_discount_codes = events['discount'].isin(valid_codes)

# 2) invert the mask
"""
The Python Bitwise Not (~) Operator works with a single value
and returns its one’s complement. This means it toggles all
bits in the value, transforming 0 bits to 1 and 1 bits to 0,
resulting in the one’s complement of the binary number.
See also https://wiki.python.org/moin/BitwiseOperators
"""
mask_unknown_discount_codes = ~mask_known_discount_codes
# 3) filter DataFrame to rows without a known discount code
events_unknown_discount = events[mask_unknown_discount_codes]

# 4) replace all the discount column values in that DataFrame with
# an empty string
## events_unknown_discount['discount'] = '' # SettingWithCopyWarning
events.loc[mask_unknown_discount_codes, 'discount'] = ''


# Exercise 10.1.3.1
mask_yes_from_delivery = events['delivery'] == 'yes'
events.loc[mask_yes_from_delivery, 'delivery'] = 'pickup'

# Experiment to understand repairing values and column types
events.loc[6, 'numtix'] = 3
events['numtix'] = events['numtix'].astype('int')
events['numtix'].sum()

# Computing new columns is not a part of OBLIG 3, but can be usefull for OBLIG 5
ticket_price = 10
# Way to create a new column total
events['total'] = events['numtix'] * ticket_price
# Give 10% discount for those with discount "birthday"
bday_mask = events['discount'] == 'birthday'
# Can potentially cast float back to int to avoid problems in future versions
events['total'] = events['total'].astype('int')
events.loc[bday_mask,'total'] = events['total'] * 0.90


# Experimenting with how to get lifting work
events.loc[bday_mask,'total'] = (events['total'] * 0.85).astype('int')
events.loc[bday_mask,'total'] = (events['total'] * 0.66).astype('int')
events.loc[bday_mask,'total'] = (events['total'] * 1.674).astype('int')
events.loc[bday_mask,'total'] = (events['total'] * 1.674).astype('int')
events.loc[bday_mask,'total'] = (events['total'] * 1.674).astype('int')
events.loc[bday_mask,'total'] = (events['total'] * 1.674).astype('int')
type(events['total'][0])


# Experiment to understand writing back to local storage
##events.to_excel("events.xlsx", sheet_name="original-events", index=False)
# OBS! This instruction will destroy / overwrite data
# in the events DataFrame object
##events['discount'] = events['discount'].str.lower()
# Use existing file and add new sheet to it (a - append)
##with pd.ExcelWriter('events.xlsx', mode='a') as writer:
##    events.to_excel(writer, sheet_name="lowercase-discount")

