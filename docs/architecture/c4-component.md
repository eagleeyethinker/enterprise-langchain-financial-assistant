
# C4 Level 3 – Component Diagram

```mermaid
flowchart TB
Prompt[Prompt Templates]
Agent[Financial Agent]
Indicators[Technical Indicator Engine]
Retriever[Stock Data Retriever]
LLM[LLM Analysis]

Prompt --> Agent
Agent --> Retriever
Retriever --> Indicators
Agent --> LLM
```
