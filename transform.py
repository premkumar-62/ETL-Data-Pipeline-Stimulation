def transform_data(data):
    data = data.dropna()
    data["total_sales"] = data["price"] * data["quantity"]
    return data