def suggest_priority(title, description):
    text = (title + " " + description).lower()
    
    high_words = ['urgent', 'asap', 'today', 'deadline', 'important', 'exam', 'project', 'submit']
    medium_words = ['tomorrow', 'soon', 'meeting', 'call', 'email', 'review']
    
    for word in high_words:
        if word in text:
            return 'High'
    
    for word in medium_words:
        if word in text:
            return 'Medium'
            
    return 'Low'