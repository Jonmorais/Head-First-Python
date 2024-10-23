def search4vowels(phrase: str) -> set:
    """ Return any vowels found in an asked-for phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))
