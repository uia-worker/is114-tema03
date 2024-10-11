import gspread as gs
import pandas as pd
import numpy as np
import altair as alt

# Få tilgang til Google Cloud (gc)
gc = gs.api_key("") # etterspør API key hos lærer
# Laste inn hele regnarket fra Google Drive i variabelen sh (spread[sh]eet)
sh = gc.open_by_key('1RYN0i4Zx_UETVuYacgaGfnFcv4l9zd9toQTTdkQkj7g')
# Velge et spesifikt ark fra regnarket (wsh - [w]ork[sh]eet)
wsh = sh.worksheet("o1-oppg3")
print(sh.worksheets())
# Laste inn (binde til navnet df) data fra wsh i dataramme (df - [d]ata[f]rame)
df = pd.DataFrame(wsh.get_all_records())
# Eksempel på bruken av det populære matematikk-pakken numpy
# Binder data til navnet array
array = np.array(wsh.get_all_values())


# Presentere data
chart = alt.Chart(df).mark_bar(
).encode(
    x = 'age:Q',     
    y = 'first_name:N' 
)
 
chart.save('bar-chart.html')
