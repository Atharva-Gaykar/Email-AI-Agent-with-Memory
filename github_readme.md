📧 AI-Driven Email Agent 🧠

A production-grade, multi-agent system built with LangGraph and FastAPI that automates email triage, context retrieval, and drafting. This project demonstrates advanced implementation of Long-term Memory, State Persistence, and Human-in-the-Loop Interrupts using LangGraph's Functional API Command pattern.

🚀 Key Features

Advanced Learning Implementation: Throughout this project, I successfully implemented Semantic Memory, Checkpointer Persistence, and Functional Interrupts, allowing the agent to maintain state and handle user feedback reliably.

Multi-Agent Workflow: Specialized agents for Triage, Context Synthesis, and Email Drafting.

Intelligent Triage: Automatically classifies emails, assigns priority, and determines if a reply is required.

Semantic Memory: Uses langmem and PostgresStore to retrieve past interactions, ensuring the agent "remembers" previous project details.

Resource Management: A dedicated Token Count Node ensures large emails (like deployment logs) are summarized before processing to optimize costs.

Human-in-the-Loop: The graph pauses using interrupt() to allow users to review, approve, or provide feedback on drafts via Command(resume=...).

Scalable Architecture: Built with FastAPI, Docker, and a modular folder structure for enterprise-level deployment.

🛠️ Tech Stack

Orchestration: langgraph (Functional API), langchain

LLM Interface: langchain-groq 

Memory & Persistence: langmem, PostgresCheckpoint, PostgresStore (via Neon/PostgreSQL)

Database ORM: SQLAlchemy 2.0

Embeddings: langchain_huggingface (DistilBERT)

Backend: FastAPI + Uvicorn

Configuration: pydantic-settings (Type-safe .env management)

Authentication: google-auth (Gmail API Integration)

📂 Project Structure

app/
├── agents/             # Brains: Specialized LLM logic (Triage, Writer, Context)
├── database/           # Data: SQLAlchemy models and Connection Pooling
├── nodes/              # Workflow: Functional steps of the graph (Safety, Tokens)
├── persistance/        # Persistence: Postgres Checkpointer & Memory Store config
├── state/              # Schema: Pydantic & TypedDict state definitions
├── utils/              # Toolbox: Token counters, Embeddings, and Auth helpers
├── graph.py            # Logic: StateGraph construction and compilation
└── main.py             # Entry: FastAPI app and Controller logic


🔄 Graph Architecture

The system follows a pre-processing pipeline before reaching the agentic loop:

Safety Check: Filters out malicious content.

Token Check: Routes large bodies to a Summarization Node.

Triage: Analyzes intent and priority.

Context Retrieval: Queries PostgresStore for relevant past facts.

Drafting Agent: Creates a reply based on the full context.

Interrupt: Pauses for User Review and feedback.

🛡️ Integrated Security

The safety classification in this agent is informed by my specialized project on threat detection:

Hybrid Phishing Detection Model: GitHub Repository

👨‍💻 Author

Atharva Gaykar AI Engineer | IIIT Nagpur

