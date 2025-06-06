# Portfolio Project

A professional portfolio website built with Django to showcase your skills, projects, experience, and blog posts.

## Features

- Responsive design using Bootstrap
- Admin panel for content management
- Profile section with personal information
- Projects showcase with images and descriptions
- Skills section with proficiency levels
- Experience timeline
- Testimonials from clients or colleagues
- Blog with rich text editing (CKEditor)
- Contact form for visitors to reach out
- Global settings for site-wide configuration

## Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/portfolio.git
   cd portfolio
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Access the site at http://127.0.0.1:8000/

## Configuration

1. Log in to the admin panel at http://127.0.0.1:8000/admin/
2. Create a Profile with your personal information
3. Add your Projects, Skills, Experience, and Testimonials
4. Configure Global Settings (site title, meta description, etc.)

## Customization

- Edit templates in the `templates` directory
- Modify CSS in the `static/css` directory
- Add custom JavaScript in the `static/js` directory

## Deployment

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

## License

This project is licensed under the MIT License - see the LICENSE file for details.