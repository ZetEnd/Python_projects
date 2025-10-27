
def Coef(V_nominal, P_nominal, R_anchor, Vel_nominal, Vel_idle):
    I_nominal = P_nominal/V_nominal
    I_idle = I_nominal/8

    coefficient = ( ( V_nominal - I_nominal*R_anchor)/Vel_nominal + (V_nominal - I_idle*R_anchor)/Vel_idle )/2

    return coefficient

def Mechanical_characteristic(V_anchor, R_anchor, Vel_engine, coef):

    M_engine = V_anchor*coef/R_anchor - coef**2*Vel_engine/R_anchor

    return M_engine

def Ñontrol_characteristic(V_anchor, Coef, M_engine, R_anchor):

    vel_engine = V_anchor/Coef - M_engine*R_anchor/(Coef**2)

    return vel_engine

def Moment_characteristic(coef, I_anchor):

    M_engine = coef*I_anchor

    return M_engine

def Power_characteristic(V_anchor, coef, R_anchor, Vel_engine):

    power = V_anchor*coef/R_anchor*Vel_engine - coef**2/R_anchor*Vel_engine**2

    return  power

if __name__ == "__main__":
    V_nominal = 27
    P_nominal = 1.171
    R_anchor = 24
    Vel_nominal = 397.9
    Vel_idle = 528.8
    coefficient = Coef(V_nominal,P_nominal,R_anchor,Vel_nominal,Vel_idle)

    V_anchor = 0

    for velocity in range(0,20,2):
        mechanical_characteristic = Mechanical_characteristic(27,24,velocity,coefficient)
    print()
