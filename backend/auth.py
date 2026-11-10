
from pwdlib import PasswordHash

# Create password hashing instance
password_hash = PasswordHash.recommended()


# Hash a user's password
def hash_password(password: str) -> str:
    return password_hash.hash(password)


# Verify a user's password
def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    return password_hash.verify(
        plain_password,
        hashed_password
    )
