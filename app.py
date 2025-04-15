import streamlit as st
from calc import cal, risk_contracts_calc
from list import instruments, get_list, get_instruments

st.set_page_config(page_title="calculadora de futuros", layout="centered")


menu = st.sidebar.selectbox(
    "Selecciona una opción",
    [
        "Calculadora",
        "Lista de Instrumentos",
        "Calculadora de Puntos",
        "Cálculo de Contratos por Riesgo",
        "Salir"
    ]
)

if menu == "Calculadora":
    st.subheader("📊 Calculadora de Futuros")

    try:
        account_balance = st.number_input("💰 Total de la cuenta (USD)", min_value=0.0)
        symbol = st.selectbox("📌 Selecciona el instrumento", list(instruments.keys()))
        risk_amount = st.number_input("⚠️ Porcentaje de riesgo (ej: 0.01 para 1%)", min_value=0.0, max_value=1.0)
        stop_loss = st.number_input("🛑 Stop loss (puntos)", min_value=0.0)
        reward = st.number_input("🎯 Reward (puntos)", min_value=0.0)

        if st.button("Calcular"):
            info = get_list(symbol)
            if not info:
                st.error("❌ Instrumento no reconocido.")
            else:
                try:
                    resultado = cal(account_balance, risk_amount, stop_loss, info, reward)
                    st.success("✅ Resultado:")
                    for k, v in resultado.items():
                        st.write(f"{k}: {v}")
                except Exception as e:
                    st.error(f"Error en cálculo: {e}")

    except Exception as e:
        st.error(f"Error: {e}")

elif menu == "Lista de Instrumentos":
    st.subheader("📌 Lista de instrumentos")
    instruments_data = get_instruments()
    for k, v in instruments_data.items():
        st.write(f"• {k.upper()} → ${v['valor_p']} por punto")

elif menu == "Calculadora de Puntos":
    st.subheader("🧮 Calculadora de Puntos")
    item = st.selectbox("📌 Selecciona el instrumento", list(instruments.keys()))
    cantidad = st.number_input("Cantidad de puntos", min_value=0.0)

    if st.button("Calcular monto en USD"):
        resultado = instruments[item]['valor_p'] * cantidad
        st.success(f"💵 Monto en USD: ${resultado:.2f}")

elif menu == "Cálculo de Contratos por Riesgo":
    st.subheader("📏 Cálculo de Contratos por Riesgo")

    try:
        risk_dollars = st.number_input("¿Cuánto deseas arriesgar en USD?", min_value=0.0)
        symbol = st.selectbox("📌 Selecciona el instrumento", list(instruments.keys()))
        stop_loss = st.number_input("Stop loss (en puntos)", min_value=0.0)

        if st.button("Calcular contratos"):
            info = get_list(symbol)
            if not info:
                st.error("❌ Instrumento no reconocido.")
            else:
                resultado = risk_contracts_calc(risk_dollars, stop_loss, info)
                st.success("✅ Resultado:")
                for k, v in resultado.items():
                    st.write(f"{k}: {v}")
    except Exception as e:
        st.error(f"Error: {e}")

elif menu == "Salir":
    st.info("Gracias por usar la calculadora ✨")