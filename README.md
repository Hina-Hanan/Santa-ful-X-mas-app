# 🎅 Santa-ful X-mas - Interactive Christmas Adventure

An immersive, interactive web application that takes users on a magical Christmas journey. Help Santa complete his mission by solving challenges across 4 unique game modules, then receive a personalized letter from Santa himself!

## 📖 Project Description

Santa-ful X-mas is a Christmas-themed interactive web experience where users become Santa's helpers. The application features a sequential game progression system where players must complete 4 modules in order:

1. **Elf Crisis** - Fix broken toys before Christmas
2. **Reindeer Navigation** - Guide Santa's reindeer through obstacles
3. **Gift Ethics** - Make important decisions about gift distribution
4. **Emotion Stabilizer** - Spread joy and happiness across the world

Upon completing all modules, players unlock the special "Letter to Santa" feature, where they can write a personalized letter and receive an AI-generated, emotionally-aware response from Santa. The app includes beautiful animations, background music, text-to-speech functionality, and a stunning finale celebration.

## ✨ Features

### 🎮 Game Modules
- **Sequential Unlocking System**: Modules unlock progressively as you complete each challenge
- **Progress Tracking**: Visual progress bar showing completion percentage
- **Interactive Map**: Beautiful journey visualization with a candy cane path connecting all modules
- **Module Completion Rewards**: Celebrate achievements with visual feedback

### 📝 Letter to Santa
- **Personalized Letter Writing**: Submit your Christmas wishes, feelings, and memories
- **AI-Generated Santa Replies**: Receive emotionally-aware, personalized responses from Santa
- **Text-to-Speech**: Hear Santa read your letter aloud (stops automatically when navigating away)
- **Christmas Card Generation**: Get a beautiful, personalized Christmas card

### 🎨 User Experience
- **Beautiful UI/UX**: Modern, responsive design with Christmas-themed aesthetics
- **Background Music**: Immersive audio experience throughout the journey
- **Smooth Animations**: Engaging transitions and visual effects
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Session Management**: Progress is saved in browser sessions

### 🎯 Additional Features
- **Instructions Page**: Comprehensive guide on how to play
- **Finale Celebration**: Special completion page with confetti and animations
- **Reset Functionality**: Start your journey over anytime
- **Character Messages**: Encouraging messages from Santa, elves, and reindeer

## 🛠️ Tech Stack

### Backend
- **Flask 3.0.0** - Python web framework for routing and session management
- **Python 3.x** - Core programming language

### Frontend
- **HTML5** - Structure and semantic markup
- **CSS3** - Styling with modern features (gradients, animations, flexbox)
- **JavaScript (ES6+)** - Interactive functionality and DOM manipulation
- **Web Speech API** - Text-to-speech for letter reading

### Key Technologies
- **Jinja2 Templates** - Server-side templating engine (included with Flask)
- **Session Management** - Flask sessions for progress tracking
- **Responsive CSS** - Mobile-first design approach
- **CSS Animations** - Smooth transitions and visual effects

## 🚀 Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- A modern web browser (Chrome, Firefox, Edge, Safari)

### Installation Steps

1. **Clone or download the repository**
   ```bash
   cd project_directory
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # On Windows
   python -m venv xvenv
   xvenv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   - Navigate to `http://127.0.0.1:5000` or `http://localhost:5000`
   - The app should now be running!

### Configuration

- **Secret Key**: For production, change the `app.secret_key` in `app.py` to a secure random string
- **Debug Mode**: The app runs in debug mode by default. Disable for production

## 🌐 Deployment to Render

### Quick Reference: Environment Variables

**What to add in Render Dashboard → Environment tab:**

✅ **ADD THIS:**
- `SECRET_KEY` - Generate a secure random string (see instructions below)

❌ **DO NOT ADD:**
- `PORT` - Automatically set by Render (will cause errors if you add it manually)

### Prerequisites
- A [Render](https://render.com) account (free tier available)
- Your code pushed to a Git repository (GitHub, GitLab, or Bitbucket)

### Deployment Steps

1. **Prepare your application for production**
   
   The application is already configured to use environment variables:
   - `SECRET_KEY`: Used for Flask session security (Render can auto-generate this)
   - `PORT`: Automatically set by Render (defaults to 5000 for local development)

2. **Deploy via Render Dashboard**
   
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New +" and select "Web Service"
   - Connect your Git repository (GitHub, GitLab, or Bitbucket)
   - Configure the service:
     - **Name**: `santa-ful-xmas` (or your preferred name)
     - **Environment**: `Python 3`
     - **Region**: Choose the closest region to your users
     - **Branch**: `main` (or your default branch)
     - **Root Directory**: Leave empty (or specify if your app is in a subdirectory)
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Instance Type**: Free tier is sufficient for testing
   
3. **Set Environment Variables**
   
   In the Render dashboard, go to your service → **Environment** tab:
   
   **Required Environment Variables:**
   
   | Variable Name | Value | How to Set |
   |--------------|-------|------------|
   | `SECRET_KEY` | A secure random string | Click "Generate" button in Render, or use Python: `python -c "import secrets; print(secrets.token_hex(32))"` |
   | `PORT` | (Auto-set) | **DO NOT ADD** - Render automatically sets this to `10000` |
   
   **Steps to add SECRET_KEY:**
   1. In Render dashboard → Your Service → **Environment** tab
   2. Click **"Add Environment Variable"**
   3. **Key**: `SECRET_KEY`
   4. **Value**: 
      - **Option 1 (Recommended)**: Click the "Generate" button next to the value field (Render will create a secure random string)
      - **Option 2**: Generate your own using Python:
        ```bash
        python -c "import secrets; print(secrets.token_hex(32))"
        ```
        Copy the output and paste it as the value
      - **Option 3**: Use any long random string (minimum 32 characters recommended)
   
   **Example SECRET_KEY value:**
   ```
   a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6
   ```
   (This is just an example - always use a unique, randomly generated key!)
   
   **Note**: `PORT` environment variable is automatically set by Render - you do NOT need to add it manually.

4. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your application
   - Your app will be available at `https://your-app-name.onrender.com`
   - First deployment may take 5-10 minutes

### Alternative: Using render.yaml (Infrastructure as Code)

You can also deploy using a `render.yaml` file for automated deployments:

1. **Create `render.yaml` in your project root:**
   ```yaml
   services:
     - type: web
       name: santa-ful-xmas
       env: python
       buildCommand: pip install -r requirements.txt
       startCommand: gunicorn app:app
       envVars:
         - key: SECRET_KEY
           generateValue: true
         - key: PYTHON_VERSION
           value: 3.11.0
   ```

2. **Deploy via Render CLI or Dashboard:**
   - Push `render.yaml` to your repository
   - Render will automatically detect and use it

### Important Notes

- **Free Tier Limitations**: 
  - Render's free tier spins down after 15 minutes of inactivity
  - The first request after spin-down may take 30-60 seconds (cold start)
  - Consider upgrading to a paid plan for production use
  
- **Secret Key**: 
  - Always use environment variables for sensitive data
  - Never commit secret keys to your repository
  - Render can auto-generate secure keys

- **Static Files**: 
  - Ensure all static files (images, audio) are committed to your repository
  - Static files are served automatically by Flask

- **Debug Mode**: 
  - The app is configured with `debug=False` for production
  - Never enable debug mode in production (security risk)

- **HTTPS**: 
  - Render provides HTTPS automatically for all services
  - Custom domains are supported on paid plans

### Troubleshooting

- **Build Fails**: 
  - Check that all dependencies are in `requirements.txt`
  - Verify Python version compatibility
  - Check build logs in Render dashboard

- **App Crashes**: 
  - Check logs in Render dashboard → Logs section
  - Verify environment variables are set correctly
  - Ensure `gunicorn` is in requirements.txt

- **Static Files Not Loading**: 
  - Verify file paths are correct
  - Ensure all files are committed to Git
  - Check that static files are in the `static/` directory

- **Port Issues**: 
  - The app is configured to use the `PORT` environment variable
  - Render automatically sets this, no manual configuration needed

- **Session Issues**: 
  - Ensure `SECRET_KEY` is set in environment variables
  - Sessions are stored in memory (lost on restart)
  - For persistent sessions, consider using a database (not included in free tier)

### Project Structure
```
Santa_app/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── modules/                    # Application modules
│   ├── letter_logic.py        # Letter session management
│   └── santa_reply_generator.py # AI reply generation
├── templates/                  # HTML templates
│   ├── base.html              # Base template
│   ├── index.html             # Landing page
│   ├── instructions.html      # Game instructions
│   ├── map.html               # Journey map
│   ├── elf_module.html        # Elf Crisis game
│   ├── reindeer_module.html   # Reindeer Navigation game
│   ├── ethics_module.html     # Gift Ethics game
│   ├── emotion_module.html    # Emotion Stabilizer game
│   ├── finale.html            # Completion page
│   ├── letter_intro.html      # Letter introduction
│   ├── letter_form.html       # Letter writing form
│   ├── santa_reply.html       # Santa's reply page
│   └── christmas_card.html    # Christmas card
├── static/                     # Static assets
│   ├── assets/
│   │   ├── audio/             # Background music
│   │   └── images/             # Images and graphics
│   ├── style.css              # Global styles
│   └── script.js              # Global JavaScript
└── README.md                   # This file
```

## 📸 Screenshots

### Landing Page
![Landing Page](screenshots/landingpage.png)

### Instructions
![Instructions Page](screenshots/instructions.png)

### Journey Map / Levels
![Journey Map](screenshots/levels.png)

### Game Modules

#### Elf Crisis Module
![Elf Crisis Game](screenshots/elfgame.png)

#### Reindeer Navigation Module
![Reindeer Navigation Game](screenshots/reindeer.png)

#### Gift Ethics Module
![Gift Ethics Game](screenshots/ethics.png)

#### Emotion Stabilizer Module
![Emotion Stabilizer Game](screenshots/emotions.png)

### Letter to Santa
![Letter Writing Form](screenshots/letter_writing.png)

### Christmas Card
![Christmas Card](screenshots/x-mas_card.png)

## 🎯 How to Play

1. **Start Your Journey**: Click "Enter" on the landing page
2. **Read Instructions**: Familiarize yourself with the game mechanics
3. **Complete Modules**: Work through each module sequentially:
   - Complete Module 1 to unlock Module 2
   - Complete Module 2 to unlock Module 3
   - And so on...
4. **Track Progress**: Watch your progress bar fill as you complete modules
5. **Write to Santa**: After completing all 4 modules, unlock the letter feature
6. **Receive Your Reply**: Get a personalized response from Santa
7. **Celebrate**: Enjoy your Christmas card and finale celebration!

## 🔧 Development Notes

- The app uses Flask sessions to track progress (no database required)
- All game state is stored in browser sessions
- Text-to-speech uses the browser's Web Speech API
- Background music plays automatically on supported pages
- The app is designed to work offline after initial load (except for external fonts)

## 📝 License

This project is created for educational and entertainment purposes.

## 🤝 Contributing

Feel free to fork this project and make it your own! Suggestions and improvements are welcome.

## 🎄 Merry Christmas!

Enjoy your journey with Santa! 🎅🎁❄️

