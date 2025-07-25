# 📘 School Management System (SaaS) – Django

A school management system built with Django, designed for English language schools in Ireland. SaaS-ready architecture focused on academic control, administrative organization, and student communication.

---

## ✅ PHASE 1 – MVP BASE (Essential + SaaS)

### 🔧 Initial Setup

* [x] Create Django project: `school_system`
* [x] Create apps: `accounts`, `organizations`, `students`, `teachers`, `classes`, `attendance`, `grades`
* [x] Configure PostgreSQL
* [x] Set up email sending (SMTP, SendGrid, etc.)
* [ ] Multi-tenant middleware to isolate data by organization

### 🔐 Users and Permissions

* [x] User roles: `admin`, `teacher`, `student`, `secretary`
* [x] Each user linked to an `Organization`
* [x] Login with role-based redirection
* [x] Logout with CSRF protection

### 📚 Entities and Relationships

* [x] CRUD for students
* [x] CRUD for teachers
* [x] CRUD for classes and rooms
* [ ] Assign students and teachers to classes (general enrollment screen in progress)

### 📜 Grades and Attendance

* [x] Attendance logging by class and date
* [ ] Grade input and viewing per student
* [ ] Student portal to view attendance and performance

### 📊 Dashboard

* [x] Teacher dashboard: view assigned classes
* [x] Admin dashboard: initial setup completed
* [ ] Student dashboard: view classes and performance
* [ ] Absences per student
* [ ] Average attendance per class/teacher

---

## 🟡 PHASE 2 – ADMINISTRATIVE FEATURES

### 📄 Documents and Certificates

* [ ] Upload and manage medical certificates
* [ ] Generate Leap Card request forms
* [ ] Generate GNIB request forms
* [ ] Certificate generation in PDF format
* [ ] Track learning levels per student

### 🗓 Exams and Payroll

* [ ] Exam scheduling
* [ ] Generate payroll reports (teacher working hours)

### 📧 Email Communication

* [ ] Automatic email notifications:

* [ ] Consecutive absences (>2 days)
* [ ] Enrollment confirmation
* [ ] General announcements
* [ ] Certificates and forms (PDF attachments)

---

## 🔹 PHASE 3 – ADVANCED FEATURES (SaaS)

### 💳 Financial

* [ ] Enrollment and tuition tracking
* [ ] Stripe or Revolut integration

### 🏢 Multi-Tenant Support

* [ ] Admin dashboard for managing multiple schools
* [ ] Data isolation by `Organization`

### ⚛️ Integrations and UX

* [ ] Google Calendar integration
* [ ] Change history logs (audit trail)
* [ ] Student document checklist
* [ ] Individual public page for each school

---

## 🚀 Suggested Technologies

| Feature        | Technology       |
| -------------- | ---------------- |
| Backend        | Django / DRF     |
| Database       | PostgreSQL       |
| Email delivery | SMTP / SendGrid  |
| Deployment     | Render / Railway |
| Payments       | Stripe / Revolut |

---

> 💡 Modular and scalable project, tailored for the educational market in Ireland.
