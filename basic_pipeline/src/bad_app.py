from data.dataclasses import EmailDict
import features.bad_pipeline as bad_pipeline

# change this to a dictionary
sample_email = {
    "email_body": "Hello, how are you?",
    "email_subject": "Meeting", 
    "recipients": ["john@example.com", "jane@example.com"]
}

print(bad_pipeline.bad_featurize_email(sample_email))

