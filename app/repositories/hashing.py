from passlib.context import CryptContext



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password:str):
        hashedPassword=pwd_context.hash(password)
        return hashedPassword
    
    def verify(hashedPassword,plain_password):
        return pwd_context.verify(plain_password,hashedPassword)
