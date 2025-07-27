import json
import re
from models.main_agent import run_local_llm
from models.trade_signal import TradeSignal

# Utility to safely convert to float or leave as-is
def safe_float(val):
    try:
        return float(str(val).replace("+", "").replace("$", "").strip())
    except Exception:
        return val

# Utility to parse entry_range from string or list
def parse_entry_range(raw):
    if isinstance(raw, list):
        return [safe_float(v) for v in raw]
    if isinstance(raw, str) and "-" in raw:
        parts = raw.replace("$", "").split("-")
        try:
            return [float(parts[0].strip()), float(parts[1].strip())]
        except Exception:
            return raw
    return raw

def fusion_analysis(coin, price_out, news_out, twitter_out):
    prompt = f"""You are an expert crypto trader with 6 years of experience in crypto Futures and Spot trading. Based on the following data for {coin}:
- Price Analysis: {price_out}
- News Sentiment: {news_out}
- Twitter Sentiment: {twitter_out}

Respond ONLY with a valid JSON object like this:

{{
  "symbol":
  "recommendation":Long or Short,
  "timeframe": "
  "position_type": "Spot or Futures",
  "entry_range": [],
  "dca":
  "stoploss":
  "targets": [],
  "analysis": "Explain the reasoning behind this signal...",
  "note": "Trade at your own risk this is not a financial advice."
}}

Do NOT include any explanation, markdown, or extra text — ONLY the JSON.
"""

    llm_response = run_local_llm(prompt)
    llm_content = getattr(llm_response, "content", llm_response)

    # Extract the JSON from the output
    match = re.search(r"\{.*\}", llm_content, re.DOTALL)
    if not match:
        print("❌ Failed to extract JSON from LLM response.")
        print("🔍 Raw output:", llm_content)
        return "Error: No JSON found."

    json_str = match.group(0)

    try:
        parsed = json.loads(json_str)

        # ✅ Clean/sanitize fields
        parsed["entry_range"] = parse_entry_range(parsed.get("entry_range"))
        parsed["dca"] = safe_float(parsed.get("dca"))
        parsed["stoploss"] = safe_float(parsed.get("stoploss"))
        parsed["targets"] = [safe_float(t) for t in parsed.get("targets", [])]

        signal = TradeSignal(**parsed)
        return signal.render()

    except Exception as e:
        print("❌ JSON parse error:", e)
        print("🔍 Cleaned JSON string:", json_str)
        return "Error: Invalid JSON structure."
