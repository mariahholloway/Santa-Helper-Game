from random import Random
from final import *
random = Random()
def main():
    print ("test giftee result")
    assert giftee_result("mariah","mariah") == "You Get To Keep Your Giftee!"
    assert giftee_result("chad","chad") == "You Get To Keep Your Giftee!"
    assert giftee_result("amira","mariah") == "The eleves went a different direction :/ "
    global random
    random = Random(1)
    assert get_elf_choice() == "Amira"
if __name__ == "__main__":
    main()
