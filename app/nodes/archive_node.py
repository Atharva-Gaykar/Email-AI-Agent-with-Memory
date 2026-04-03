from app.state.state import EmailAgentState
from langchain_core.runnables.config import RunnableConfig

def archive_node(state: EmailAgentState,config: RunnableConfig) -> dict:

    print(f"[ARCHIVE] {state['triage_label']} — {state['sender_subject']}")

    
    session=get_session()

    user_id=state['user_id']

    thread_id = config.get("configurable", {}).get("thread_id")

    save_received_email(session, user_id, thread_id,state) 

    return {}