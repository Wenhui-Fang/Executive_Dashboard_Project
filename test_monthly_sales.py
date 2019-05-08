from monthly_sales import to_usd
from monthly_sales import top_selling_products
import os
import pandas

def test_to_usd():
    assert to_usd(6.66) == "$6.66"
    assert to_usd(6) == "$6.00"
    assert to_usd(-6) == "-$6.00"

def test_top_selling_products():
    csv_filepath = os.path.join(os.path.dirname(__file__), "mock_data", "sales-201804.csv")
    sales = pandas.read_csv(csv_filepath)
    results = top_selling_products(sales)
    expected_result = [
        {'name': 'Button-Down Shirt', 'monthly_sales': 6374.90},
        {'name': 'Super Soft Hoodie', 'monthly_sales': 1950.00},
        {'name': 'Khaki Pants', 'monthly_sales': 1246.00},
        {'name': 'Vintage Logo Tee', 'monthly_sales': 1036.00},
        {'name': 'Sticker Pack', 'monthly_sales': 202.50},
        {'name': 'Baseball Cap', 'monthly_sales': 200.97},
        {'name': 'Brown Boots', 'monthly_sales': 125.00}
    ]
    assert results == expected_result