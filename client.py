"""Autonomous Gift Concierge Engine.
100% Python Standard Library.
"""

class GiftConciergeEngine:
    """Matches recipient persona, interests, and budget constraints to curate gift ideas."""

    @staticmethod
    def recommend_gifts(recipient_persona: str, budget_max: float, catalog_candidates: list) -> dict:
        persona_tokens = set(recipient_persona.lower().split())
        matched = []

        for item in catalog_candidates:
            price = float(item.get("price", 0.0))
            if price > budget_max:
                continue
            tags = set(t.lower() for t in item.get("tags", []))
            overlap = len(persona_tokens.intersection(tags))
            score = overlap * 10.0 + (100.0 - (price / max(1.0, budget_max)) * 20.0)
            matched.append({
                "product_name": item.get("name"),
                "price": price,
                "relevance_score": round(score, 1),
                "affinity_tags": list(tags)
            })

        matched.sort(key=lambda x: x["relevance_score"], reverse=True)
        return {
            "recipient_persona": recipient_persona,
            "budget_max": budget_max,
            "curated_gifts_count": len(matched),
            "recommendations": matched[:5]
        }
