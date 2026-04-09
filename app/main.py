import time
from psycopg import OperationalError
from app.graph import graph
from app.state.state import EmailAgentState
from app.database.connection import pool
import uuid


config = {"configurable": {"thread_id": str(uuid.uuid4()), "user_id": "1"}}

input_data: EmailAgentState = {
    "user_email_id": "gaykaratharva7@gmail.com",
    "user_id": 1,
    "user_name": "Atharva",
    "sender_email_id": "atharvagaykar36@gmail.com",
    "sender_subject": "URGENT: Validation of Hybrid Phishing Detection Model & XGBoost Integration",
    "sender_email_body": """Dear Atharva,\r\n\r\nI have completed the integration of the AI-Driven Email Threat Detection pipeline... [truncated for brevity]"""
}

if __name__ == "__main__":
    result = None
    try:
        # 3. Retry loop for Neon wake-up/stability
        for i in range(3): 
            try:
                print(f"Attempt {i+1}: Invoking graph...")
                result = graph.invoke(input_data, config=config)
                break  # Success! Exit the loop.
            except OperationalError as e:
                if i < 2:
                    print("Waiting for Neon database to wake up...")
                    time.sleep(10) # Increased sleep slightly for Neon cold starts
                else:
                    print("Max retries reached. Database connection failed.")
                    raise e

        # 4. Output the result
        if result:
            print("\n--- Graph Execution Result ---")
            print(result)

    except Exception as e:
        print(f"An error occurred during execution: {e}")

    finally:
        # 5. CRITICAL: Close the pool to prevent "cannot join current thread" error
        print("Closing connection pool...")
        pool.close()
