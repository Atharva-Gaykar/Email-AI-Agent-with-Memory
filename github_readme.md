<h1 align="center">📧 AI-Driven Email Agent 🧠</h1>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-0.118-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/LangGraph-StateGraph-1C3C3C?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Groq-LLM-F55036?style=for-the-badge"/>
<img src="https://img.shields.io/badge/PostgreSQL-16-336791?style=for-the-badge&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/Neon-Serverless-31EFB8?style=for-the-badge"/>
<img src="https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=for-the-badge"/>
<img src="https://img.shields.io/badge/LangMem-Memory-FFD21E?style=for-the-badge"/>
<img src="https://img.shields.io/badge/SentenceTransformers-Embeddings-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black"/>
<img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/HuggingFace-Spaces-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black"/>
</p>

<p align="center">
Multi-agent email automation using LangGraph, FastAPI, semantic memory, interrupt-driven workflows, and custom threat detection.
</p>

---

## 🚀 Overview

This system intelligently automates:

- Email triage  
- Context retrieval from long-term memory  
- Professional draft generation  
- Human-in-the-loop review workflows  

Advanced implementations include:

- 🧠 Semantic Memory Management  
- 💾 State Persistence  
- ⏸️ Human-in-the-Loop Interrupts  
- 🔐 Custom Email Threat Detection  
- 🚀 Production-Ready Orchestration

---

## ✨ Key Features

## 🤖 Advanced Multi-Agent Architecture

### Graph Workflow Diagram

<p align="center">
  <img src="https://github.com/user-attachments/assets/5d17b94a-200d-437f-b1c6-83558359d963" width="700"/>
</p>


### Triage Agent

Determines intent using productivity-focused labels:

- **FOLLOW_UP_REQUIRED** — Action or reply required  
- **READ_LATER** — Informational, no action needed  
- **CHECK_LATER** — Cold outreach or unknown sender  
- **PROMOTIONAL** — Marketing or sales content  
- **FYI_NOTIFICATION** — Automated alerts or confirmations  

Also assigns priority scores for downstream routing.

---

### Context Agent

- Performs multi-query semantic retrieval  
- Finds relevant historical interactions  
- Synthesizes retrieved memory into response context

---

### Writing Agent

- Crafts contextual replies  
- Supports user feedback loops  
- Regenerates drafts through interrupt-driven review

---

## 🧠 Semantic Memory System

The agent doesn’t just process emails — it learns from them.

- Powered by **langmem + PostgreSQL (Neon)**  
- Stores interaction summaries with embeddings  
- Remembers project details from historical interactions  
- Grounds replies in prior context

---

## 💾 State Persistence & Recovery

### PostgreSQL Checkpointer

Every graph step is snapshotted.

**Resilience**  
If the system restarts, execution resumes exactly where it stopped.

**Auditability**  
Every AI decision is stored in a structured audit trail.

---

## ⏸️ Human-in-the-Loop Review

Uses LangGraph’s `Command(resume=...)` interrupt pattern.

### Flow

1. Graph pauses after drafting  
2. User reviews draft  
3. User approves or rejects  
4. Draft sends or regenerates with feedback

```python
if user_approved:
    payload = Command(
        resume={"status": "approved"}
    )
else:
    payload = Command(
        resume={
            "status": "rejected",
            "feedback": "Add more detail about cost."
        }
    )

final_state = graph.invoke(payload, config=config)
```

---

## 🔐 Custom Email Threat Detection

Safety classification is powered by a hybrid model.

### Model
- DistilBERT text embeddings  
- XGBoost URL numerical features

### Performance
**99.35% test accuracy**

### Protection
Detects:

- Phishing attempts  
- Malicious URLs  
- Unsafe inbound content before triage

---

## 📖 Full Threat Detection Implementation

Repository:  
[AI-Driven Email Threat Detection](https://github.com/Atharva-Gaykar/AI-Driven-Email-Threat-Detection)

---

## 🛠️ Architecture Stack

| Layer | Technology | Purpose |
|------|------------|---------|
| Orchestration | LangGraph Functional API | Stateful workflows with interrupts |
| LLM | Groq (Llama 3.1 / Mixtral) | Agentic reasoning |
| Memory | langmem + PostgreSQL | Long-term semantic persistence |
| Embeddings | Sentence Transformers | Vector retrieval |
| Security | DistilBERT + XGBoost | Threat classification |
| Database | PostgreSQL 16 (Neon) | Checkpointing + PostgresStore |
| API | FastAPI 0.118 | Async endpoints |
| Containers | Docker | Environment orchestration |

---

## 🔄 Graph Architecture

*(Add LangGraph workflow diagram here)*

## Workflow Nodes

### `safety_check_node`
Identifies phishing or unsafe content.

### `check_token_count_node`
Checks whether email exceeds context limits.

### `summarise_email_body_node`
Summarizes long emails.

### `triage_node`
Categorizes email and assigns priority.

### `check_previous_email_exist_node`
Determines whether semantic retrieval is needed.

### `prepare_context_node`
Builds prompt-ready context.

### `email_writing_agent`
Generates draft and triggers interrupt review.

### `tools`
Interfaces with Gmail API:

- Draft creation  
- Final sending

### `store_memory_and_data_node`
Stores final interaction into semantic memory.

### `archive_node`
Moves processed emails into history.

### `unsafe_emails_node`
Quarantines threats for administrator review.

---

## 🧠 Memory Namespace Strategy

```python
namespace = ("emails", user_id, "collection")
```

Scoped namespaces ensure privacy and retrieval precision.

---

## 🎯 Implementation Highlights

### LangGraph Functional API
Moved beyond simple chains into stateful interactive graphs.

### Persistent Checkpointing
Solved state-loss in stateless cloud deployments.

### Semantic Memory
Bridged short-term context with long-term knowledge.

### Resilient API Design

Implemented:

- Retry loops for serverless PostgreSQL (Neon)  
- Connection pooling in FastAPI

---

## 🎓 Learning Journey

Through this project I deepened expertise in:

- LangGraph Functional API  
- Interrupt-driven workflows  
- PostgreSQL checkpoint persistence  
- Semantic memory systems  
- FastAPI backend resilience  
- Hybrid ML security pipelines

---

## 👨‍💻 Author

**Atharva Gaykar**
