def generate_embedding(data):
    return [1, 2, 3]

def bad_featurize_email(email_dict):
    print("In featurize")

    features = {}
    features["num_recipients"] = len(email_dict["recipients"])
    features["body_embedding"] = generate_embedding(email_dict["email_body"])
    features["subject_embedding"] = generate_embedding(email_dict["email_subject"])
    features["is_spam"] = False

    return features

