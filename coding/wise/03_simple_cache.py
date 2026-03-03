"""
WISE PAIR PROGRAMMING — Problem 3: Simple Cache

SCENARIO:
Currency Exchange service calls external API (~200ms, costs money).
Rates update every ~5 minutes, but we make 10K lookups/min.
Build a cache to avoid redundant calls.
"""

from datetime import datetime, timedelta


class Cache:
    """Generic in-memory cache with TTL per entry."""

    def __init__(self, default_ttl=300, max_size=1000):
        self.default_ttl = timedelta(seconds=default_ttl)  # 5 min
        self.max_size = max_size
        self.store = {}  # {"GBP_USD": {"value": 1.5, "expires_at": datetime}}

    def get(self, key):
        """Return cached value if exists and not expired. None otherwise."""
        entry = self.store.get(key)
        if not entry:
            return None

        if datetime.now() > entry["expires_at"]:
            del self.store[key]
            return None

        self.store[key].update({"last_access": datetime.now()})
        return entry["value"]

    def put(self, key, value, ttl=None):
        """Store value with TTL. Uses default TTL if not specified."""
        if self.size() >= self.max_size:
            oldest_key = min(self.store, key=lambda k: self.store[k]["last_access"])
            self.delete(oldest_key)

        expires_at = datetime.now() + (timedelta(seconds=ttl) if ttl else self.default_ttl)
        self.store[key] = {
            "value": value,
            "expires_at": expires_at,
            "last_access": datetime.now()
        }

    def delete(self, key):
        """Remove entry from cache."""
        self.store.pop(key, None)

    def clear(self):
        """Remove all entries."""
        self.store.clear()

    def size(self):
        return len(self.store)


class CurrencyExchangeService:
    """Fetches exchange rates, using cache to avoid redundant API calls."""

    def __init__(self, cache=None):
        self.cache = cache or Cache(default_ttl=300)

    def get_rate(self, from_currency, to_currency):
        cache_key = f"{from_currency}_{to_currency}"

        # Try cache first
        cached = self.cache.get(cache_key)
        if cached:
            print(f"  CACHE HIT: {cache_key} = {cached}")
            return cached

        # Cache miss — call external API
        print(f"  CACHE MISS: {cache_key} — calling API...")
        rate = self._fetch_rate(from_currency, to_currency)
        self.cache.put(cache_key, rate)
        return rate

    def _fetch_rate(self, from_currency, to_currency):
        """Simulates external API call (~200ms, costs money)."""
        # In production: requests.get(f"https://api.wise.com/rates/{from_currency}/{to_currency}")
        fake_rates = {
            "GBP_USD": 1.27,
            "GBP_BRL": 6.35,
            "USD_BRL": 5.17,
            "USD_NGN": 1370.0,
        }
        return fake_rates.get(f"{from_currency}_{to_currency}", 1.0)


# --- TEST ---
if __name__ == "__main__":
    service = CurrencyExchangeService()

    print("First call (miss):")
    rate = service.get_rate("GBP", "USD")
    print(f"  Rate: {rate}\n")

    print("Second call (hit):")
    rate = service.get_rate("GBP", "USD")
    print(f"  Rate: {rate}\n")

    print("Different pair (miss):")
    rate = service.get_rate("USD", "BRL")
    print(f"  Rate: {rate}\n")

    print(f"Cache size: {service.cache.size()}")
