# ============================================================
# TAREA 3 - RUNGE-KUTTA CUARTO ORDEN (RK4)
# y' = y*tan(x),  y(0)=1,  evaluar y(5)
# ============================================================
import math

def f(x, y):
    return y * math.tan(x)

def rk4(x0, y0, xf, h):
    steps = round((xf - x0) / h)
    x, y = x0, y0
    SEP = '+------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+'
    HDR = '|  n   |       Xn       |       K1       |       K2       |       K3       |       K4       |       Yn       |    f(Xn,Yn)    |'
    print(SEP); print(HDR); print(SEP)
    for n in range(1, steps + 1):
        k1 = f(x,       y)
        k2 = f(x + h/2, y + h*k1/2)
        k3 = f(x + h/2, y + h*k2/2)
        k4 = f(x + h,   y + h*k3)
        y_new = y + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        x_new = round(x + h, 10)
        fn    = f(x_new, y_new)
        if n <= 3:
            print(f"| {n:^4} | {x_new:^14.10f} | {k1:^14.10f} | {k2:^14.10f} | {k3:^14.10f} | {k4:^14.10f} | {y_new:^14.10f} | {fn:^14.10f} |")
        elif n == 4 and steps > 4:
            print('|      |      ...       |      ...       |      ...       |      ...       |      ...       |      ...       |      ...       |')
        elif n == steps:
            print(f"| {n:^4} | {x_new:^14.10f} | {k1:^14.10f} | {k2:^14.10f} | {k3:^14.10f} | {k4:^14.10f} | {y_new:^14.10f} | {fn:^14.10f} |")
        x, y = x_new, y_new
    print(SEP)
    return y

x0, y0, xf = 0.0, 1.0, 5.0
for h in [0.1, 0.001, 0.00001]:
    print("\n" + "="*120)
    print(f"  RK4 | y'=y*tan(x) | y(0)=1 | h={h}")
    print("="*120)
    r = rk4(x0, y0, xf, h)
    print(f"  Resultado: y(5) = {r:.10f}")