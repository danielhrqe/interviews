"""
WISE REAL INTERVIEW — Circuit Breaker (3/mar/2026)

EXACT PROBLEM:
Service A calls Service B and Service C every time.
If one service fails 3 times in 10 minutes (20 seconds in test),
the next call is BLOCKED for 5 minutes (10 seconds in test).
After cooldown, ALL requests are unblocked (no HALF_OPEN).

Given: simulation of remote method calls.
Implement: execute() which calls the remote service if possible.

STATES (simplified — no HALF_OPEN):
  CLOSED ──3 fails in 10min──→ OPEN ──5min cooldown──→ CLOSED
"""

from datetime import datetime, timedelta


class CircuitBreakerOpenError(Exception):
    pass


class CircuitBreaker:
    CLOSED = "CLOSED"
    OPEN = "OPEN"

    def __init__(self, failure_threshold=3, failure_window_seconds=600, cooldown_seconds=300):
        self.failure_threshold = failure_threshold
        self.failure_window = timedelta(seconds=failure_window_seconds)
        self.cooldown = timedelta(seconds=cooldown_seconds)
        self.services = {}

    def _get_service(self, service_name):
        if service_name not in self.services:
            self.services[service_name] = {
                "state": self.CLOSED,
                "failures": [],
                "opened_at": None,
            }
        return self.services[service_name]

    def allow_request(self, service_name):
        service = self._get_service(service_name)
        now = datetime.now()

        if service["state"] == self.CLOSED:
            return True

        # OPEN — check if cooldown has passed
        if now - service["opened_at"] >= self.cooldown:
            # Cooldown done → unblock everything (no HALF_OPEN)
            service["state"] = self.CLOSED
            service["failures"] = []
            service["opened_at"] = None
            return True

        return False  # still blocked

    def record_failure(self, service_name):
        service = self._get_service(service_name)
        now = datetime.now()

        # Record failure timestamp
        service["failures"].append(now)

        # Keep only failures within the window
        cutoff = now - self.failure_window
        service["failures"] = [t for t in service["failures"] if t > cutoff]

        # Hit threshold → open circuit
        if len(service["failures"]) >= self.failure_threshold:
            service["state"] = self.OPEN
            service["opened_at"] = now

    def record_success(self, service_name):
        # In this simplified version, success just means it worked.
        # No state change needed (no HALF_OPEN to transition from).
        pass


def execute(service_name: str, remote_call, circuit_breaker: CircuitBreaker):
    """
    Calls the remote service if the circuit breaker allows it.
    This is the method we needed to implement in the interview.
    """
    if not circuit_breaker.allow_request(service_name):
        raise CircuitBreakerOpenError(
            f"{service_name} is blocked. Try again later."
        )

    try:
        result = remote_call()
        circuit_breaker.record_success(service_name)
        return result
    except Exception as e:
        circuit_breaker.record_failure(service_name)
        raise e


# --- SIMULATION (like the interview) ---
if __name__ == "__main__":
    # Using test values: 20 second window, 10 second cooldown
    cb = CircuitBreaker(
        failure_threshold=3,
        failure_window_seconds=20,
        cooldown_seconds=10,
    )

    call_count = 0

    def service_b_always_fails():
        raise Exception("Service B is down")

    def service_c_works():
        return "OK from Service C"

    # Simulate: Service B fails 3 times → gets blocked
    print("=== Service B failing ===")
    for i in range(5):
        try:
            execute("service_b", service_b_always_fails, cb)
        except CircuitBreakerOpenError:
            print(f"  Call {i}: BLOCKED (circuit open)")
        except Exception:
            print(f"  Call {i}: FAILED (error recorded)")

    # Service C still works — independent circuit
    print("\n=== Service C still works ===")
    for i in range(3):
        try:
            result = execute("service_c", service_c_works, cb)
            print(f"  Call {i}: {result}")
        except Exception as e:
            print(f"  Call {i}: ERROR — {e}")

    print(f"\nService B state: {cb.services['service_b']['state']}")
    print(f"Service C state: {cb.services['service_c']['state']}")
