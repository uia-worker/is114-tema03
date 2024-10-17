import pandas as pd
from write_with_pandas_to_excel import *

# ----------------  Innhenting og Vasking --------------------------------------
# Hvis man "graver dypt nok i Python moduler (pandas i dette tilfelle),
# man kan finne litt "gull", som na_values, som gjør "vasking" av
# barnehagedata mye mer effektiv.
# Siden vi visste om celler med "." og "..", så kan vi erstatte de med "nan", samtidig som
# vi henter inn data i minnerommet til vårt program.
# Med names kan vi også gjøre kolonnenavn (merkelapper i pandas DataFrame objektet)
# kortere, slik at koden er mer kompakt. "kom" står for kommune og y står for year.
# header=3 gjør at vi ikke henter inn de tre første radene fra excel-filen.
# Med sheet_name kan vi velge hvilken arbeidsbok vi ønsker å hente inn (i tilfeller det
# er flere i excel-filen).
# Navn til DataFrame objektet, som refererer til all data er kgdata - kindergarden data.
kgdata = pd.read_excel("ssb-barnehager-2015-2023-alder-1-2-aar.xlsm", sheet_name="KOSandel120000",
                       header=3,
                       names=['kom','y15','y16','y17','y18','y19','y20','y21','y22','y23'],
                       na_values=['.', '..'])

# Vi oppdaget også at en del av data var ikke korrekte, dvs. verdiene var over 100%, som
# kun kan være en situasjon hvor antall innbyggere i 1-2 årsalderen i en kommune er mindre
# enn antal barn i 1-2 årsalderen registrert med en plass i barnehagen ...
# Forslaget er å vaske ut (erstatte med NaN) verdier større enn 100:
for coln in ['y15','y16','y17','y18','y19','y20','y21','y22','y23']:
    mask_over_100 = (kgdata[coln] > 100) # Kan bli et typeproblem?
    kgdata.loc[mask_over_100, coln] = float("nan")
# --- mer vasking? ----
# Trenger mer vasking (finner ut etter en feilmelding på typefeil
# kgdata[['Modalen' in row for row in kgdata['kom']]]
# Men denne type vasking kan gi problemer, f. eks., hvis man bruker innebygde
# funksjoner for behandling av strenger, som str og split ...
# kgdata.loc[724:779, 'kom'] = "NaN"
kgdata.loc[724:779], 'kom'] = float("nan")

# Filtrerer ut kun navn på kommunbe fra kom feltet og setter kom lik denne verdien
# F. eks. erstatter '3001 Halden' med 'Halden' osv.
# Denne tolker "NaN" som en streng og derfor returnerer en array med ett element
#kgdata["knavn"] = kgdata['kom'].str.split(" ").apply(lambda x: x[1])
# Endring (forutsetter følgende fromat på kom-kolonne: 'KOM-NR KOM-NAVN ...', dvs. at
# lengden på array etter splitting av strenger er større enn 1
# "NaN" gir en array med lengde 1, derfor skal den ignoreres
kgdata["kom"] = kgdata['kom'].str.split(" ").apply(lambda x: x[1] if len(x) > 1 else "")

# Dette må gjøres for å unngå ikke relevante felt i vid tabell
kgdata_no_meta = kgdata.drop(kgdata.index[724:])

write_pandas_dataframe_to_excel_worksheet_with_nan(kgdata_no_meta,
                                                   "ssb-barnehager-2015-2023-alder-1-2-aar.xlsm",
                                                   "VASKET")

