# main_app.py
# This is the main application file. It imports functionality from
# the other modules, demonstrating modularity.

# Import specific functions from the data_operations module
from data_operations import add_numbers, subtract_numbers

# Import the display_utils module entirely
import display_utils

# --- Main Program Execution ---

# 1. Use function from display_utils module
display_utils.print_welcome_message("Modular Calculator Demo")

# Define input variables
x = 25
y = 17

# 2. Use functions from data_operations module
# Perform Addition
sum_result = add_numbers(x, y)
# Format and display the result using display_utils
output_sum = display_utils.format_result("Addition", sum_result)
print(output_sum)

# Perform Subtraction
diff_result = subtract_numbers(x, y)
# Format and display the result using display_utils
output_diff = display_utils.format_result("Subtraction", diff_result)
print(output_diff)

print("\nModularity achieved: The main app successfully combined")
print("logic from 'data_operations' and presentation from 'display_utils'.")
