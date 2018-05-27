class ChainLink:
    def __init__(self, chain, filter):
        self.filter = filter
        self.chain = chain
        self.chain.append(self)

    def next(self):
        location = self.chain.index(self)
        if not self.end():
            return self.chain[location+1]

    def end(self):
        return (self.chain.index(self) + 1 >=
                len(self.chain))

    def __call__(self, message):
        r = self.filter(message)
        if r.isSuccessful() or self.end():
            return r
        return self.next()(message)
