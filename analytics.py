import pandas as pd
import sys


class OnlineStoreAnalytics:
    def __init__(self, csv_file):
        try:
            # Load CSV file into a Pandas DataFrame and convert 'order_date' to datetime
            self.df = pd.read_csv(csv_file)
            self.df['order_date'] = pd.to_datetime(self.df['order_date'])
        except FileNotFoundError:
            # Raise a specific exception for FileNotFoundError
            raise FileNotFoundError(f"File not found: {csv_file}")
        except Exception as e:
            # Raise a generic exception with details for any other loading errors
            raise Exception(f"Error loading data: {str(e)}")

    def calculate_monthly_revenue(self):
        try:
            # Create a new column 'month' using the 'order_date' and group by it to calculate monthly revenue
            self.df['month'] = self.df['order_date'].dt.to_period(
                'M')  # .sort_values(ascending=False)
            return self.df.groupby('month')['product_price'].sum()
        except Exception as e:
            # Raise a specific exception for errors during monthly revenue calculation
            raise Exception(f"Error calculating monthly revenue: {str(e)}")

    def calculate_product_revenue(self):
        try:
            # Group by 'product_name' to calculate total revenue for each product
            return self.df.groupby('product_name')['product_price'].sum()
        except Exception as e:
            # Raise a specific exception for errors during product revenue calculation
            raise Exception(f"Error calculating product revenue: {str(e)}")

    def calculate_customer_revenue(self):
        try:
            # Group by 'customer_id' to calculate total revenue for each customer
            return self.df.groupby('customer_id')['product_price'].sum()
        except Exception as e:
            raise Exception(f"Error calculating customer revenue: {str(e)}")

    def get_top_customers(self, n=10):
        try:
            # Use the calculate_customer_revenue method to get total customer revenue and find the top customers
            customer_revenue = self.calculate_customer_revenue()
            return customer_revenue.nlargest(n)
        except Exception as e:
            raise Exception(f"Error getting top customers: {str(e)}")


if __name__ == "__main__":
    try:
        # Create an instance of OnlineStoreAnalytics
        online_store_analytics = OnlineStoreAnalytics('orders.csv')

        # Perform tasks
        monthly_revenue = online_store_analytics.calculate_monthly_revenue()
        product_revenue = online_store_analytics.calculate_product_revenue()
        customer_revenue = online_store_analytics.calculate_customer_revenue()
        top_customers = online_store_analytics.get_top_customers()

        # Display the results
        print("Total Revenue by Month:")
        print(monthly_revenue)
        print("\nTotal Revenue by Product:")
        print(product_revenue)
        print("\nTotal Revenue by Customer:")
        print(customer_revenue)
        print("\nTop 10 Customers by Revenue:")
        print(top_customers)
    except Exception as e:
        # Catch any generic exceptions and print an error message
        print(f"Error: {str(e)}")
