import pandas as pd

def process_transactions(df):
    df['category']=df['title'].apply(lambda x: x.split()[0])
    df['net_total']=df['total']*(1-df['discount']/100)
    summary=df.groupby('category')['net_total'].sum().reset_index()
    return df, summary
