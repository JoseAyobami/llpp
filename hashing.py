from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated='auto')



class Hash():
    def encrypt(password: str):
        return pwd_cxt.hash(password)
    
    def verify(hashed_password, plain_word):
        return pwd_cxt.verify(plain_word, hashed_password)