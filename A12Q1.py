def ChkVowel(A):
    vowel = ["a","e","i","o","u"]
    if A in vowel:
        return True
    else:
        return False


def main():
    chr = input("Write aplphabet to check: ").lower()
    Ret = ChkVowel(chr)
    if (Ret == True):
        print("Given Alphabet is vowel")
    else:
        print("Given Alphabet is Not vowel")


if __name__ == "__main__":
    main()
