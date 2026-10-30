from client import GiftConciergeEngine

if __name__ == "__main__":
    candidates = [
        {"name": "Mechanical Keyboard", "price": 89.99, "tags": ["tech", "developer", "gamer"]},
        {"name": "Espresso Coffee Blend", "price": 24.50, "tags": ["coffee", "gourmet", "developer"]}
    ]
    res = GiftConciergeEngine.recommend_gifts("developer gamer coffee lover", 100.0, candidates)
    print("Curated Gifts:", res)
