
from langchain_core.prompts import PromptTemplate

analyst_prompt = PromptTemplate.from_template(
'''
You are a senior Wall Street financial analyst.

Stock indicators:

Price: {price}
SMA50: {SMA50}
SMA200: {SMA200}
RSI: {RSI}

Provide:

1. Trend analysis
2. Overbought or oversold evaluation
3. Short-term outlook
4. Long-term outlook
'''
)
