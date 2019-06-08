import sys

"""
Counts amount of ways the string s is hidden in the string t
Runs in O(n*m) where n = length of t, m = length of s
"""
def search(s, t):
    m = len(s)-1
    n = len(t)
    complexity = 0

    r = 0
    _next = 0
    for i in range(n):
        complexity += 1
        if t[i] == s[_next]:
            if _next == m:
                r += 1
            else:
                _next += 1

    assert(complexity <= n*m)
    print("Complexity: {}, m*n={}".format(complexity, n*m))
  
    return r

if __name__== "__main__":
    s = sys.argv[1]
    t = sys.argv[2]
    print("Hidden strings found: {}".format(search(s, t)))
