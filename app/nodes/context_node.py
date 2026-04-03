from langchain_core.messages import AIMessage
from app.agents.context_agent import context_agent
from app.prompts.context_agent_prompt import context_agent_template
from app.state.state import EmailAgentState
from langgraph.types import RunnableConfig

def prepare_context_node(state: EmailAgentState,config: RunnableConfig):

    """This node retrieves past context and prepares the prompt for the drafting agent."""
    print("DEBUG: Executing prepare_context_node...")

    prompt_value = context_agent_template.invoke({
        "user_name":      state["user_name"],
        "user_email_id": state["user_email_id"], 
        "senders_email": state["sender_email_id"],
        "subject":       state["sender_subject"],
        "body":          state["sender_email_body"],
        "triage_label":  state["triage_label"],
        "priority_score":state["priority_score"],
    })

    prompt = prompt_value.to_messages()

    
    context_agent_response = context_agent.invoke({"messages": prompt},config=config)

    draft_context = ""
    
    for msg in context_agent_response["messages"]:
       
        if msg.type == "tool" and msg.name == "give_previous_context":
            draft_context = msg.content
            break
        
        elif isinstance(msg, AIMessage) and not msg.tool_calls and not draft_context:
            draft_context = msg.content

    print(f"DEBUG: draft_context = {draft_context[:100] if draft_context else 'NOT FOUND'}")

    return {
        "context_agent_messages":      context_agent_response["messages"],
        "draft_context": draft_context,
    }