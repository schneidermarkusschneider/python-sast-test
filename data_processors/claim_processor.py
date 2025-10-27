import json

class ClaimProcessor:
    def parse_claims(self, claims_str):
        try:
            claims = json.loads(claims_str)
            return claims
        except:
            return {}
