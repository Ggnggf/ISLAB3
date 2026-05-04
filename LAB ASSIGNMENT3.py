import hashlib, datetime

class Block:
    def __init__(self, i, data, prev_hash):
        self.i = i
        self.t = datetime.datetime.now()
        self.data = data
        self.prev = prev_hash
        self.hash = self.calc()

    def calc(self):
        s = f"{self.i}{self.t}{self.data}{self.prev}"
        return hashlib.sha256(s.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [Block(0, "Genesis", "0")]

    def add(self, data):
        prev = self.chain[-1]
        self.chain.append(Block(prev.i+1, data, prev.hash))

    def show(self):
        for b in self.chain:
            print(b.i, b.data, b.hash[:10], "...")

# Test
bc = Blockchain()
for i in range(1,5):
    bc.add(f"Block {i}")

bc.show()

# Tamper
print("\nTampered:\n")
bc.chain[2].data = "Hacked"
bc.chain[2].hash = bc.chain[2].calc()
bc.show()