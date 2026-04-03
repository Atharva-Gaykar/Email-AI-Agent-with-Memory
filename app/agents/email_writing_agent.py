from langchain_groq import ChatGroq
from app.tools.email_writing_agent_tools import create_gmail_draft, send_draft_by_id
base_llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0.1,       
)
tools = [create_gmail_draft, send_draft_by_id]
email_agent = base_llm.bind_tools(tools)