# Rabin-Karp algorithm in python
 
d = 26  # number of characters in input set, if a-j, then its 10, pick any suitable value
 
 
def search(pattern, text, q):
    m = len(pattern)  # window size of searching pattern
    n = len(text)  # length of the text
    p = 0  # hash value for pattern
    t = 0  # hash value for first few letters in given text
    h = 1  # init value for h, will later be changed to update hash value of windows
    i = 0  # for iteration
    j = 0  # for iteration
 
    for i in range(m-1):
        # The value of h would be "pow(d, M-1)%q", would be used to recalculate hash value
        h = (h*d) % q
 
    # Calculate hash value for pattern and text
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q
 
    # Find the match
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break
 
            j += 1
            if j == m:
                print("Pattern is found at position: " + str(i))
 
        if i < n-m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q
 
            if t < 0:
                t = t+q
 
 
text = "algorisfunalgoisgreat"
print("Input text: algorisfunalgoisgreat")
pattern = "fun"
pattern2 = "algo"
q = 13  # to be modulo, hashing function
print("\nWhere is 'fun' located in the text?")
search(pattern, text, q)
print("\nWhere is 'algo' located in the text?")
search(pattern2, text, q)
print("\n")
