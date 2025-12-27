"""
Santa Reply Generator module.
Generates personalized, emotional letters from Santa based on user responses.
"""

import random

# Emotional response templates based on feelings
FEELING_RESPONSES = {
    'happy': [
        "I can feel the joy radiating from your words, and it warms my heart like a cozy fire on a winter's night.",
        "Your happiness is like a bright star in the night sky, and I'm so glad to see you shining.",
        "The joy in your letter has made my workshop even merrier today!"
    ],
    'sad': [
        "I can sense the weight in your heart, and I want you to know that even in the darkest nights, stars still shine.",
        "Your feelings matter deeply to me, and I want you to remember that every storm eventually passes.",
        "I understand that sometimes the world feels heavy, but you are stronger than you know."
    ],
    'excited': [
        "Your excitement is contagious! I can almost hear the anticipation in your words.",
        "The energy in your letter has me checking my list twice with extra enthusiasm!",
        "Your excitement reminds me why I love this magical time of year so much."
    ],
    'anxious': [
        "I can sense the worry in your words, and I want you to know that it's okay to feel uncertain sometimes.",
        "Your concerns are valid, and I hope you find peace in knowing that you're not alone.",
        "Even when things feel uncertain, remember that you have the strength to face whatever comes."
    ],
    'grateful': [
        "Your gratitude shines through your words like a beacon of light, and it touches my heart deeply.",
        "The appreciation in your letter reminds me of the true spirit of Christmas.",
        "Your thankfulness is a gift in itself, and I'm honored to receive it."
    ],
    'hopeful': [
        "Your hope is like a candle in the darkness, and I believe it will guide you to wonderful things.",
        "I can feel the optimism in your words, and it gives me great joy to see your spirit.",
        "Your hopeful heart is one of the most beautiful things I've read this season."
    ],
    'lonely': [
        "I can feel the loneliness in your words, and I want you to know that you are never truly alone.",
        "Even when it feels like no one understands, remember that I'm here, and I care about you.",
        "Your letter reached me, and I want you to know that you matter, deeply and truly."
    ],
    'peaceful': [
        "The peace in your words is like a gentle snowfall, quiet and beautiful.",
        "Your calm spirit brings a sense of tranquility that I cherish.",
        "I can sense the serenity in your heart, and it's a beautiful thing to witness."
    ]
}

# Generic emotional responses for feelings not in the dictionary
GENERIC_EMOTIONAL_RESPONSES = [
    "I can feel the emotions in your words, and they touch my heart in ways words cannot fully express.",
    "Your feelings come through clearly in your letter, and I want you to know they matter to me.",
    "The emotions you've shared with me are precious, and I hold them close to my heart."
]

# Wish-related responses
WISH_RESPONSES = [
    "I've read your wish carefully, and while I can't promise everything, I can promise that I'll do my best.",
    "Your wish has been noted in my special book, and I'll carry it with me on my journey.",
    "I understand what you're hoping for, and I want you to know that sometimes the best gifts aren't the ones we can hold."
]

# Memory-related responses
MEMORY_RESPONSES = [
    "The memory you shared is beautiful, and I'm so glad you have it to hold close.",
    "That memory sounds precious, and I hope it continues to bring you warmth.",
    "Thank you for sharing that special moment with me. Memories like that are the true treasures of life."
]

# Closing messages
CLOSING_MESSAGES = [
    "May this Christmas bring you peace, joy, and the warmth of love surrounding you.",
    "I'll be thinking of you on Christmas Eve, and I hope you feel the magic in the air.",
    "Remember, the greatest gifts aren't always wrapped in boxes—they're the moments of connection, the acts of kindness, and the love we share.",
    "May your heart be light, your spirit bright, and your Christmas filled with wonder.",
    "I believe in you, and I believe in the magic of this season. May it bring you everything you need."
]

def detect_emotion_from_text(text):
    """
    Detect primary emotion from user's feeling text.
    Uses simple keyword matching to identify emotions.
    
    Args:
        text: User's feeling description
    
    Returns:
        str: Detected emotion key or 'generic'
    """
    if not text:
        return 'generic'
    
    text_lower = text.lower()
    
    # Check for specific emotions
    emotion_keywords = {
        'happy': ['happy', 'joy', 'joyful', 'glad', 'cheerful', 'merry', 'delighted', 'ecstatic'],
        'sad': ['sad', 'down', 'depressed', 'unhappy', 'melancholy', 'blue', 'upset'],
        'excited': ['excited', 'thrilled', 'eager', 'enthusiastic', 'pumped', 'energetic'],
        'anxious': ['anxious', 'worried', 'nervous', 'stressed', 'concerned', 'uneasy'],
        'grateful': ['grateful', 'thankful', 'appreciative', 'blessed'],
        'hopeful': ['hopeful', 'optimistic', 'hoping', 'wishful', 'positive'],
        'lonely': ['lonely', 'alone', 'isolated', 'lonesome'],
        'peaceful': ['peaceful', 'calm', 'serene', 'tranquil', 'relaxed', 'content']
    }
    
    for emotion, keywords in emotion_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            return emotion
    
    return 'generic'

def generate_santa_reply(letter_data):
    """
    Generate a personalized, emotional letter from Santa.
    
    Args:
        letter_data: Dictionary containing user's letter information
    
    Returns:
        str: Complete personalized letter from Santa
    """
    name = letter_data.get('name', 'Dear Friend')
    feeling = letter_data.get('feeling', '')
    wish = letter_data.get('wish', '')
    memory = letter_data.get('memory', '')
    age = letter_data.get('age')
    country = letter_data.get('country')
    
    # Start building the letter
    letter_parts = []
    
    # Greeting with name
    if name:
        letter_parts.append(f"Dear {name},")
    else:
        letter_parts.append("Dear Friend,")
    
    letter_parts.append("")  # Empty line
    
    # Opening paragraph - acknowledge receiving the letter
    opening_options = [
        "I received your letter, and I want you to know how much it means to me that you took the time to share your thoughts with me.",
        "Your letter arrived at the North Pole, and I've read it with great care and attention.",
        "I'm writing to you from my workshop, where your letter sits on my desk, and I've been thinking about what you shared."
    ]
    letter_parts.append(random.choice(opening_options))
    letter_parts.append("")
    
    # Address location if provided
    if country:
        location_options = [
            f"I can see you're writing from {country}, and I'm so glad your letter found its way to me.",
            f"From {country} to the North Pole—your words have traveled far, and I'm honored to receive them.",
            f"Even though we're far apart (you in {country} and me at the North Pole), your words have brought us closer."
        ]
        letter_parts.append(random.choice(location_options))
        letter_parts.append("")
    
    # Address age if provided (make it warm and appropriate)
    if age:
        try:
            age_int = int(age)
            if age_int < 13:
                letter_parts.append("I can see you're still young, and I want you to know that your feelings and thoughts are just as important as anyone else's.")
            elif age_int < 18:
                letter_parts.append("I know that being your age can bring many challenges and joys, and I appreciate you sharing your heart with me.")
            else:
                letter_parts.append("Even though you're older now, I believe that the magic of Christmas lives in all of us, regardless of age.")
            letter_parts.append("")
        except ValueError:
            pass  # If age isn't a number, skip this part
    
    # Address feeling/emotion
    if feeling:
        detected_emotion = detect_emotion_from_text(feeling)
        
        if detected_emotion in FEELING_RESPONSES:
            letter_parts.append(random.choice(FEELING_RESPONSES[detected_emotion]))
        else:
            letter_parts.append(random.choice(GENERIC_EMOTIONAL_RESPONSES))
        
        # Add personalized touch about their specific feeling
        letter_parts.append(f"When you wrote '{feeling[:50]}{'...' if len(feeling) > 50 else ''}', I could sense the depth of what you're experiencing.")
        letter_parts.append("")
    
    # Address wish
    if wish:
        letter_parts.append(random.choice(WISH_RESPONSES))
        if len(wish) > 0:
            # Reference their wish without repeating it verbatim
            wish_preview = wish[:100] + ('...' if len(wish) > 100 else '')
            letter_parts.append(f"I understand that you're hoping for something meaningful, and I want you to know that your wishes are heard.")
        letter_parts.append("")
    
    # Address memory
    if memory:
        letter_parts.append(random.choice(MEMORY_RESPONSES))
        if len(memory) > 0:
            memory_preview = memory[:100] + ('...' if len(memory) > 100 else '')
            letter_parts.append("Memories like the one you shared are the threads that weave the tapestry of our lives, and I'm grateful you chose to share yours with me.")
        letter_parts.append("")
    
    # Personal message connecting everything
    connection_messages = [
        "As I prepare for my journey around the world, I carry your words with me, and I want you to know that you matter.",
        "In a world that sometimes feels too busy, your letter reminded me of what truly matters—connection, understanding, and the human heart.",
        "Your letter has touched me in ways I can't fully express, and I hope my words can bring you some comfort and joy."
    ]
    letter_parts.append(random.choice(connection_messages))
    letter_parts.append("")
    
    # Closing message
    letter_parts.append(random.choice(CLOSING_MESSAGES))
    letter_parts.append("")
    
    # Signature
    letter_parts.append("With warmth and love,")
    letter_parts.append("Santa Claus")
    letter_parts.append("")
    letter_parts.append("P.S. Remember, you are never alone, and you are deeply valued.")
    
    return "\n".join(letter_parts)


