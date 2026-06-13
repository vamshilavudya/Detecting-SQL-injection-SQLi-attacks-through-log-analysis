import re

def detect_sqli(query):
    if not query:
        return "Safe ✅"

    # normalize
    q = query.lower().strip()
    q = q.replace("\n", " ")   # 🔥 CRITICAL FIX (remove newline issue)
    q = q.rstrip(";")

    # ✅ allow normal UNION queries first
    if "union select" in q:
        # only block if sensitive data extraction
        if any(word in q for word in ["password", "admin", "user", "login", "credit"]):
            return "Malicious ❌"
        else:
            return "Safe ✅"

    # other attacks
    if re.search(r"\bor\s+1=1\b", q):
        return "Malicious ❌"

    if re.search(r"\band\s+1=1\b", q):
        return "Malicious ❌"

    if re.search(r";\s*(drop|delete|insert|update)\b", q):
        return "Malicious ❌"

    if re.search(r"sleep\s*\(", q):
        return "Malicious ❌"

    return "Safe ✅"