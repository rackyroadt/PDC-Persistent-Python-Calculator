
import subprocess
import os
import sys

# Remove history if exists
if os.path.exists('history.json'):
    try:
        os.remove('history.json')
    except Exception as e:
        print(f"Could not remove history.json: {e}")

print("Running calculator test...")
# Run calculator
try:
    process = subprocess.Popen([sys.executable, 'calculator.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input="add\n10\n20\nquit\n")
    
    print("STDOUT:", stdout)
    print("STDERR:", stderr)
except Exception as e:
    print(f"Failed to run subprocess: {e}")

if os.path.exists('history.json'):
    print("SUCCESS: history.json created")
    with open('history.json', 'r') as f:
        print("CONTENT:", f.read())
else:
    print("FAILURE: history.json not found")
