from data.dataclasses import EmailDict

def num_recipients(email: EmailDict):
    return len(email.recipients)

def body_embedding(email: EmailDict):
    return [1, 2, 3]

def subject_embedding(email: EmailDict):
    return [1, 2, 3]

def spam_classifier(email: EmailDict):
    return False