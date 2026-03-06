
# C4 Level 2 – Container Diagram

```mermaid
flowchart TB
UI[Web Client]
API[FastAPI Gateway]
Orch[LangChain Orchestrator]
Tools[Financial Tools]
Data[Market Data Service]
LLM[LLM Provider]

UI --> API
API --> Orch
Orch --> Tools
Tools --> Data
Orch --> LLM
```
