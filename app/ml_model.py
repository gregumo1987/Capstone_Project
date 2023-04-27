import random

# This function simulates fetching raw financial data for a company
def fetch_data(company_name):
    return {
        "revenue": [random.uniform(1000, 10000) for _ in range(12)],
        "liquidity_ratio": [random.uniform(1, 3) for _ in range(12)],
        "profitability": [random.uniform(0.1, 0.5) for _ in range(12)],
        "return_on_investment": [random.uniform(0.05, 0.15) for _ in range(12)],
        "cost_of_goods_sold": [random.uniform(500, 5000) for _ in range(12)],
        "sales_by_product": [[random.uniform(100, 1000) for _ in range(12)] for _ in range(5)],
        "budget_variance": [random.uniform(-1000, 1000) for _ in range(12)]
    }

# This function processes the raw financial data to generate KPI data and chart data
def process_kpi_data(raw_data):
    kpi_data = [
        {"name": "Revenue", "value": sum(raw_data["revenue"])},
        {"name": "Liquidity Ratio", "value": sum(raw_data["liquidity_ratio"]) / len(raw_data["liquidity_ratio"])},
        {"name": "Profitability", "value": sum(raw_data["profitability"]) / len(raw_data["profitability"])},
        {"name": "Return on Investment", "value": sum(raw_data["return_on_investment"]) / len(raw_data["return_on_investment"])},
        {"name": "Cost of Goods Sold", "value": sum(raw_data["cost_of_goods_sold"])},
        {"name": "Sales by Product", "value": [sum(product_sales) for product_sales in raw_data["sales_by_product"]]},
        {"name": "Budget Variance", "value": sum(raw_data["budget_variance"])}
    ]

    chart_data = [
        {
            "labels": [f"Month {i + 1}" for i in range(12)],
            "datasets": [
                {
                    "label": "Revenue",
                    "data": raw_data["revenue"],
                    "backgroundColor": "rgba(75, 192, 192, 0.2)",
                    "borderColor": "rgba(75, 192, 192, 1)",
                    "borderWidth": 2
                }
            ]
        },
        # Other chart data for additional KPIs can be added here
    ]

    return kpi_data, chart_data