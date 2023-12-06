
import random
import pandas as pd
from datetime import datetime, timedelta

# Function to generate random dates
def random_date(start_date, end_date):
    return (start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )).strftime('%Y-%m-%d')

# Generate test data
order_ids = list(range(1, 21))
customer_ids = [random.randint(101, 110) for _ in range(20)]
order_dates = [random_date(datetime(2023, 1, 1), datetime(2023, 12, 31)) for _ in range(20)]
product_ids = list(range(201, 211))
product_names = ['ProductA', 'ProductB', 'ProductC', 'ProductD', 'ProductE',
                 'ProductF', 'ProductG', 'ProductH', 'ProductI', 'ProductJ']
product_prices = [10.0, 20.0, 15.0, 25.0, 30.0, 12.0, 18.0, 22.0, 28.0, 35.0]
quantities = [random.randint(1, 5) for _ in range(20)]

test_data = {
    'order_id': order_ids,
    'customer_id': customer_ids,
    'order_date': order_dates,
    'product_id': product_ids * 2,  # Repeating product IDs to match 20 orders
    'product_name': random.choices(product_names, k=20),
    'product_price': random.choices(product_prices, k=20),
    'quantity': quantities,
}

print(test_data)
df = pd.DataFrame(test_data)
df.to_csv('orders.csv', index=False)
