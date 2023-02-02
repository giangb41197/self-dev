import pandas as pd
from datetime import datetime

# Borrow library

daily_note = pd.read_excel(
    "daily_note.xlsx",
    sheet_name="Time Management",
    skiprows=[0, 1, 2, 3],
    # index_col=[0],
)
daily_note.set_index()
"""daily_note  is data frames
.drop() is pandas function to delete row or collumn
implace = True meaning it is apply on the same data frames"""
# 18- Dec (CK WorldCup, Chủ nhật) change name
# daily_note.replace(to_replace="18- Dec (CK WorldCup, Chủ nhật)", value=None, inplace=True)
# daily_note.loc[daily_note["Date"] == "18- Dec (CK WorldCup, Chủ nhật)"] = "18/12/2022"
print(daily_note)
