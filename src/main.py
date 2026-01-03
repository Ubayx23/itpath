"""
Main CLI interface for ITPath.

This is the entry point - users interact with the system here.
"""

from storage import add_request, get_all_requests, change_state, get_request_by_id


def print_request(req):
    """Print a single request nicely."""
    print(f"\n[{req.id}] {req.state.upper()}")
    print(f"   {req.description}")
    print(f"   Created: {req.created_at.strftime('%Y-%m-%d %H:%M:%S')}")


def show_request_details():
    """Show detailed view of a request including its log."""
    show_all_requests()
    all_requests = get_all_requests()
    
    if not all_requests:
        return
    
    try:
        request_id = int(input("\nEnter request ID to view details: "))
        req = get_request_by_id(request_id)
        
        if not req:
            print(f"Request #{request_id} not found.")
            return
        
        print("\n" + "="*50)
        print_request(req)
        print("\n--- Activity Log ---")
        if req.logs:
            for timestamp, action, details in req.logs:
                print(f"  {timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {action}: {details}")
        else:
            print("  No activity logged yet.")
        print("="*50)
    except ValueError:
        print("Please enter a valid number.")


def show_all_requests():
    """Show all requests."""
    all_requests = get_all_requests()
    if not all_requests:
        print("\nNo requests yet.")
        return
    
    print(f"\n=== All Requests ({len(all_requests)}) ===")
    for req in all_requests:
        print_request(req)


def create_request():
    """Create a new support request."""
    print("\n=== Create New Request ===")
    description = input("What do you need help with? ")
    if description.strip():
        req = add_request(description)
        print(f"\n✓ Request #{req.id} created!")
        print_request(req)
    else:
        print("Description cannot be empty.")


def update_request_state():
    """Change a request's state."""
    show_all_requests()
    all_requests = get_all_requests()
    
    if not all_requests:
        return
    
    try:
        request_id = int(input("\nEnter request ID to update: "))
        req = get_request_by_id(request_id)
        
        if not req:
            print(f"Request #{request_id} not found.")
            return
        
        print(f"\nCurrent state: {req.state}")
        print("Available states: submitted, in_progress, resolved")
        new_state = input("New state: ").strip().lower()
        
        if new_state in ["submitted", "in_progress", "resolved"]:
            success, old_state = change_state(request_id, new_state)
            if success:
                print(f"\n✓ Request #{request_id} changed from '{old_state}' to '{new_state}'")
        else:
            print("Invalid state. Use: submitted, in_progress, or resolved")
    except ValueError:
        print("Please enter a valid number.")


def main():
    """Main menu loop."""
    print("=== ITPath - IT Support System ===\n")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Create new request")
        print("2. View all requests")
        print("3. View request details (with log)")
        print("4. Update request state")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == "1":
            create_request()
        elif choice == "2":
            show_all_requests()
        elif choice == "3":
            show_request_details()
        elif choice == "4":
            update_request_state()
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()

