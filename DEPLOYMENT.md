# Deployment Guide

This guide will help you deploy your Django Portfolio project to various platforms.

## Table of Contents

1. [Preparation](#preparation)
2. [Heroku Deployment](#heroku-deployment)
3. [Render Deployment](#render-deployment)
4. [PythonAnywhere Deployment](#pythonanywhere-deployment)
5. [VPS Deployment (DigitalOcean, AWS, etc.)](#vps-deployment)
6. [Troubleshooting](#troubleshooting)

## Preparation

Before deploying, make sure you have:

1. Created a `.env` file based on the `.env.example` template with your actual values
2. Collected static files with `python manage.py collectstatic`
3. Tested your application locally with production settings:
   ```
   set DJANGO_SETTINGS_MODULE=portfolio_project.settings_prod
   python manage.py runserver
   ```

## Heroku Deployment

### Prerequisites

- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed
- Git repository initialized

### Steps

1. Login to Heroku:
   ```
   heroku login
   ```

2. Create a new Heroku app:
   ```
   heroku create your-portfolio-app-name
   ```

3. Add a PostgreSQL database:
   ```
   heroku addons:create heroku-postgresql:mini
   ```

4. Configure environment variables:
   ```
   heroku config:set SECRET_KEY=your_secret_key_here
   heroku config:set DJANGO_SETTINGS_MODULE=portfolio_project.settings_prod
   ```

5. Deploy your application:
   ```
   git add .
   git commit -m "Ready for deployment"
   git push heroku main
   ```

6. Run migrations:
   ```
   heroku run python manage.py migrate
   ```

7. Create a superuser:
   ```
   heroku run python manage.py createsuperuser
   ```

8. Open your application:
   ```
   heroku open
   ```

## Render Deployment

### Prerequisites

- A [Render](https://render.com/) account
- Git repository pushed to GitHub, GitLab, or Bitbucket

### Steps

1. Sign up or log in to [Render](https://render.com/)

2. From the Render dashboard, click "New" and select "Web Service"

3. Connect your GitHub/GitLab/Bitbucket repository

4. Configure your web service:
   - **Name**: Choose a name for your service
   - **Environment**: Select "Python 3"
   - **Region**: Choose the region closest to your users
   - **Branch**: Select your main/master branch
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn portfolio_project.wsgi:application`

5. Add environment variables:
   - Click on "Environment" tab
   - Add the following key-value pairs:
     ```
     SECRET_KEY=your_secret_key_here
     DJANGO_SETTINGS_MODULE=portfolio_project.settings_prod
     PYTHON_VERSION=3.12.0
     ```

6. Set up a PostgreSQL database:
   - From the Render dashboard, click "New" and select "PostgreSQL"
   - Configure your database (name, region, etc.)
   - After creation, copy the "Internal Database URL"
   - Go back to your web service, add a new environment variable:
     ```
     DATABASE_URL=your_internal_database_url
     ```

7. Deploy your service:
   - Click "Create Web Service"
   - Render will automatically build and deploy your application

8. Run migrations and create a superuser:
   - After deployment, go to the "Shell" tab in your web service
   - Run the following commands:
     ```
     python manage.py migrate
     python manage.py createsuperuser
     ```

9. Access your application at the provided Render URL

10. (Optional) Set up a custom domain:
    - Go to the "Settings" tab in your web service
    - Scroll to "Custom Domain" section
    - Follow the instructions to add your domain

## PythonAnywhere Deployment

### Steps

1. Sign up for a [PythonAnywhere](https://www.pythonanywhere.com/) account

2. Upload your code:
   - Use the Files tab to upload a zip of your project or
   - Clone your Git repository using the Bash console:
     ```
     git clone https://github.com/yourusername/portfolio.git
     ```

3. Set up a virtual environment:
   ```
   mkvirtualenv --python=/usr/bin/python3.10 portfolio-env
   cd portfolio
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your environment variables

5. Configure a new web app:
   - Go to the Web tab and click "Add a new web app"
   - Choose "Manual configuration" and select Python 3.10
   - Set the path to your virtual environment
   - Configure the WSGI file to point to your project's wsgi.py

6. Set up static files:
   - In the Web tab, add the static file mappings:
     - URL: /static/ Directory: /home/yourusername/portfolio/staticfiles
     - URL: /media/ Directory: /home/yourusername/portfolio/media

7. Run migrations and create a superuser using the Bash console

## VPS Deployment

### Prerequisites

- A VPS (DigitalOcean, AWS EC2, etc.)
- Domain name (optional)

### Steps

1. SSH into your server

2. Install required packages:
   ```
   sudo apt update
   sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx
   ```

3. Create a PostgreSQL database and user

4. Clone your repository:
   ```
   git clone https://github.com/yourusername/portfolio.git
   cd portfolio
   ```

5. Set up a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

6. Create a `.env` file with your environment variables

7. Collect static files:
   ```
   python manage.py collectstatic
   ```

8. Configure Gunicorn:
   Create a systemd service file for Gunicorn

9. Configure Nginx:
   Create an Nginx server block for your domain

10. Secure with SSL using Let's Encrypt

## Troubleshooting

### Static Files Not Loading

- Make sure you've run `python manage.py collectstatic`
- Check that your web server is configured to serve static files
- Verify the STATIC_ROOT and STATIC_URL settings

### Database Connection Issues

- Verify your DATABASE_URL environment variable
- Check that your database server is running
- Ensure your database user has the correct permissions

### 500 Server Errors

- Check your application logs
- Temporarily set DEBUG=True to see detailed error messages
- Verify all required environment variables are set

### Media File Uploads

- Ensure your MEDIA_ROOT directory is writable
- Check that your web server is configured to serve media files
- Verify the file upload permissions in your hosting environment