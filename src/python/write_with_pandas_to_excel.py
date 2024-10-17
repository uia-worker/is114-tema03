import pandas as pd
def write_pandas_dataframe_to_excel_worksheet_with_nan(pandas_df, file_name, wsh_name):
    with pd.ExcelWriter(file_name, mode='a') as writer:
        pandas_df.to_excel(writer, sheet_name=wsh_name, na_rep='nan')
