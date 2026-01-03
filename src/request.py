from datetime import datetime

request_counter = 0

class SupportRequest:
    def __init__(self, description):
        # Set the description and state
        self.description = description
        self.state = "submitted"  

        # Increment the request counter and set the ID
        global request_counter
        request_counter += 1
        self.id = request_counter

        # Set the timestamp
        self.created_at = datetime.now()
        
        # Log all changes to this request
        # Each log entry is: (timestamp, action, details)
        self.logs = []
        self.logs.append((datetime.now(), "created", f"Request created with description: {description}"))

   
