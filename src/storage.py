"""
Storage system for support requests.

This keeps all requests in memory (a list).
Later we can add file saving to make it persistent.
"""

# This list holds all our support requests
requests = []


def add_request(description):
    """Create a new support request and add it to storage."""
    from request import SupportRequest
    req = SupportRequest(description)
    requests.append(req)
    return req


def get_all_requests():
    """Get all support requests."""
    return requests


def get_request_by_id(request_id):
    """Find a request by its ID."""
    for req in requests:
        if req.id == request_id:
            return req
    return None


def change_state(request_id, new_state):
    """Change a request's state and log the change."""
    from datetime import datetime
    req = get_request_by_id(request_id)
    if req:
        old_state = req.state
        req.state = new_state
        # Log this state change
        req.logs.append((datetime.now(), "state_changed", f"Changed from '{old_state}' to '{new_state}'"))
        return True, old_state
    return False, None

