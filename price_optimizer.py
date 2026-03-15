def optimize_price(predicted_demand, base_price):

    if predicted_demand > 250:
        return base_price * 1.15

    elif predicted_demand > 200:
        return base_price * 1.05

    else:
        return base_price * 0.95