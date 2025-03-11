🚀 3/11/2025 Troubleshooting FastAPI
📌 Note – To ensure that the API works, make sure:
1️⃣ Each major directory contains an __init__.py file.
2️⃣ The app/ folder is correctly set as the primary module.
3️⃣ The virtual environment (venv/) is correctly activated.

🐍 Fixing Import Errors in FastAPI
🚨 Error:
If you see an error like:

ImportError: cannot import name 'X' from 'app.database.models'

Follow these steps:

✅ 1️⃣ Ensure __init__.py Exists in Every Folder
Run the following commands to create missing __init__.py files:

cmd
Copy
Edit
echo. > app/__init__.py
echo. > app/database/__init__.py
echo. > app/api/__init__.py
✅ 2️⃣ Fix Virtual Environment Issues
If imports are still red in PyCharm, your virtual environment might be broken.
Recreate it by running:

cmd
Copy
Edit
rmdir /s /q venv  # Delete old venv
python -m venv venv  # Create a new one
venv\Scripts\activate  # Activate it
pip install fastapi uvicorn sqlalchemy pydantic  # Reinstall dependencies
✅ 3️⃣ Set the Correct Python Interpreter in PyCharm
Go to File > Settings > Project: BackTrackIt > Python Interpreter
Select:
makefile
Copy
Edit
C:\Users\michale\BackTrackIt\backend\venv\Scripts\python.exe
Click Apply & OK, then restart PyCharm.
✅ 4️⃣ Delete Python Cache (__pycache__)
Old cache files can cause conflicts. Remove them by running:

c
Copy
Edit
rmdir /s /q app/__pycache__
rmdir /s /q app/database/__pycache__
rmdir /s /q app/api/__pycache__
✅ 5️⃣ Restart FastAPI
Once the fixes are applied, restart your FastAPI server:

cmd
Copy
Edit
uvicorn app.main:app --reload
✅ 6️⃣ Use Absolute Imports if Needed
If you still get import errors, use absolute paths in your main.py:

python
Copy
Edit
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
🎯 Final Checklist Before Running FastAPI
✅ __init__.py exists in all major directories
✅ Virtual environment (venv/) is activated
✅ Correct Python interpreter is set in PyCharm
✅ __pycache__ is cleared
✅ FastAPI is restarted
