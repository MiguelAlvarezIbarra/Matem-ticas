# ============================================================
# TAREA 2 - MÉTODO DE EULER MODIFICADO (Heun)
# y' = x + y^2,  y(1)=0,  evaluar y(1.5)
# ============================================================


def f(x, y):
    return x + y**2

def euler_modificado(x0, y0, xf, h):
    steps = round((xf - x0) / h)
    x, y = x0, y0
    SEP = '+------+------------------+------------------+------------------+------------------+------------------+'
    HDR = '|  n   |        Xn        |       Yn*        |    f(Xn,Yn*)     |        Yn        |     f(Xn,Yn)     |'
    print(SEP); print(HDR); print(SEP)
    for n in range(1, steps + 1):
        k1     = f(x, y)
        x_new  = round(x + h, 10)
        y_pred = y + h * k1
        k2     = f(x_new, y_pred)
        y_new  = y + h * (k1 + k2) / 2.0
        fn_new = f(x_new, y_new)
        if n <= 3:
            print(f"| {n:^4} | {x_new:^16.10f} | {y_pred:^16.10f} | {k2:^16.10f} | {y_new:^16.10f} | {fn_new:^16.10f} |")
        elif n == 4 and steps > 4:
            print('|      |       ...        |       ...        |       ...        |       ...        |       ...        |')
        elif n == steps:
            print(f"| {n:^4} | {x_new:^16.10f} | {y_pred:^16.10f} | {k2:^16.10f} | {y_new:^16.10f} | {fn_new:^16.10f} |")
        x, y = x_new, y_new
    print(SEP)
    return y

x0, y0, xf = 1.0, 0.0, 1.5
for h in [0.1, 0.001, 0.00001]:
    print("\n" + "="*100)
    print(f"  EULER MOD | y'=x+y^2 | y(1)=0 | h={h}")
    print("="*100)
    r = euler_modificado(x0, y0, xf, h)
    print(f"  Resultado: y(1.5) = {r:.10f}")