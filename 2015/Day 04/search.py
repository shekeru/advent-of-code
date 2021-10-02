from hashlib import md5

I, R, S = 0, [5, 6], "ckczppom"

while R and (I := I + 1):
    H = md5(f"{S}{I}".encode()).hexdigest()
    if H.startswith('0' * R[0]):
        print(f"Found {R.pop(0)} at {I}")
