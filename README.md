# ITPath

A simple IT support workflow system for managing support requests from submission to resolution.

## Why I Built This

This project was built as a learning exercise to understand:
- **System design fundamentals** - How to structure a real application with clear separation of concerns
- **State management** - Tracking and transitioning data through different states
- **Data flow** - How information moves through a system from input to storage to display
- **Error handling** - Building robust systems that handle edge cases
- **Git workflow** - Proper version control practices with meaningful commits

The goal wasn't to build something production-ready, but to deeply understand how real systems are designed and implemented from the ground up.

## What It Does

ITPath manages IT support requests through a simple workflow:

1. **Users submit support requests** with a description of their issue
2. **Support staff move requests** through fixed states: `submitted` → `in_progress` → `resolved`
3. **Every change is logged** - Complete audit trail of when requests were created and when states changed

## Features

- ✅ Create and manage support requests
- ✅ State transitions with validation
- ✅ Complete activity logging for audit trails
- ✅ Both CLI and web interfaces
- ✅ Clean, modern web UI

## Tech Stack

- **Python 3** - Core language
- **Flask** - Web framework
- **HTML/CSS** - Frontend (no JavaScript - keeping it simple)

## Project Structure

```
itpath/
├── src/
│   ├── request.py      # SupportRequest data model
│   ├── storage.py      # In-memory storage and CRUD operations
│   ├── main.py         # CLI interface
│   ├── app.py          # Flask web application
│   ├── templates/      # HTML templates
│   └── static/         # CSS styles
├── requirements.txt    # Python dependencies
└── README.md
```

## Setup & Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ubayx23/itpath.git
   cd itpath
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Web Interface (Recommended)

Start the Flask development server:

```bash
python3 src/app.py
```

Then open your browser to: **http://localhost:5000**

### CLI Interface

For a command-line interface:

```bash
python3 src/main.py
```

## How It Works

### Core Components

- **`SupportRequest`** - Data model representing a single support ticket with ID, description, state, timestamp, and activity logs
- **`storage.py`** - Manages all requests in memory with functions for creating, retrieving, and updating requests
- **`app.py`** - Flask routes that connect the web interface to the storage layer
- **`main.py`** - CLI interface providing the same functionality via terminal

### State Flow

Requests start in `submitted` state and can be moved to:
- `in_progress` - Work has begun
- `resolved` - Issue is fixed

Each state change is automatically logged with a timestamp.

## Current Limitations

- **In-memory storage** - Requests are lost when the application stops (no persistence)
- **No authentication** - Anyone can access and modify requests
- **Single instance** - Not designed for multiple users simultaneously

These were intentional simplifications to focus on core concepts rather than production features.

## Future Enhancements

Potential improvements (if continuing development):
- File-based or database persistence
- User authentication and authorization
- Email notifications
- Search and filtering
- Multi-user support

## License

This is a personal learning project - feel free to use it as a reference or starting point for your own projects.
