class SuffixArray:
    N = 0  # length
    T = []  # text
    sa = []  # sorted suffix array values
    lcp = []  # longest common prefix array
    constructedSa = False
    constructedLcpArray = False

    def __init__(self, text):
        if text is None:
            return False
        self.T = text
        self.N = len(text)

    def getTextLength(self):
        return len(self.T)

    def getSa(self):
        self.buildSuffixArray()
        return self.lcp

    def getLcpArray(self):
        self.buildSuffixArray()
        return self.lcp

    def buildSuffixArray(self):
        if self.constructedSa:
            return
        self.construct()
        self.constructedSa = True

    def buildLcpArray(self):
        if self.constructedLcpArray:
            return
        self.buildSuffixArray()
        self.kasai()
        self.constructedLcpArray = True

    def toIntArray(self, s):
        if s is None:
            return None
        t = []
        for i in range(len(s), +1):
            t[i] = s[i]
        return t

    def kasai(self):
        self.lcp = []
        inv = []
        for i in range(self.N, +1):
            inv[self.sa[i]] = i
        i = 0
        len = 0
        for i in range(self.N, +1):
            if inv[i] > 0:
                k = self.sa[inv[i] - 1]
                while (i + len < self.N) and (k + len < self.N) and self.T[i + len] == self.T[k + len]:
                    len += 1
                self.lcp[inv[i]] = len
                if len > 0:
                    len -= 1
                    


