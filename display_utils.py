# display_utils.py
# This module is responsible for formatting and presentation.
# It is independent of the calculation logic.

def format_result(operation_name, result):
    """Formats the result into a clean, human-readable string."""
    header = "=" * 30
    footer = "-" * 30
    
    return (
        f"\n{header}\n"
        f"Operation: {operation_name.upper()}\n"
        f"Result: {result}\n"
        f"{footer}\n"
    )

def print_welcome_message(app_name):
    """Prints a friendly welcome message for the application."""
    print(f"\n*** Welcome to the {app_name} ***")
    print("This app uses modular code (data_operations and display_utils).")
