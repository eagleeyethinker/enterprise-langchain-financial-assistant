
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain_openai import ChatOpenAI
from tools.stock_price_tool import stock_analysis

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)

tools = [stock_analysis]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)
