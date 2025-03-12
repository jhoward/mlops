from data.dataclasses import EmailDict
from features.calculators import (
    num_recipients,
    body_embedding,
    subject_embedding,
    spam_classifier
)

FEATURE_CALCULATOR_MAP = {
    "num_recipients": num_recipients,
    "email_body": body_embedding,
    "email_subject": subject_embedding,
    "is_spam": spam_classifier
}
def engine(email_dict: EmailDict):

    # Add validation checks

    # Add data quality checks

    # Compute features
    features = {
        feature_name: calculator(email_dict)
        for feature_name, calculator in FEATURE_CALCULATOR_MAP.items()
    }

    return features