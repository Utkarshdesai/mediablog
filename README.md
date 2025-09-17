# Django Blog Project

A modern Django-based microblogging application that allows users to create, edit, and delete posts with images. This project features user authentication, media handling, and a responsive UI built with Tailwind CSS.

## 🚀 Features

- **User Authentication**: Complete user registration and login system
- **Tweet Management**: Create, read, update, and delete posts
- **Image Upload**: Support for photo attachments in posts
- **Responsive Design**: Modern UI built with Tailwind CSS
- **User-Specific Actions**: Users can only edit/delete their own posts
- **Media Handling**: Proper static and media file management

## 🛠️ Technology Stack

- **Backend**: Django 5.2.6
- **Database**: SQLite3
- **Frontend**: HTML5, Tailwind CSS
- **Image Processing**: Pillow 11.3.0
- **Python Version**: 3.x

## 🔧 Installation & Setup

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Installation Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd Django_project/blog
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the development server**
   ```bash
   python manage.py runserver
   ```

5. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 📱 Usage

### For End Users
1. **Register**: Create a new account at `/accounts/register/`
2. **Login**: Sign in at `/accounts/login/`
3. **View Posts**: Browse all tweets on the home page
4. **Create Post**: Click "create tweet" to add a new post with optional image
5. **Edit/Delete**: Manage your own posts using the edit/delete buttons

### For Developers
- **Admin Interface**: Access Django admin at `/admin/` for database management
- **API Endpoints**: All functionality is available through web interface
- **Media Files**: Uploaded images are stored in the `media/static/` directory

## 🔐 Authentication

The project includes a complete authentication system:
- User registration with email validation
- Login/logout functionality
- Password-based authentication
- User-specific content access control

## 🎨 UI/UX Features

- **Responsive Design**: Works on desktop and mobile devices
- **Modern Interface**: Clean, card-based layout
- **Interactive Elements**: Hover effects and smooth transitions
- **User-Friendly Navigation**: Intuitive menu and action buttons
- **Image Display**: Properly sized and styled image previews

## 📝 Key URLs

- `/` - Welcome page
- `/tweet/` - Main tweets list
- `/tweet/newtweet/` - Create new tweet
- `/tweet/<id>/edit/` - Edit existing tweet
- `/tweet/<id>/delete/` - Delete tweet
- `/accounts/register/` - User registration
- `/accounts/login/` - User login
- `/accounts/logout/` - User logout
- `/admin/` - Django admin interface

## 🔧 Configuration

### Settings Highlights
- **Debug Mode**: Currently enabled for development
- **Database**: SQLite3 (easily configurable for production)
- **Media Handling**: Properly configured for file uploads
- **Static Files**: Configured for CSS and JavaScript
- **Authentication**: Login/logout redirects properly configured

## 📦 Dependencies

- **Django 5.2.6**: Web framework
- **Pillow 11.3.0**: Image processing
- **asgiref 3.9.1**: ASGI support
- **sqlparse 0.5.3**: SQL parsing
- **tzdata 2025.2**: Timezone data


