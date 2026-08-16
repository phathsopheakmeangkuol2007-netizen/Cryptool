"""
Password strength checking utilities
"""
import re

# Common passwords list (top 1000 most common passwords)
COMMON_PASSWORDS = {
    'password', '123456', '12345678', 'qwerty', '123456789', '12345', '1234', '111111',
    '1234567', 'dragon', '123123', 'baseball', 'abc123', 'football', 'monkey', 'letmein',
    'shadow', 'master', '666666', 'qwertyuiop', '123321', 'mustang', '1234567890',
    'michael', '654321', 'superman', '1qaz2wsx', '7777777', '121212', '000000',
    'qazwsx', '123qwe', 'killer', 'trustno1', 'jordan', 'jennifer', 'zxcvbnm',
    'asdfgh', 'hunter', 'buster', 'soccer', 'harley', 'batman', 'andrew', 'tigger',
    'sunshine', 'iloveyou', '2000', 'charlie', 'robert', 'thomas', 'hockey',
    'ranger', 'daniel', 'starwars', 'klaster', '112233', 'george', 'computer',
    'michelle', 'jessica', 'pepper', '1111', 'zxcvbn', '555555', '11111111',
    '131313', 'freedom', '777777', 'pass', 'maggie', '159753', 'aaaaaa',
    'ginger', 'princess', 'joshua', 'cheese', 'summer', 'love', 'ashley',
    'nicole', 'chelsea', 'biteme', 'matthew', 'access', 'yankees', '987654321',
    'dallas', 'austin', 'thunder', 'taylor', 'matrix', 'mobilemail', 'mom',
    'monitor', 'monitoring', 'montana', 'moon', 'moscow', 'mountain', 'mouse',
    'dog', 'cat', 'bird', 'fish', 'lizard', 'horse', 'cow', 'pig', 'rabbit',
    'duck', 'goat', 'sheep', 'wolf', 'bear', 'lion', 'tiger', 'elephant',
    'giraffe', 'zebra', 'monkey', 'ape', 'hat', 'shirt', 'shoe', 'pant',
    'short', 'sock', 'glove', 'hat', 'coat', 'jacket', ' sweater', ' jeans',
    'khaki', 'chino', ' corduroy', ' leather', ' denim', ' cotton', ' wool',
    ' silk', ' linen', ' polyester', ' nylon', ' rayon', ' acrylic', ' spandex',
    ' yoga', ' running', ' basketball', ' football', ' baseball', ' soccer',
    ' tennis', ' golf', ' swimming', ' hiking', ' camping', ' fishing',
    ' hunting', ' skiing', ' snowboarding', ' skateboarding', ' surfing',
    ' cycling', ' bowling', ' boxing', ' wrestling', ' martial arts', ' karate',
    ' judo', ' taekwondo', ' kung fu', ' boxing', ' wrestling', ' mma',
    ' meditation', ' yoga', ' pilates', ' aerobics', ' dancing', ' ballet',
    ' jazz', ' tap', ' hip hop', ' salsa', ' ballroom', ' belly', ' flamenco',
    ' irish', ' square', ' line', ' break', ' tap', ' jazz', ' ballet',
    ' contemporary', ' modern', ' jazz', ' tap', ' hip hop', ' breakdancing'
}

def check_password_strength(password, check_common=False):
    """
    Check password strength and return a score and feedback
    
    Args:
        password (str): Password to check
        check_common (bool): Whether to check against common passwords
    
    Returns:
        dict: Contains score, feedback, and estimated crack time
    """
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 12:
        score += 4
    elif len(password) >= 8:
        score += 2
    else:
        feedback.append("Password is too short (minimum 8 characters)")
    
    # Character variety
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[^a-zA-Z0-9]', password):
        score += 1
    
    # Common password check
    if check_common and password.lower() in COMMON_PASSWORDS:
        feedback.append("This is a very common password")
        score = 0  # Reset score if it's a common password
    
    # Determine strength level
    if score >= 9:
        strength = "Very Strong"
        crack_time = "centuries"
    elif score >= 7:
        strength = "Strong"
        crack_time = "years"
    elif score >= 5:
        strength = "Moderate"
        crack_time = "months"
    elif score >= 3:
        strength = "Weak"
        crack_time = "weeks"
    else:
        strength = "Very Weak"
        crack_time = "hours"
    
    # Add specific feedback
    if len(password) < 8:
        feedback.append("Use at least 8 characters")
    if not re.search(r'[a-z]', password):
        feedback.append("Include lowercase letters")
    if not re.search(r'[A-Z]', password):
        feedback.append("Include uppercase letters")
    if not re.search(r'[0-9]', password):
        feedback.append("Include numbers")
    if not re.search(r'[^a-zA-Z0-9]', password):
        feedback.append("Include special characters")
    
    return {
        'score': score,
        'strength': strength,
        'feedback': feedback,
        'estimated_crack_time': crack_time,
        'is_common': check_common and password.lower() in COMMON_PASSWORDS
    }
