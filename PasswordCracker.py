alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

real_pass = "feeb"

for s1 in alphabet:
    for s2 in alphabet:
        for s3 in alphabet:
            for s4 in alphabet:
                possible_pass = s1 + s2 + s3 + s4
                if possible_pass == real_pass:
                    print(f"real password is {possible_pass}")


