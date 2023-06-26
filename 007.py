from decimal import Decimal
from decimal import getcontext

print(0.3 + 0.3 + 0.3 - 0.9)

Decimal('0.3') + Decimal('0.3') + Decimal('0.3') - Decimal('0.9')
print(Decimal('0.0'))

print(1/3)

getcontext().prec = 3
print(Decimal('1') / Decimal('3'))
print(Decimal('1') / 3 == Decimal('0.333'))
