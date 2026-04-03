import re
from langchain_core.messages import ToolMessage
from app.state.state import EmailAgentState


def parse_response_node(state: EmailAgentState) -> dict:
    messages = state["messages"]
    updates = {}
    
    # 1. Find the successful SEND message to get the ID
    # We scan backwards for the first ToolMessage from 'send_draft_by_id'
    send_tool_msg = next((m for m in reversed(messages) 
                         if isinstance(m, ToolMessage) and m.name == "send_draft_by_id"), None)
    
    if send_tool_msg and "SUCCESS" in send_tool_msg.content.upper():
        id_match = re.search(r'<id>(.*?)</id>', send_tool_msg.content)
        if id_match:
            updates["sent_message_id"] = id_match.group(1)

    # 2. Find the most recent successful DRAFT creation
    # This is the "lookback" that ignores all the rejections and rewrites
    draft_tool_msg = next((m for m in reversed(messages) 
                          if isinstance(m, ToolMessage) and m.name == "create_gmail_draft" 
                          and "Successfully" in m.content), None)

    if draft_tool_msg:
        # Extract the content from the tags you defined in the tool
        subject_match = re.search(r'<subject>(.*?)</subject>', draft_tool_msg.content)
        body_match = re.search(r'<body>(.*?)</body>', draft_tool_msg.content, re.DOTALL)
        
        if subject_match:
            updates["reply_subject"] = subject_match.group(1)
        if body_match:
            updates["reply_email_body"] = body_match.group(1)

    # 3. Final Safety: If we still don't have a body, don't return 'None'
    if not updates.get("reply_email_body"):
        updates["reply_email_body"] = "Content could not be retrieved from history."

    return updates