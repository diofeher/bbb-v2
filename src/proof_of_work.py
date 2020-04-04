import hashlib

def break_proof_of_work(hashcash, zeroes):
    match = "0" * int(zeroes)
    count = 0
    while True:
        count += 1
        digest = hashlib.sha1(f'{hashcash}{count}'.encode('utf-8')).hexdigest()
        if digest.startswith(match):
            return count


if __name__ == "__main__":
    # Test script
    assert break_proof_of_work('FIKHSU3LH2JSJK7VJHTVHVZDQM;5', 5) == 379107
