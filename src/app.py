"""
Flask web application for ITPath.

This provides a web interface for the IT support system.
Uses the existing storage system - no changes needed there!
"""

from flask import Flask, render_template, request, redirect, url_for
from storage import add_request, get_all_requests, get_request_by_id, change_state

app = Flask(__name__)


@app.route('/')
def index():
    """Show all requests on the home page."""
    requests = get_all_requests()
    return render_template('index.html', requests=requests)


@app.route('/create', methods=['GET', 'POST'])
def create():
    """Create a new support request."""
    if request.method == 'POST':
        description = request.form.get('description', '').strip()
        if description:
            req = add_request(description)
            return redirect(url_for('view_request', request_id=req.id))
        else:
            return render_template('create.html', error="Description cannot be empty")
    return render_template('create.html')


@app.route('/request/<int:request_id>')
def view_request(request_id):
    """View a single request with its full log."""
    req = get_request_by_id(request_id)
    if not req:
        return "Request not found", 404
    return render_template('request.html', req=req)


@app.route('/request/<int:request_id>/update', methods=['POST'])
def update_state(request_id):
    """Update a request's state."""
    new_state = request.form.get('state', '').strip().lower()
    if new_state in ['submitted', 'in_progress', 'resolved']:
        change_state(request_id, new_state)
    return redirect(url_for('view_request', request_id=request_id))


if __name__ == '__main__':
    app.run(debug=True, port=5000)

