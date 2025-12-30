"""
BrightSmile Dental Clinic - Flask Application
CS50-style full-stack dental clinic website
"""

import os
from flask import Flask, render_template, request, redirect, session, flash, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required
import sqlite3

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = os.urandom(24)

# Configure database path
DATABASE = os.path.join("database", "clinic.db")

# Ensure database directory exists
os.makedirs("database", exist_ok=True)


def get_db():
    """Get database connection"""
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


def init_db():
    """Initialize database with tables"""
    db = get_db()
    
    # Create users table
    db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'admin'
        )
    """)
    
    # Create services table
    db.execute("""
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)
    
    # Create appointments table
    db.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            service_id INTEGER,
            date TEXT NOT NULL,
            message TEXT,
            status TEXT DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (service_id) REFERENCES services(id)
        )
    """)
    
    # Create default admin user if not exists
    admin_exists = db.execute("SELECT id FROM users WHERE email = ?", ("admin@clinic.com",)).fetchone()
    if not admin_exists:
        password_hash = generate_password_hash("admin123")
        db.execute(
            "INSERT INTO users (name, email, password_hash, role) VALUES (?, ?, ?, ?)",
            ("Admin User", "admin@clinic.com", password_hash, "admin")
        )
    
    # Insert Alif Dental Clinic services if none exist
    services_count = db.execute("SELECT COUNT(*) as count FROM services").fetchone()["count"]
    if services_count == 0:
        alif_services = [
            ("Teeth brace/orthodontic", "We help straighten your teeth with braces and other orthodontic care. Our treatment makes your smile better, fixes bite problems, and keeps your mouth healthy. Each plan is made to fit your needs."),
            ("Teeth washing/bleaching", "We clean and whiten your teeth to make your smile brighter. Our safe treatment removes stains and helps your teeth look fresh and healthy."),
            ("Implants / prosthodontist", "We replace missing teeth safely with implants. Our modern implant service is designed to match your other teeth beautifully. We use high-quality materials such as zirconia, ceramic, Aermax, and flexible dentures to make your smile complete again. This treatment brings back your confidence and improves your quality of life."),
            ("Restorations", "We restore your teeth to their natural look without harming the surrounding teeth."),
            ("Child Dental Care", "We provide exceptional kids dental care ensuring that children receive gentle and expert treatment for a lifetime of healthy smiles."),
            ("Emergency Dental Care", "Alif Dental Clinic is here to provide fast and effective emergency dental care in Addis Ababa, helping you manage pain and prevent further damage."),
            ("Cosmetic Dentistry", "Our cosmetic dentistry services are designed to enhance your appearance and boost your confidence using the latest technology and expert care."),
            ("Oral & MaxilloFacial Surgery", "Our experienced surgeons perform a range of oral and maxillofacial procedures, ensuring you receive the best care possible.")
        ]
        for title, description in alif_services:
            db.execute(
                "INSERT INTO services (title, description) VALUES (?, ?)",
                (title, description)
            )
    
    db.commit()
    db.close()


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Home page"""
    db = get_db()
    services = db.execute(
        "SELECT * FROM services ORDER BY id LIMIT 4"
    ).fetchall()
    db.close()
    return render_template("index.html", services=services)


@app.route("/about")
def about():
    """About page"""
    return render_template("about.html")


@app.route("/services")
def services():
    """Services page"""
    db = get_db()
    services = db.execute("SELECT * FROM services ORDER BY id").fetchall()
    db.close()
    return render_template("services.html", services=services)


@app.route("/appointment", methods=["GET", "POST"])
def appointment():
    """Appointment booking page"""
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email") or None
        service_id = request.form.get("service_id")
        date = request.form.get("date")
        time = request.form.get("time") or None
        message = request.form.get("message") or None
        
        # Validate required fields
        if not name or not phone or not service_id or not date:
            flash("Please fill in all required fields.", "danger")
            return redirect("/appointment")
        
        # Insert appointment (store time in message if provided, or add to date)
        db = get_db()
        try:
            full_message = message or ""
            if time:
                full_message = f"Preferred Time: {time}\n\n{full_message}".strip()
            
            db.execute(
                """INSERT INTO appointments (name, phone, email, service_id, date, message, status)
                   VALUES (?, ?, ?, ?, ?, ?, 'Pending')""",
                (name, phone, email, service_id, date, full_message)
            )
            db.commit()
            db.close()
            return redirect("/success")
        except Exception as e:
            db.close()
            flash("An error occurred. Please try again.", "danger")
            return redirect("/appointment")
    
    # GET request - show form
    db = get_db()
    services = db.execute("SELECT * FROM services ORDER BY title").fetchall()
    db.close()
    return render_template("appointment.html", services=services)


@app.route("/success")
def success():
    """Success page after appointment booking"""
    return render_template("success.html")


@app.route("/contact")
def contact():
    """Contact page"""
    return render_template("contact.html")


@app.route("/testimonials")
def testimonials():
    """Testimonials page"""
    return render_template("testimonials.html")


@app.route("/faq")
def faq():
    """FAQ page"""
    return render_template("faq.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Admin login"""
    session.clear()
    
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        if not email or not password:
            flash("Please provide both email and password.", "danger")
            return render_template("login.html")
        
        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE email = ?", (email,)
        ).fetchone()
        db.close()
        
        if not user or not check_password_hash(user["password_hash"], password):
            flash("Invalid email or password.", "danger")
            return render_template("login.html")
        
        # Remember user session
        session["user_id"] = user["id"]
        session["user_name"] = user["name"]
        session["user_role"] = user["role"]
        
        flash("Logged in successfully!", "success")
        return redirect("/admin")
    
    return render_template("login.html")


@app.route("/logout")
def logout():
    """Logout user"""
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect("/")


@app.route("/admin")
@login_required
def admin():
    """Admin dashboard"""
    db = get_db()
    
    # Get all appointments
    appointments = db.execute("""
        SELECT a.*, s.title as service_title
        FROM appointments a
        LEFT JOIN services s ON a.service_id = s.id
        ORDER BY a.created_at DESC
    """).fetchall()
    
    # Get all services
    services = db.execute("SELECT * FROM services ORDER BY id").fetchall()
    
    db.close()
    return render_template("admin.html", appointments=appointments, services=services)


@app.route("/admin/update_status", methods=["POST"])
@login_required
def update_status():
    """Update appointment status"""
    appointment_id = request.form.get("appointment_id")
    status = request.form.get("status")
    
    if not appointment_id or not status:
        flash("Invalid request.", "danger")
        return redirect("/admin")
    
    db = get_db()
    db.execute(
        "UPDATE appointments SET status = ? WHERE id = ?",
        (status, appointment_id)
    )
    db.commit()
    db.close()
    
    flash("Appointment status updated successfully!", "success")
    return redirect("/admin")


@app.route("/admin/delete_appointment", methods=["POST"])
@login_required
def delete_appointment():
    """Delete appointment"""
    appointment_id = request.form.get("appointment_id")
    
    if not appointment_id:
        flash("Invalid request.", "danger")
        return redirect("/admin")
    
    db = get_db()
    db.execute("DELETE FROM appointments WHERE id = ?", (appointment_id,))
    db.commit()
    db.close()
    
    flash("Appointment deleted successfully!", "success")
    return redirect("/admin")


@app.route("/admin/add_service", methods=["POST"])
@login_required
def add_service():
    """Add new service"""
    title = request.form.get("title")
    description = request.form.get("description")
    
    if not title or not description:
        flash("Please provide both title and description.", "danger")
        return redirect("/admin")
    
    db = get_db()
    db.execute(
        "INSERT INTO services (title, description) VALUES (?, ?)",
        (title, description)
    )
    db.commit()
    db.close()
    
    flash("Service added successfully!", "success")
    return redirect("/admin")


@app.route("/admin/edit_service", methods=["POST"])
@login_required
def edit_service():
    """Edit service"""
    service_id = request.form.get("service_id")
    title = request.form.get("title")
    description = request.form.get("description")
    
    if not service_id or not title or not description:
        flash("Please provide all required fields.", "danger")
        return redirect("/admin")
    
    db = get_db()
    db.execute(
        "UPDATE services SET title = ?, description = ? WHERE id = ?",
        (title, description, service_id)
    )
    db.commit()
    db.close()
    
    flash("Service updated successfully!", "success")
    return redirect("/admin")


@app.route("/admin/delete_service", methods=["POST"])
@login_required
def delete_service():
    """Delete service"""
    service_id = request.form.get("service_id")
    
    if not service_id:
        flash("Invalid request.", "danger")
        return redirect("/admin")
    
    db = get_db()
    # Check if service is used in appointments
    appointments = db.execute(
        "SELECT COUNT(*) as count FROM appointments WHERE service_id = ?",
        (service_id,)
    ).fetchone()
    
    if appointments["count"] > 0:
        flash("Cannot delete service that has appointments. Please remove appointments first.", "danger")
        db.close()
        return redirect("/admin")
    
    db.execute("DELETE FROM services WHERE id = ?", (service_id,))
    db.commit()
    db.close()
    
    flash("Service deleted successfully!", "success")
    return redirect("/admin")


if __name__ == "__main__":
    # Initialize database on first run
    init_db()
    app.run(debug=True)

