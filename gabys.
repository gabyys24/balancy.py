import streamlit as st
import re
from fractions import Fraction

st.set_page_config(page_title="Balanceador de Combustión", layout="centered")

st.title("🔥 Balanceador de Reacciones de Combustión")
st.write("Introduce la fórmula de un alcano, alqueno o alquino (ej: `C2H6`, `C3H4`)")

formula = st.text_input("Fórmula molecular del hidrocarburo:")

def parse_formula(formula):
    """Extrae número de átomos de C y H"""
    match = re.fullmatch(r"C(\d*)H(\d+)", formula.strip())
    if not match:
        return None, None
    c = int(match.group(1)) if match.group(1) else 1
    h = int(match.group(2))
    return c, h

def balance_combustion(c, h):
    co2 = c
    h2o = Fraction(h, 2)
    oxy_needed = 2 * co2 + h2o
    o2 = Fraction(oxy_needed, 2)
    return co2, h2o, o2

def get_type(c, h):
    if h == 2 * c + 2:
        return "Alcano (CnH₂n₊₂)"
    elif h == 2 * c:
        return "Alqueno (CnH₂n)"
    elif h == 2 * c - 2:
        return "Alquino (CnH₂n₋₂)"
    else:
        return "No es un alcano, alqueno ni alquino conocido"

if formula:
    c, h = parse_formula(formula)
    if c is None:
        st.error("Fórmula no válida. Usa el formato como C2H6, C3H4, etc.")
    else:
        tipo = get_type(c, h)
        co2, h2o, o2 = balance_combustion(c, h)
        st.markdown(f"**Tipo de compuesto:** {tipo}")
        st.markdown("### Reacción balanceada:")

        # Si hay fracciones, multiplicamos todo por el mínimo común denominador
        if not o2.denominator == 1:
            lcm = o2.denominator
            equation = f"{lcm} C{c}H{h} + {lcm * o2} O₂ → {lcm * co2} CO₂ + {lcm * h2o} H₂O"
        else:
            equation = f"C{c}H{h} + {o2} O₂ → {co2} CO₂ + {h2o} H₂O"

        st.latex(equation)
