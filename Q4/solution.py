class Cache:
    def __init__(self): self.store = {}
    def get(self, name, now):
        if name in self.store:
            address, expiry = self.store[name]
            if now < expiry: return address
            del self.store[name]
        return None
    def put(self, name, address, now, ttl):
        self.store[name] = (address, now + ttl)
NAME, ADDRESS = 'shop.example.in', '203.0.113.7'
def run(ttl, request_times):
    cache, upstream = Cache(), 0
    for t in request_times:
        if cache.get(NAME,t) is None:
            upstream += 1
            cache.put(NAME, ADDRESS,t,ttl)
    return upstream
for ttl in (20,60,300,3600):
    print(f'TTL {ttl:4d} s: {run(ttl,range(0,3600,5)):3d} authoritative queries in 1 hour')
