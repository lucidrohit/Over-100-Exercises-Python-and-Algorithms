#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


def reversing_words_setence(str1):
    ''' reverse the words in a sentence'''
    words = str1.split()
    rev_set = " ".join(reversed(words))
    return rev_set


def test_reversing_words_setence(module_name='this module'):
    str1 = "Buffy is a Vampire Slayer"
    assert(reversing_words_setence(str1) == "Slayer Vampire a is Buffy")
        
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))


if __name__ == '__main__':
    test_reversing_words_setence()

