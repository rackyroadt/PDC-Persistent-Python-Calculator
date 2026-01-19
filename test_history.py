
import subprocess
import os
import sys

# Clean up
if os.path.exists('history.json'):
    os.remove('history.json')

print("Starting history test...")

input_sequence = "add\n50\n50\nhistory\nquit\n"

try:
    process = subprocess.Popen(
        [sys.executable, 'calculator.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=input_sequence)
    
    print("STDOUT OUTPUT:\n", stdout)
    
    if "--- History ---" in stdout and "50.0 + 50.0 = 100.0" in stdout:
        print("\nTEST PASSED: History was displayed correctly.")
    else:
        print("\nTEST FAILED: History NOT displayed correctly.")
        
except Exception as e:
    print(f"Test Execution Failed: {e}")
