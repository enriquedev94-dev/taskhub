from app.services.password import PasswordService

def test_hash_returns_different_value_than_original_password():
    password_service = PasswordService()
    password = "my_secure_password"
    hashed_password = password_service.hash(password)
    assert hashed_password != password  # Ensure the hashed password is different from the original

def test_verify_returns_true_for_correct_password():
    password_service = PasswordService()
    password = "my_secure_password"
    hashed_password = password_service.hash(password)
    assert password_service.verify(password, hashed_password)  is True# Ensure the correct password verifies successfully

def test_verify_returns_false_for_incorrect_password():
    password_service = PasswordService()
    password = "my_secure_password"
    hashed_password = password_service.hash(password)
    assert password_service.verify("wrong_password", hashed_password) is False  # Ensure an incorrect password does not verify