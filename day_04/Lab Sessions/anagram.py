from collections import Counter

def anagram(first: str, second: str) -> bool:
    """Returns True if the first and second word are anagrams.

    Note: Listen and Silent are anagrams
    """
    first_string = first.lower()
    second_string = second.lower()

    first_count = Counter(first_string)
    second_count = Counter(second_string)

    return first_count == second_count

def test_anagram():
    assert anagram("Cat" ,"Act")
    assert anagram("Dear" ,"Read")
    assert anagram("Rail" ,"Liar")
    assert not anagram("Compass" ,"Red")
    assert not anagram("aa" ,"a")
    assert not anagram("abb" ,"baa")
