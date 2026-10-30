import sys
import json
from client import GiftConciergeEngine

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "recommend_gifts",
                "description": "Curate personalized gifts within budget constraints based on recipient persona",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "recipient_persona": {"type": "string"},
                        "budget_max": {"type": "number"},
                        "catalog_candidates": {"type": "array"}
                    },
                    "required": ["recipient_persona", "budget_max", "catalog_candidates"]
                }
            }]
        }
    elif method == "tools/call":
        args = req.get("params", {}).get("arguments", {})
        out = GiftConciergeEngine.recommend_gifts(
            args.get("recipient_persona", ""),
            float(args.get("budget_max", 100.0)),
            args.get("catalog_candidates", [])
        )
        return {"content": [{"type": "text", "text": json.dumps(out, indent=2)}]}
    return {"error": "Unsupported method"}

if __name__ == "__main__":
    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()
