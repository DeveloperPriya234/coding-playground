#WAF to convert USD to :
# 1usd = 83inr


def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD =",inr_val,"INR")
    
converter(65)