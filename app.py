from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'santa-secret-key-change-in-production'  # Change this in production

# Module name mapping: short names to full module names
MODULE_MAPPING = {
    'elf': 'elf_crisis',
    'reindeer': 'reindeer_navigation',
    'ethics': 'gift_ethics',
    'emotion': 'emotion_stabilizer'
}

# Reverse mapping for getting short names
REVERSE_MODULE_MAPPING = {v: k for k, v in MODULE_MAPPING.items()}

def initialize_modules():
    """Initialize module completion status in session if not exists."""
    if 'modules_completed' not in session:
        session['modules_completed'] = {
            'elf': False,
            'reindeer': False,
            'ethics': False,
            'emotion': False
        }
        session.modified = True

def mark_complete(module_name):
    """
    Mark a module as complete.
    
    Args:
        module_name: Short name ('elf', 'reindeer', 'ethics', 'emotion') 
                     or full name ('elf_crisis', etc.)
    """
    initialize_modules()
    
    # Convert full module name to short name if needed
    if module_name in REVERSE_MODULE_MAPPING:
        module_name = REVERSE_MODULE_MAPPING[module_name]
    elif module_name in MODULE_MAPPING:
        # Already a short name, use as is
        pass
    else:
        # Invalid module name
        return False
    
    if module_name in session['modules_completed']:
        session['modules_completed'][module_name] = True
        session.modified = True
        return True
    return False

def get_progress():
    """
    Calculate and return overall progress percentage.
    
    Returns:
        int: Progress percentage (0-100)
    """
    initialize_modules()
    
    total_modules = len(session['modules_completed'])
    completed_modules = sum(1 for completed in session['modules_completed'].values() if completed)
    progress = int((completed_modules / total_modules) * 100)
    
    return progress

def all_modules_complete():
    """
    Check if all modules are completed.
    
    Returns:
        bool: True if all modules are complete, False otherwise
    """
    initialize_modules()
    return all(session['modules_completed'].values())

def is_module_accessible(module_name):
    """
    Check if a module is accessible (all modules are accessible by default).
    This function can be extended for sequential unlocking if needed.
    
    Args:
        module_name: Short name of the module ('elf', 'reindeer', 'ethics', 'emotion')
    
    Returns:
        bool: True if module is accessible, False otherwise
    """
    initialize_modules()
    # All modules are accessible from the start
    # Can be modified to implement sequential unlocking
    return module_name in session['modules_completed']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    initialize_modules()
    progress = get_progress()
    
    # Get completion status for template
    modules_completed = session['modules_completed']
    
    return render_template('map.html', progress=progress, modules_completed=modules_completed)

@app.route('/module/<module_name>')
def module(module_name):
    # Validate module name
    valid_modules = ['elf_crisis', 'reindeer_navigation', 'gift_ethics', 'emotion_stabilizer']
    if module_name not in valid_modules:
        return redirect(url_for('map'))
    
    initialize_modules()
    
    # Get short module name for completion tracking
    short_name = REVERSE_MODULE_MAPPING.get(module_name, module_name)
    
    # Guard: Check if module is accessible
    if not is_module_accessible(short_name):
        return redirect(url_for('map'))
    
    is_completed = session['modules_completed'].get(short_name, False)
    
    return render_template('module.html', module_name=module_name, is_completed=is_completed)

@app.route('/elf')
def elf_module():
    """Elf module - toy fixing game."""
    initialize_modules()
    
    # Guard: Check if module is accessible
    if not is_module_accessible('elf'):
        return redirect(url_for('map'))
    
    is_completed = session['modules_completed'].get('elf', False)
    progress = get_progress()
    return render_template('elf_module.html', is_completed=is_completed, progress=progress)

@app.route('/complete_elf', methods=['POST'])
def complete_elf():
    """Mark elf module as complete after successful game completion."""
    initialize_modules()
    
    # Guard: Ensure module is accessible before allowing completion
    if not is_module_accessible('elf'):
        return redirect(url_for('map'))
    
    if mark_complete('elf'):
        return redirect(url_for('map') + '?completed=elf')
    return redirect(url_for('elf_module'))

@app.route('/reindeer')
def reindeer_module():
    """Reindeer module - navigation/reaction game."""
    initialize_modules()
    
    # Guard: Check if module is accessible
    if not is_module_accessible('reindeer'):
        return redirect(url_for('map'))
    
    is_completed = session['modules_completed'].get('reindeer', False)
    progress = get_progress()
    return render_template('reindeer_module.html', is_completed=is_completed, progress=progress)

@app.route('/complete_reindeer', methods=['POST'])
def complete_reindeer():
    """Mark reindeer module as complete after successful game completion."""
    initialize_modules()
    
    # Guard: Ensure module is accessible before allowing completion
    if not is_module_accessible('reindeer'):
        return redirect(url_for('map'))
    
    if mark_complete('reindeer'):
        return redirect(url_for('map') + '?completed=reindeer')
    return redirect(url_for('reindeer_module'))

@app.route('/ethics')
def ethics_module():
    """Ethics module - gift distribution decision."""
    initialize_modules()
    
    # Guard: Check if module is accessible
    if not is_module_accessible('ethics'):
        return redirect(url_for('map'))
    
    is_completed = session['modules_completed'].get('ethics', False)
    progress = get_progress()
    return render_template('ethics_module.html', is_completed=is_completed, progress=progress)

@app.route('/complete_ethics', methods=['POST'])
def complete_ethics():
    """Mark ethics module as complete after decision."""
    initialize_modules()
    
    # Guard: Ensure module is accessible before allowing completion
    if not is_module_accessible('ethics'):
        return redirect(url_for('map'))
    
    choice = request.form.get('choice', '')
    if mark_complete('ethics'):
        return redirect(url_for('map') + '?completed=ethics')
    return redirect(url_for('ethics_module'))

@app.route('/emotion')
def emotion_module():
    """Emotion module - send emotions to regions."""
    initialize_modules()
    
    # Guard: Check if module is accessible
    if not is_module_accessible('emotion'):
        return redirect(url_for('map'))
    
    is_completed = session['modules_completed'].get('emotion', False)
    progress = get_progress()
    return render_template('emotion_module.html', is_completed=is_completed, progress=progress)

@app.route('/complete_emotion', methods=['POST'])
def complete_emotion():
    """Mark emotion module as complete after interaction."""
    initialize_modules()
    
    # Guard: Ensure module is accessible before allowing completion
    if not is_module_accessible('emotion'):
        return redirect(url_for('map'))
    
    if mark_complete('emotion'):
        return redirect(url_for('map') + '?completed=emotion')
    return redirect(url_for('emotion_module'))

@app.route('/complete_module/<module_name>', methods=['POST'])
def complete_module(module_name):
    """Mark a module as complete."""
    if mark_complete(module_name):
        return redirect(url_for('map'))
    return redirect(url_for('map'))

@app.route('/finale')
def finale():
    """Finale route - only accessible if all modules are complete."""
    initialize_modules()
    
    # Guard: Finale is locked until all modules are completed
    if not all_modules_complete():
        # Redirect to map if not all modules are complete
        return redirect(url_for('map'))
    
    progress = get_progress()
    return render_template('finale.html', progress=progress)

@app.route('/reset')
def reset():
    """Reset all progress."""
    session['modules_completed'] = {
        'elf': False,
        'reindeer': False,
        'ethics': False,
        'emotion': False
    }
    session.modified = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

