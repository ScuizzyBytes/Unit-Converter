units = {
    "USD": 1.0,
    "RUB": 92.0,
    "EURO": 0.925,
    "UAH": 41.5
}

from_unit = input(f"atake a unit {list(units.keys())}\n: ").strip().upper()
amount = float(input("how much ta wanna to convert\n: "))

def convert_currency(units, from_curr, to_curr, amount):
    amount_total = amount / units[from_curr]

    result = amount_total * units[to_curr]

    return round(result, 2)

print(f"\n{amount} {from_unit} = {convert_currency(units, from_unit, 'EURO', amount)} EURO")
print(f"{amount} {from_unit} = {convert_currency(units, from_unit, 'UAH', amount)} UAH")
print(f"{amount} {from_unit} = {convert_currency(units, from_unit, 'RUB', amount)} USD")
print(f"{amount} {from_unit} = {convert_currency(units, from_unit, 'USD', amount)} RUB")