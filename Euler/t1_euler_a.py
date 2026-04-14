# ============================================================
# TAREA 1 - MÉTODO DE EULER
# y' = x*sqrt(y),  y(1)=4,  evaluar y(10)
# ============================================================
import math

def f(x, y):
    return x * math.sqrt(y)

def euler(x0, y0, xf, h):
    steps = round((xf - x0) / h)
    x, y = x0, y0
    SEP = '+------+----------------+------------------+------------------+'
    HDR = '|  n   |       Xn       |        Yn        |     f(Xn,Yn)     |'
    print(SEP); print(HDR); print(SEP)
    print(f"| {0:^4} | {x:^14.10f} | {y:^16.10f} | {f(x,y):^16.10f} |")
    for n in range(1, steps + 1):
        fn    = f(x, y)
        y_new = y + h * fn
        x_new = round(x + h, 10)
        if n <= 3:
            print(f"| {n:^4} | {x_new:^14.10f} | {y_new:^16.10f} | {f(x_new,y_new):^16.10f} |")
        elif n == 4 and steps > 4:
            print('|      |      ...       |       ...        |       ...        |')
        elif n == steps:
            print(f"| {n:^4} | {x_new:^14.10f} | {y_new:^16.10f} | {f(x_new,y_new):^16.10f} |")
        x, y = x_new, y_new
    print(SEP)
    return y

x0, y0, xf = 1.0, 4.0, 10.0
for h in [0.1, 0.001, 0.00001]:
    print("\n" + "="*70)
    print(f"  EULER | y'=x*sqrt(y) | y(1)=4 | h={h}")
    print("="*70)
    r = euler(x0, y0, xf, h)
    print(f"  Resultado: y(10) = {r:.10f}")