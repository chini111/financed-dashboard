from data_fetch import fetch_transaction_data
from process_data import process_transactions
from visualize import plot_category_spending
import os

def run():
    print('Fetching data...')
    df=fetch_transaction_data()
    print('Processing data...')
    df,summary=process_transactions(df)
    os.makedirs('reports', exist_ok=True)
    summary.to_csv('reports/summary.csv', index=False)
    print('Generating visualisations...')
    plot_category_spending(summary)
    print('Done!')

if __name__=='__main__':
    run()
