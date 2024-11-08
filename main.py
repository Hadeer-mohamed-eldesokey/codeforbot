#!/usr/bin/env python
# coding: utf-8

# In[11]:


import json
import requests
from botbuilder.core import ActivityHandler, MessageFactory
from botbuilder.schema import ChannelAccount

class MyBot(ActivityHandler):
    def __init__(self):
        self.scoring_uri = "http://8877b5ca-e8cc-4c8c-89de-cd70256576f4.eastus2.azurecontainer.io/score"

    async def on_message_activity(self, turn_context):
        user_input = turn_context.activity.text
        
        # Prepare payload and headers
        input_data = {"input_text": user_input}
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}" if self.api_key else None
        }
        
        # Send request to the model
        try:
            response = requests.post(self.scoring_uri, headers=headers, data=json.dumps(input_data))
            if response.status_code == 200:
                model_response = response.json().get("response", "Sorry, I didn't understand that.")
            else:
                model_response = f"Error {response.status_code}: {response.text}"
        except Exception as e:
            model_response = f"Request failed: {e}"
        
        # Send model response back to user
        await turn_context.send_activity(MessageFactory.text(model_response))


# In[ ]:




