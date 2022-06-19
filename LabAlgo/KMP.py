# KMP Algorithm
def KMP(pat, txt):
    m = len(pat)
    n = len(txt)
      # longest prefix suffix 
    lps = [0]*m
    j = 0 # index for pat[]
    # Preprocess the pattern
    computeLPSArray(pat, m, lps)
    i = 0 # index for txt[]
    while i < n:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == m:
            print (" index  " + str(i-j))
            j = lps[j-1]
          # mismatch after j matches
        elif i < n and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
def computeLPSArray(pat, m, lps):
    len = 0 # length of the previous longest prefix suffix
    lps[0] # lps[0] is always 0
    i = 1
    #calculates lps[i] for i = 1 to m-1
    while i < m:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1
  
txt = "algorisfunalgoisgreat"
word1 = "algo" 
word2 = "fun"
print("algorisfunalgoisgreat")
print("Found word 'algo' at:")
KMP(word1, txt)
print("Found word 'fun' at:")
KMP(word2, txt)

