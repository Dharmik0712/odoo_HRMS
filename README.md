# 🚀 Dayflow HRMS - Human Resource Management System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![React](https://img.shields.io/badge/React-18+-61DAFB.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-316192.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**A Production-Grade Human Resource Management System built with FastAPI, React, and PostgreSQL**

[Features](#-features) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Architecture](#-architecture) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Running the Application](#-running-the-application)
- [API Documentation](#-api-documentation)
- [Database Schema](#-database-schema)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)
- [Support](#-support)

---

## 🌟 Overview

**Dayflow HRMS** is a comprehensive, production-ready Human Resource Management System designed to streamline HR operations for modern organizations. Built with cutting-edge technologies, it provides a robust platform for managing employees, tracking attendance, processing leave requests, and handling payroll.

### Why Dayflow HRMS?

- ✅ **Production-Ready**: Built with industry best practices
- ✅ **Secure**: JWT authentication, password hashing, RBAC
- ✅ **Scalable**: Async operations, connection pooling, caching
- ✅ **Well-Documented**: Comprehensive API docs with Swagger/ReDoc
- ✅ **Easy to Deploy**: Docker support with docker-compose
- ✅ **Maintainable**: Clean code, proper error handling, extensive logging

---

## ✨ Features

### 🔐 Authentication & Authorization
- **JWT-based authentication** with access and refresh tokens
- **Role-based access control** (Admin, HR, Employee)
- **Secure password hashing** using bcrypt
- **Email verification** system
- **Password reset** functionality

### 👥 Employee Management
- Complete **employee profiles** with personal and professional details
- **Department and designation** management
- **Emergency contact** information
- **Profile picture** upload
- **Employee hierarchy** (Manager-subordinate relationships)

### ⏰ Attendance Tracking
- **Real-time check-in/check-out** system
- **Daily and weekly attendance** views
- **Working hours calculation**
- **Attendance status** (Present, Absent, Half-day, Leave)
- **Attendance statistics** and reports
- **Monthly attendance** summary

### 🏖️ Leave Management
- **Multiple leave types** (Paid, Sick, Casual, Unpaid)
- **Leave application** with date range selection
- **Approval workflow** for HR/Admin
- **Leave balance tracking**
- **Leave history** and status updates
- **Email notifications** for leave actions

### 💰 Payroll Management
- **Comprehensive salary structure**
  - Basic salary, HRA, allowances
  - Tax deductions, PF, insurance
- **Salary slip generation**
- **Bank account details** management
- **Gross and net salary** calculation
- **Read-only access** for employees
- **Full control** for HR/Admin

### 📊 Reporting & Analytics
- **Attendance reports** with filters
- **Leave balance reports**
- **Payroll summaries**
- **Employee statistics**
- **Department-wise analytics**

### 🔔 Notifications
- Email alerts for leave approvals/rejections
- Payroll update notifications
- System alerts and reminders

---

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **Python 3.11+** - Latest Python features
- **SQLAlchemy** - SQL toolkit and ORM
- **Alembic** - Database migration tool
- **PostgreSQL** - Robust relational database
- **Redis** - In-memory data structure store for caching
- **Pydantic** - Data validation using Python type annotations
- **python-jose** - JWT token handling
- **passlib** - Password hashing library

### Frontend
- **React 18** - Modern UI library
- **Vite** - Next generation frontend tooling
- **Tailwind CSS** - Utility-first CSS framework
- **Axios** - Promise-based HTTP client
- **Lucide React** - Beautiful icon library

### DevOps & Tools
- **Docker & Docker Compose** - Containerization
- **Nginx** - Reverse proxy and load balancing
- **GitHub Actions** - CI/CD pipeline
- **Pytest** - Testing framework
- **Black** - Code formatter
- **Flake8** - Linting

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Client Layer (Frontend)                  │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   React UI   │  │  Tailwind    │  │     Axios    │     │
│  │  Components  │  │     CSS      │  │  HTTP Client │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│              API Gateway & Security Layer                    │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │   JWT    │  │   RBAC   │  │   CORS   │  │ Logging  │   │
│  │  Auth    │  │  Access  │  │ Security │  │  System  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│              Application Layer (FastAPI)                     │
│                                                              │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐          │
│  │  Auth   │ │Employee │ │Attendance│ │ Leave   │          │
│  │   API   │ │   API   │ │   API    │ │   API   │          │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘          │
│  ┌─────────┐                                                │
│  │ Payroll │                                                │
│  │   API   │                                                │
│  └─────────┘                                                │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│            Business Logic & Services Layer                   │
│                                                              │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐           │
│  │   User     │  │ Attendance │  │   Leave    │           │
│  │  Service   │  │  Service   │  │  Service   │           │
│  └────────────┘  └────────────┘  └────────────┘           │
│  ┌────────────┐  ┌────────────┐                            │
│  │  Payroll   │  │   Email    │                            │
│  │  Service   │  │  Service   │                            │
│  └────────────┘  └────────────┘                            │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│              Data Layer (ORM & Database)                     │
│                                                              │
│  ┌────────────────────────────────────────────────┐         │
│  │            SQLAlchemy ORM Models               │         │
│  │  User │ Employee │ Attendance │ Leave │ Payroll│         │
│  └────────────────────────────────────────────────┘         │
│                                                              │
│  ┌──────────────────┐         ┌──────────────────┐         │
│  │   PostgreSQL     │         │      Redis       │         │
│  │ Primary Database │         │   Cache Store    │         │
│  └──────────────────┘         └──────────────────┘         │
└─────────────────────────────────────────────────────────────┘
```

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10 or higher**
- **Node.js 18+ and npm/yarn**
- **PostgreSQL 13+**
- **Redis 6+** (optional but recommended)
- **Git**
- **Docker & Docker Compose** (for containerized deployment)

### System Requirements
- **RAM**: 4GB minimum, 8GB recommended
- **Disk Space**: 10GB free space
- **OS**: Linux, macOS, or Windows with WSL2

---

## 🚀 Installation

### Option 1: Docker Installation (Recommended)

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/dayflow-hrms.git
cd dayflow-hrms
```

2. **Copy environment file**
```bash
cp .env.example .env
```

3. **Update environment variables** in `.env`

4. **Start all services**
```bash
docker-compose up -d
```

5. **Run database migrations**
```bash
docker-compose exec api alembic upgrade head
```

6. **Create admin user**
```bash
docker-compose exec api python scripts/create_admin.py
```

7. **Access the application**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/api/docs

### Option 2: Manual Installation

#### Backend Setup

1. **Clone and navigate to project**
```bash
git clone https://github.com/yourusername/dayflow-hrms.git
cd dayflow-hrms
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Set up PostgreSQL**
```bash
# Create database and user
sudo -u postgres psql
CREATE DATABASE dayflow_hrms;
CREATE USER hrms_user WITH PASSWORD 'hrms_pass';
GRANT ALL PRIVILEGES ON DATABASE dayflow_hrms TO hrms_user;
\q
```

6. **Run migrations**
```bash
alembic upgrade head
```

7. **Create admin user**
```bash
python scripts/create_admin.py
```

8. **Start the backend server**
```bash
uvicorn app.main:app --reload
```

#### Frontend Setup

1. **Navigate to frontend directory**
```bash
cd frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Start development server**
```bash
npm run dev
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Application Settings
APP_NAME=Dayflow HRMS
APP_VERSION=1.0.0
DEBUG=True
API_PREFIX=/api/v1

# Database Configuration
DATABASE_URL=postgresql://hrms_user:hrms_pass@localhost:5432/dayflow_hrms

# Redis Configuration
REDIS_URL=redis://localhost:6379/0

# Security Settings
SECRET_KEY=your-super-secret-key-min-32-characters-long
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# CORS Settings
CORS_ORIGINS=["http://localhost:3000","http://localhost:5173"]

# Email Configuration (Optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
FROM_EMAIL=noreply@dayflow.com

# File Upload
MAX_UPLOAD_SIZE=5242880  # 5MB
```

### Database Configuration

Update `alembic.ini` with your database URL:

```ini
sqlalchemy.url = postgresql://hrms_user:hrms_pass@localhost:5432/dayflow_hrms
```

---

## 🎮 Running the Application

### Development Mode

**Backend:**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend
npm run dev
```

### Production Mode

**Using Docker Compose:**
```bash
docker-compose -f docker-compose.prod.yml up -d
```

**Using PM2 (Backend):**
```bash
pm2 start "uvicorn app.main:app --host 0.0.0.0 --port 8000" --name dayflow-api
```

**Frontend Build:**
```bash
cd frontend
npm run build
# Serve the dist folder with nginx or any static server
```

---

## 📚 API Documentation

### Interactive API Documentation

Once the backend is running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc

### API Endpoints Overview

#### Authentication
```
POST   /api/v1/auth/signup          - Register new user
POST   /api/v1/auth/login           - Login user
POST   /api/v1/auth/refresh         - Refresh access token
GET    /api/v1/auth/me              - Get current user info
POST   /api/v1/auth/change-password - Change password
```

#### Employees
```
GET    /api/v1/employees            - List all employees (Admin/HR)
POST   /api/v1/employees            - Create employee (Admin/HR)
GET    /api/v1/employees/me         - Get own profile
GET    /api/v1/employees/{id}       - Get employee by ID
PUT    /api/v1/employees/{id}       - Update employee
DELETE /api/v1/employees/{id}       - Delete employee (Admin)
```

#### Attendance
```
POST   /api/v1/attendance/check-in              - Check in
POST   /api/v1/attendance/check-out             - Check out
GET    /api/v1/attendance/my-attendance         - Get own attendance
GET    /api/v1/attendance/employee/{id}         - Get employee attendance (Admin)
POST   /api/v1/attendance                       - Create attendance record (Admin)
GET    /api/v1/attendance/stats/{employee_id}   - Get attendance statistics
```

#### Leaves
```
POST   /api/v1/leaves                    - Apply for leave
GET    /api/v1/leaves/my-leaves          - Get own leaves
GET    /api/v1/leaves/pending            - Get pending leaves (Admin/HR)
GET    /api/v1/leaves/{id}               - Get leave by ID
PUT    /api/v1/leaves/{id}/approve       - Approve/Reject leave (Admin/HR)
DELETE /api/v1/leaves/{id}               - Cancel leave
GET    /api/v1/leaves/balance/{emp_id}   - Get leave balance
```

#### Payroll
```
POST   /api/v1/payroll                          - Create payroll (Admin/HR)
GET    /api/v1/payroll/my-payroll               - Get own payroll
GET    /api/v1/payroll/employee/{id}            - Get employee payroll (Admin/HR)
GET    /api/v1/payroll                          - List all payrolls (Admin/HR)
PUT    /api/v1/payroll/{id}                     - Update payroll (Admin/HR)
DELETE /api/v1/payroll/{id}                     - Delete payroll (Admin)
GET    /api/v1/payroll/salary-slip/{emp_id}     - Generate salary slip
```

### Sample API Usage

**Login:**
```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin@dayflow.com&password=Admin@123"
```

**Get Current User:**
```bash
curl -X GET "http://localhost:8000/api/v1/auth/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Check In:**
```bash
curl -X POST "http://localhost:8000/api/v1/attendance/check-in" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## 🗄️ Database Schema

### Entity Relationship Diagram

```
┌─────────────────┐
│      User       │
├─────────────────┤
│ id (PK)         │
│ employee_id     │◄──────┐
│ email           │       │
│ password_hash   │       │
│ role            │       │
│ is_active       │       │
│ created_at      │       │
└─────────────────┘       │
         │                │
         │ 1              │
         │                │
         │ 1              │
         ▼                │
┌─────────────────┐       │
│    Employee     │       │
├─────────────────┤       │
│ id (PK)         │       │
│ user_id (FK)    │───────┘
│ first_name      │
│ last_name       │
│ department      │
│ designation     │
│ date_of_joining │
│ phone           │
└─────────────────┘
         │
         │ 1
         │
         │ N
         ├────────────────────────────────┐
         │                                │
         ▼                                ▼
┌─────────────────┐            ┌─────────────────┐
│   Attendance    │            │      Leave      │
├─────────────────┤            ├─────────────────┤
│ id (PK)         │            │ id (PK)         │
│ employee_id(FK) │            │ employee_id(FK) │
│ date            │            │ leave_type      │
│ check_in        │            │ start_date      │
│ check_out       │            │ end_date        │
│ status          │            │ status          │
│ working_hours   │            │ reason          │
└─────────────────┘            └─────────────────┘
         │
         │ 1
         │
         │ 1
         ▼
┌─────────────────┐
│     Payroll     │
├─────────────────┤
│ id (PK)         │
│ employee_id(FK) │
│ basic_salary    │
│ allowances      │
│ deductions      │
│ net_salary      │
└─────────────────┘
```

---

## 🧪 Testing

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test File
```bash
pytest tests/test_auth.py -v
```

### Run with Coverage
```bash
pytest tests/ --cov=app --cov-report=html
```

### Test Structure
```
tests/
├── __init__.py
├── conftest.py              # Test fixtures
├── test_auth.py             # Authentication tests
├── test_employees.py        # Employee API tests
├── test_attendance.py       # Attendance tests
├── test_leaves.py           # Leave management tests
└── test_payroll.py          # Payroll tests
```

---

## 🚢 Deployment

### Docker Deployment

1. **Build production image**
```bash
docker build -t dayflow-hrms:latest .
```

2. **Run with docker-compose**
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Cloud Deployment

#### AWS EC2
```bash
# Install Docker on EC2
sudo yum update -y
sudo yum install docker -y
sudo service docker start

# Clone and run
git clone https://github.com/yourusername/dayflow-hrms.git
cd dayflow-hrms
docker-compose up -d
```

#### Heroku
```bash
heroku create dayflow-hrms
heroku addons:create heroku-postgresql:hobby-dev
heroku addons:create heroku-redis:hobby-dev
git push heroku main
```

#### DigitalOcean
```bash
# Use App Platform or deploy to Droplet with Docker
doctl apps create --spec .do/app.yaml
```

### Nginx Configuration

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location / {
        root /var/www/frontend/dist;
        try_files $uri $uri/ /index.html;
    }
}
```

---

## 📁 Project Structure

```
dayflow_hrms/
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI application
│   ├── config.py                  # Configuration settings
│   ├── database.py                # Database connection
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py               # API dependencies
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── auth.py           # Authentication endpoints
│   │       ├── employees.py      # Employee endpoints
│   │       ├── attendance.py     # Attendance endpoints
│   │       ├── leaves.py         # Leave endpoints
│   │       └── payroll.py        # Payroll endpoints
│   ├── core/
│   │   ├── __init__.py
│   │   ├── security.py           # Security utilities
│   │   ├── logger.py             # Logging configuration
│   │   └── exceptions.py         # Custom exceptions
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py               # User model
│   │   ├── employee.py           # Employee model
│   │   ├── attendance.py         # Attendance model
│   │   ├── leave.py              # Leave model
│   │   └── payroll.py            # Payroll model
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py               # User schemas
│   │   ├── employee.py           # Employee schemas
│   │   ├── attendance.py         # Attendance schemas
│   │   ├── leave.py              # Leave schemas
│   │   └── payroll.py            # Payroll schemas
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py       # User business logic
│   │   ├── employee_service.py   # Employee business logic
│   │   ├── attendance_service.py # Attendance business logic
│   │   ├── leave_service.py      # Leave business logic
│   │   └── payroll_service.py    # Payroll business logic
│   └── utils/
│       ├── __init__.py
│       ├── email.py              # Email utilities
│       └── validators.py         # Validation helpers
├── alembic/
│   ├── env.py                    # Alembic environment
│   └── versions/                 # Migration files
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/           # React components
│   │   ├── pages/                # Page components
│   │   ├── services/             # API services
│   │   ├── utils/                # Utility functions
│   │   ├── App.jsx               # Main app component
│   │   └── main.jsx              # Entry point
│   ├── package.json
│   └── vite.config.js
├── tests/
│   ├── __init__.py
│   ├── conftest.py               # Test fixtures
│   ├── test_auth.py
│   ├── test_employees.py
│   ├── test_attendance.py
│   ├── test_leaves.py
│   └── test_payroll.py
├── scripts/
│   ├── create_admin.py           # Admin user creation
│   └── seed_data.py              # Sample data seeding
├── logs/                         # Application logs
├── .env                          # Environment variables
├── .env.example                  # Example environment file
├── .gitignore
├── requirements.txt              # Python dependencies
├── docker-compose.yml            # Docker compose config
├── Dockerfile                    # Docker image config
├── alembic.ini                   # Alembic configuration
├── pytest.ini                    # Pytest configuration
└── README.md                     # This file
```

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Code Style

- Follow PEP 8 for Python code
- Use Black for code formatting
- Write meaningful commit messages
- Add tests for new features
- Update documentation

### Development Guidelines

- Write clean, readable code
- Add docstrings to functions and classes
- Handle errors gracefully
- Log important operations
- Write unit tests
- Update API documentation

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Dayflow HRMS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 💬 Support

### Documentation
- **API Docs**: http://localhost:8000/api/docs
- **User Guide**: [docs/USER_GUIDE.md](docs/USER_GUIDE.md)
- **Admin Guide**: [docs/ADMIN_GUIDE.md](docs/ADMIN_GUIDE.md)

### Community
- **GitHub Issues**: [Create an issue](https://github.com/yourusername/dayflow-hrms/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/dayflow-hrms/discussions)
- **Email**: support@dayflow.com

### Reporting Bugs
When reporting bugs, please include:
- Description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- Environment details (OS, Python version, etc.)

### Feature Requests
We love feature requests! Please provide:
- Clear description of the feature
- Use case and benefits
- Any implementation ideas

---

## 🙏 Acknowledgments

- **FastAPI** - For the amazing web framework
- **SQLAlchemy** - For the powerful ORM
- **React** - For the excellent UI library
- **Tailwind CSS** - For beautiful styling
- All open-source contributors

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/dayflow-hrms)
![GitHub forks](https://img.shields.io/github/forks/yourusername/dayflow-hrms)
![GitHub issues](https://img.shields.io/github/issues/yourusername/dayflow-hrms)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/dayflow-hrms)

---

## 🗺️ Roadmap

### Version 1.1 (Q2 2024)
- [ ] Multi-language support
- [ ] Advanced reporting dashboard
- [ ] Mobile app (React Native)
- [ ] Performance reviews module

### Version 1.2 (Q3 2024)
- [ ] Training & development tracking
- [ ] Asset management
- [ ] Document management system
- [ ] Time tracking integration

### Version 2.0 (Q4 2024)
- [ ] AI-powered insights
- [ ] Recruitment module
- [ ] Onboarding automation
- [ ] Advanced analytics

---

<div align="center">

**Made with ❤️ by the Dayflow Team**

[⬆ Back to Top](#-dayflow-hrms---human-resource-management-system)

</div>
