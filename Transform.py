import pandas as pd
import re

import re
def extract_price(text):
    match = re.search(r'\d+\.\d+|\d+', text)
    if match:
        return float(match.group())
    else:
        return None  
def Transform(filename) :
    data = pd.read_json(f"DATA/{filename}")
    data = data.T.reset_index()
    data.rename(columns={"index": "Product"}, inplace=True)



    data['prix'] = data['prix'].apply(lambda x : extract_price(x))

    data['commission'] = data['commission'].apply(lambda x : extract_price(x))
    fileName = filename.split(".")[0]
    data.to_csv(rf"./DATA/{fileName}.csv",  index=False)
