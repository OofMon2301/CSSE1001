def is_dna(string):
    """Returns True if string is DNA, which must also be multiple of three, False otherwise."""  # noqa: E501
    for char in string:
        if char not in "ATCG" or len(string) % 3 != 0:
            return False
    return True


def reverse_complement(string):
    """Returns the reverse complement of string."""
    complement = ""
    for char in string:
        if char == "A":
            complement += "T"
        elif char == "T":
            complement += "A"
        elif char == "C":
            complement += "G"
        elif char == "G":
            complement += "C"
    # Check if sequence is valid or invalid
    for char in string:
        if char not in "ATCG" or len(string) % 3 != 0:
            return False
    return complement[::-1]


def print_codons(string):
    # Check if sequence is valid or invalid
    for char in string:
        if char not in "ATCG" or len(string) % 3 != 0:
            return False
    # Print codons
    for i in range(0, len(string), 3):
        print(string[i : i + 3])


def generate_codons(string):
    # Check if sequence is valid or invalid
    for char in string:
        if char not in "ATCG" or len(string) % 3 != 0:
            return False
    # Generate codons
    codons = []
    for i in range(0, len(string), 3):
        codons.append(string[i : i + 3])
    return codons
