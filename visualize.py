import matplotlib.pyplot as plt
import os

def plot_category_spending(summary_df):
    os.makedirs('reports', exist_ok=True)
    summary_df.plot(kind='bar', x='category', y='net_total')
    plt.title('Spending by Category')
    plt.ylabel('Total Spent ($)')
    plt.tight_layout()
    plt.savefig('reports/spending_breakdown.png')
    plt.close()
