def num_recipients(email):
    return len(email["recipients"])

def body_embedding(email):
    return [1, 2, 3]

def subject_embedding(email):
    return [1, 2, 3]

def spam_classifier(email):
    return False