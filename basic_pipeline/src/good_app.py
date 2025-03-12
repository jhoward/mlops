from data.dataclasses import EmailDict
import features.pipeline as pipeline

sample_email = EmailDict(
    email_body="Hello, how are you?",
    email_subject="Meeting", 
    recipients=["john@example.com", "jane@example.com"]
)

print(pipeline.engine(sample_email))

