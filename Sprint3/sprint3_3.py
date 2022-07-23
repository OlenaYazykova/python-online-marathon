import re


def create_account(user_name: str, password: str, secret_words: list):
    regex=re.fullmatch(r'(?=.*[0-9])(?=.*[_!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z_!@#$%^&*]{6,}',password)
    if not regex:
        raise ValueError

    def check(password_check: str, secret_words_check: list):
        if len(secret_words_check)==len(secret_words):
            for i in secret_words:
                if i in secret_words_check:
                    secret_words_check.remove(i)
            return password_check==password and len(secret_words_check)<=1
        else:
            return False

    return check


tom = create_account("Tom", "Qwerty1_", ["1", "word"])  
check1 = tom("Qwerty1_",  ["1", "word"]) 
print(check1)
check2 = tom("Qwerty1_",  ["word"]) 
print(check2)
check3 = tom("Qwerty1_",  ["word", "2"]) 
print(check3)
check4 = tom("Qwerty1!",  ["word", "12"]) 
print(check4)
user2 = create_account("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
print(user2("yu6r*Tt5",["abc3", "abc3", "abc3"]))
