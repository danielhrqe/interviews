from dataclasses import dataclass

@dataclass
class Account:
    type: str
    balance: float
    currency: str

@dataclass
class User:
    name: str
    email: str

@dataclass
class UserAccount:
    user: User
    account: Account

@dataclass
class ExchangeRate:
    rates = {
            "GBP": {
                "BRL": {"value": 6, "fee": 0.05},
                "USD": {"value": 1.5, "fee": 0.05}
            },
            "BRL": {
                "USD": {"value": 0.19, "fee": 0.05},
                "GBP": {"value": 0.14, "fee": 0.05}
            },
            "USD": {
                "BRL": {"value": 5.17, "fee": 0.05},
                "GBP": {"value": 0.75, "fee": 0.05},
                "NGN": {"value": 1.370, "fee": 0.05}
            }
        }

@dataclass
class Wise:
    balance: float

@dataclass
class Exchange:
    from_user: UserAccount
    to_user: UserAccount
    wise: Wise
    exchangeRate: ExchangeRate

    def _find_route(self, from_currency, to_currency):
        """Find conversion route: direct or via intermediary."""
        from_rates = ExchangeRate.rates.get(from_currency, {})

        # Direct route exists?
        direct = from_rates.get(to_currency)
        if direct:
            return [{"from": from_currency, "to": to_currency, "rate": direct}]

        # No direct route — find intermediary (1 hop)
        for mid_currency, first_hop in from_rates.items():
            mid_rates = ExchangeRate.rates.get(mid_currency, {})
            second_hop = mid_rates.get(to_currency)
            if second_hop:
                return [
                    {"from": from_currency, "to": mid_currency, "rate": first_hop},
                    {"from": mid_currency, "to": to_currency, "rate": second_hop},
                ]

        raise CurrencyRouteNotFound(
            f"No route from {from_currency} to {to_currency}"
        )

    def transfer(self, value):
        if value > self.from_user.account.balance:
            raise MoneyInsufficientException()

        from_currency = self.from_user.account.currency
        to_currency = self.to_user.account.currency

        route = self._find_route(from_currency, to_currency)

        # Apply each hop: fee first, then convert
        current_value = value
        total_fee = 0
        for hop in route:
            fee = current_value * hop["rate"]["fee"]
            total_fee += fee
            current_value = (current_value - fee) * hop["rate"]["value"]

        self.from_user.account.balance -= value
        self.to_user.account.balance += current_value
        self.wise.balance += total_fee


class MoneyInsufficientException(Exception):
    pass

class CurrencyRouteNotFound(Exception):
    pass


# --- TEST: Direct route (GBP → USD) ---
user1 = User(name="Daniel", email="daniel@gmail.com")
account1 = Account(type="current", balance=150, currency="GBP")

user2 = User(name="Joao", email="joao@gmail.com")
account2 = Account(type="current", balance=0, currency="USD")

wise = Wise(balance=0)
exchange = Exchange(UserAccount(user1, account1), UserAccount(user2, account2), wise, ExchangeRate())
exchange.transfer(value=100)

print("=== Direct: GBP → USD ===")
print(f"Daniel: {account1.balance} GBP")
print(f"Joao:   {account2.balance} USD")
print(f"Wise:   {wise.balance} fee collected")

# --- TEST: Indirect route (BRL → NGN via USD) ---
user3 = User(name="Maria", email="maria@gmail.com")
account3 = Account(type="current", balance=1000, currency="BRL")

user4 = User(name="Ade", email="ade@gmail.com")
account4 = Account(type="current", balance=0, currency="NGN")

wise2 = Wise(balance=0)
exchange2 = Exchange(UserAccount(user3, account3), UserAccount(user4, account4), wise2, ExchangeRate())
exchange2.transfer(value=500)

print("\n=== Indirect: BRL → USD → NGN ===")
print(f"Maria: {account3.balance} BRL")
print(f"Ade:   {account4.balance:.2f} NGN")
print(f"Wise:  {wise2.balance:.2f} fee collected")
