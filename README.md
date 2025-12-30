# BrightSmile Dental Clinic Website

A modern, futuristic full-stack dental clinic website built with Flask, featuring a clean UI, admin dashboard, and appointment management system.

## 🚀 Features

- **Modern Futuristic Design**: Clean, modern UI with glassmorphism effects and smooth animations
- **Full-Stack Application**: Flask backend with SQLite database
- **Admin Dashboard**: Manage appointments and services
- **Appointment Booking**: Easy-to-use appointment request system
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Secure Authentication**: Session-based admin login with password hashing

## 📋 Prerequisites

Before running the application, make sure you have:

- Python 3.7 or higher installed
- pip (Python package manager)

## 🛠️ Installation & Setup

### Step 1: Navigate to Project Directory

Open your terminal/command prompt and navigate to the project directory:

```bash
cd "C:\Users\hisal\Documents\Dental clinic cs50 website"
```

### Step 2: Create Virtual Environment (Recommended)

Create a virtual environment to isolate project dependencies:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

This will install:
- Flask 3.0.0
- Werkzeug 3.0.1

### Step 4: Run the Application

Start the Flask development server:

```bash
python app.py
```

You should see output similar to:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 5: Access the Website

Open your web browser and navigate to:

- **Frontend**: http://localhost:5000 or http://127.0.0.1:5000
- **Admin Login**: http://localhost:5000/login

## 🔐 Default Admin Credentials

- **Email**: `admin@clinic.com`
- **Password**: `admin123`

⚠️ **Important**: Change these credentials in production!

## 📁 Project Structure

```
Dental clinic cs50 website/
├── app.py                 # Main Flask application
├── helpers.py             # Authentication helpers
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .gitignore            # Git ignore rules
├── database/             # SQLite database (auto-created)
│   └── clinic.db
├── templates/            # Jinja2 HTML templates
│   ├── layout.html       # Base template
│   ├── index.html        # Home page
│   ├── about.html        # About page
│   ├── services.html     # Services page
│   ├── appointment.html  # Appointment booking
│   ├── contact.html      # Contact page
│   ├── login.html        # Admin login
│   ├── admin.html        # Admin dashboard
│   └── success.html      # Success confirmation
└── static/
    ├── css/
    │   └── style.css     # Modern futuristic styling
    └── js/
        └── main.js        # JavaScript utilities
```

## 🎨 Design Features

- **Glassmorphism Effects**: Modern frosted glass navbar
- **Gradient Backgrounds**: Beautiful color gradients throughout
- **Smooth Animations**: Subtle hover effects and transitions
- **Modern Typography**: Inter font family for clean readability
- **Responsive Layout**: Mobile-first design approach
- **Professional Color Scheme**: Green primary color (#00d4aa) with modern accents

## 📱 Available Routes

| Route | Description |
|-------|-------------|
| `/` | Home page with hero section and services preview |
| `/about` | About page with clinic history and team |
| `/services` | Services page listing all dental services |
| `/appointment` | Appointment booking form |
| `/contact` | Contact information and map placeholder |
| `/login` | Admin login page |
| `/admin` | Admin dashboard (protected) |
| `/success` | Appointment confirmation page |
| `/logout` | Logout admin user |

## 🗄️ Database

The application uses SQLite database that is automatically created on first run. It includes:

- **users**: Admin user accounts
- **services**: Dental services offered
- **appointments**: Appointment requests from patients

The database file is located at: `database/clinic.db`

## 🔧 Admin Features

Once logged in as admin, you can:

- ✅ View all appointment requests
- ✅ Update appointment status (Pending/Confirmed/Completed/Cancelled)
- ✅ Delete appointments
- ✅ Add new services
- ✅ Edit existing services
- ✅ Delete services

## 🐛 Troubleshooting

### Port Already in Use

If you get an error that port 5000 is already in use:

1. Find and close the process using port 5000, or
2. Change the port in `app.py`:
   ```python
   app.run(debug=True, port=5001)
   ```

### Database Errors

If you encounter database errors:

1. Delete the `database/clinic.db` file
2. Restart the application (it will recreate the database)

### Module Not Found Errors

If you get import errors:

```bash
pip install --upgrade -r requirements.txt
```

## 🚀 Deployment

For production deployment:

1. Set a secure `SECRET_KEY` in `app.py`
2. Change default admin credentials
3. Use a production WSGI server (e.g., Gunicorn)
4. Configure proper database backups
5. Set up HTTPS/SSL certificates

## 📝 License

This project is created for educational purposes.

## 👨‍💻 Development

Built with:
- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite
- **Styling**: Custom modern CSS with glassmorphism effects

---

**Enjoy your modern dental clinic website! 🦷✨**

