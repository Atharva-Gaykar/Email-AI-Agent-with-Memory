from langchain_core.prompts import ChatPromptTemplate

memory_agent_template = ChatPromptTemplate([
    ("system", """<username>{user_name}</username>.<user_email_id>{user_email_id}</user_email_id>

"""),

    ("human", """
<incoming_email>
From: {senders_email_id}
To:User
Body: {incoming_email_body}
</incoming_email>
<reply_email>
From:User
To: {senders_email_id}
Body: {sent_email_body}  
</reply_email>    
"""),
])