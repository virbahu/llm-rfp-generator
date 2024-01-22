import numpy as np
def calculate_rfp_score(responses):
    scored = []
    for r in responses:
        price_s = (1 - r["price"]/max(p["price"] for p in responses)) * 40
        quality_s = r.get("quality",80)/100 * 30
        delivery_s = (1 - r.get("lead_time",14)/30) * 20
        terms_s = r.get("terms_score",70)/100 * 10
        total = price_s + quality_s + delivery_s + terms_s
        scored.append({"vendor": r["vendor"], "score": round(total, 1), "price": r["price"]})
    return sorted(scored, key=lambda x: -x["score"])
if __name__=="__main__":
    bids = [{"vendor":"A","price":50000,"quality":95,"lead_time":10,"terms_score":85},{"vendor":"B","price":42000,"quality":88,"lead_time":14,"terms_score":70},{"vendor":"C","price":55000,"quality":98,"lead_time":7,"terms_score":90}]
    for r in calculate_rfp_score(bids): print(r)
