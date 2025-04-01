import streamlit as st
import sympy as sp

def balancear_combustion(formula):
    """
    Balancea la ecuación de combustión para la fórmula de un compuesto (alcano, alqueno, alquino).
    La fórmula debe ser una cadena de caracteres, como 'C4H10' para el butano.
    """

    # Extraer el número de átomos de C y H de la fórmula
    if 'C' not in formula or 'H' not in formula:
        st.error("Fórmula química inválida. Debe incluir C (Carbono) y H (Hidrógeno).")
        return
    
    n_carbono = int(formula.split('C')[1].split('H')[0]) if 'C' in formula else 1
    n_hidrogeno = int(formula.split('H')[1]) if 'H' in formula else 2

    # Definir las variables simbólicas
    O2, CO2, H2O = sp.symbols('O2 CO2 H2O')

    # Balancear la ecuación de combustión
    # Composición general: CnHm + O2 → CO2 + H2O
    eq1 = sp.Eq(n_carbono, CO2)
    eq2 = sp.Eq(n_hidrogeno / 2, H2O)
    eq3 = sp.Eq(O2 / 2, CO2 + H2O)

    # Resolver las ecuaciones
    resultado = sp.solve((eq1, eq2, eq3))
    
    # Construir la ecuación balanceada
    ecuacion_balanceada = f"{formula} + O2 → CO2 + H2O"
    
    return ecuacion_balanceada

def app():
    st.title("Balanceador de Reacciones de Combustión")
    st.subheader("Balancea la combustión de Alcanos, Alquenos y Alquinos")

    # Entrada del usuario
    formula = st.text_input("Introduce la fórmula del compuesto (ej. C4H10 para Butano):")
    
    if formula:
        st.write(f"Balanceando la combustión de: {formula}")
        
        resultado = balancear_combustion(formula)
        if resultado:
            st.write(f"Reacción balanceada: {resultado}")

if __name__ == "__main__":
    app()
