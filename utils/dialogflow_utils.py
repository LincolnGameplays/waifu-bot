from google.cloud import dialogflow_v2 as dialogflow
import os

def get_dialogflow_response(user_id, text, project_id, language_code="pt-BR"):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, f"tg-{user_id}")
    
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    
    return response.query_result.fulfillment_text
