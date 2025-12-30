"""
Letter to Santa logic module.
Handles storing and retrieving user letter responses in session.
"""

def initialize_letter_session(session):
    """Initialize letter data in session if not exists."""
    if 'letter_data' not in session:
        session['letter_data'] = {
            'name': None,
            'age': None,
            'gender': None,
            'country': None,
            'feeling': None,
            'wish': None,
            'memory': None,
            'submitted': False
        }
        session.modified = True

def save_letter_data(session, form_data):
    """
    Save letter form data to session.
    
    Args:
        session: Flask session object
        form_data: Dictionary containing form fields
    """
    initialize_letter_session(session)
    
    session['letter_data']['name'] = form_data.get('name', '').strip()
    session['letter_data']['age'] = form_data.get('age', '').strip() or None
    session['letter_data']['gender'] = form_data.get('gender', '').strip() or None
    session['letter_data']['country'] = form_data.get('country', '').strip() or None
    session['letter_data']['feeling'] = form_data.get('feeling', '').strip()
    session['letter_data']['wish'] = form_data.get('wish', '').strip()
    session['letter_data']['memory'] = form_data.get('memory', '').strip()
    session['letter_data']['submitted'] = True
    session.modified = True
    
    return True

def get_letter_data(session):
    """
    Get letter data from session.
    
    Args:
        session: Flask session object
    
    Returns:
        dict: Letter data or None if not initialized
    """
    initialize_letter_session(session)
    return session.get('letter_data')

def has_submitted_letter(session):
    """Check if user has already submitted a letter."""
    initialize_letter_session(session)
    return session.get('letter_data', {}).get('submitted', False)





