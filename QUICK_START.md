# 🚀 Quick Start Guide

## ✅ Application Status

**Your Flask application is now RUNNING!**

Open your browser and visit:
- **Website**: http://localhost:5000
- **Admin Panel**: http://localhost:5000/login

## 🔐 Admin Login Credentials

- **Email**: `admin@clinic.com`
- **Password**: `admin123`

---

## 📝 How to Run (3 Easy Methods)

### Method 1: Double-Click Batch File (Easiest!)
Simply double-click `run.bat` in Windows Explorer

### Method 2: Use PowerShell Script
```powershell
powershell -ExecutionPolicy Bypass -File run.ps1
```

### Method 3: Manual Command
```powershell
.\venv\Scripts\python.exe app.py
```

---

## 🛑 How to Stop the Server

Press `Ctrl + C` in the terminal window

---

## ⚠️ Troubleshooting

### If port 5000 is already in use:
1. Find the process using port 5000
2. Close it, or
3. Edit `app.py` line 377 to use a different port:
   ```python
   app.run(debug=True, port=5001)
   ```

### If you see "Module not found":
Run this command:
```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

---

## 🎉 You're All Set!

The application is running and ready to use!

