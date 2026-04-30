import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Diod VAX simulyatori", layout="wide")

st.title("Yarim o‘tkazgichli diod VAX simulyatori")
st.markdown("### Diodning volt-amper xarakteristikasi")

st.markdown("""
Ushbu virtual laboratoriyada diod kuchlanishi o‘zgarganda tok qanday o‘zgarishi kuzatiladi.
Diod toki Shockley tenglamasi orqali hisoblanadi:
""")

st.subheader("Diodning matematik modeli")

st.latex(r"I_D = I_S \left(e^{\frac{V_D}{nV_T}} - 1\right)")

col1, col2 = st.columns([1, 1.5])

with col1:
    st.subheader("Parametrlarni sozlash")

    diode_type = st.selectbox(
        "Diod turi",
        ["Kremniy diod", "Germaniy diod", "Ideal diod"]
    )

    if diode_type == "Kremniy diod":
        Is = st.slider("Teskari to‘yinish toki Is (nA)", 1.0, 100.0, 10.0, 1.0) * 1e-9
        n = st.slider("Ideallik koeffitsiyenti n", 1.0, 2.5, 1.8, 0.1)
        threshold = 0.7

    elif diode_type == "Germaniy diod":
        Is = st.slider("Teskari to‘yinish toki Is (nA)", 10.0, 500.0, 100.0, 10.0) * 1e-9
        n = st.slider("Ideallik koeffitsiyenti n", 1.0, 2.5, 1.5, 0.1)
        threshold = 0.3

    else:
        Is = 1e-12
        n = 1.0
        threshold = st.slider("Ideal ochilish kuchlanishi (V)", 0.0, 1.0, 0.7, 0.05)

    temperature = st.slider("Harorat T (°C)", 0, 100, 25, 1)
    selected_voltage = st.slider("Diod kuchlanishi Vd (V)", -1.0, 1.0, 0.7, 0.01)

    T_kelvin = temperature + 273.15
    k = 1.380649e-23
    q = 1.602176634e-19
    Vt = k * T_kelvin / q

    if diode_type == "Ideal diod":
        selected_current = 0 if selected_voltage < threshold else (selected_voltage - threshold) * 1000
    else:
        selected_current = Is * (np.exp(selected_voltage / (n * Vt)) - 1)

    st.markdown("---")
    st.metric("Termik kuchlanish Vt", f"{Vt:.4f} V")
    st.metric("Tanlangan kuchlanish Vd", f"{selected_voltage:.2f} V")
    st.metric("Diod toki Id", f"{selected_current * 1000:.3f} mA")

    if selected_voltage < 0:
        st.warning("Diod teskari yo‘nalishda ulangan. Tok juda kichik.")
    elif selected_voltage < threshold:
        st.info("Diod hali to‘liq ochilmagan.")
    else:
        st.success("Diod ochilgan holatda ishlayapti.")

with col2:
    st.subheader("Volt-amper xarakteristika grafigi")

    V = np.linspace(-1, 1, 1000)

    if diode_type == "Ideal diod":
        I = np.where(V < threshold, 0, (V - threshold) * 1000)
    else:
        I = Is * (np.exp(V / (n * Vt)) - 1)

    I_mA = I * 1000
    selected_current_mA = selected_current * 1000

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(V, I_mA, linewidth=2, label="Diod VAX")
    ax.scatter(
        selected_voltage,
        selected_current_mA,
        s=80,
        label="Ishchi nuqta"
    )

    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)

    ax.set_xlabel("Diod kuchlanishi Vd (V)")
    ax.set_ylabel("Diod toki Id (mA)")
    ax.set_title(f"{diode_type} volt-amper xarakteristikasi")
    ax.grid(True)
    ax.legend()

    ax.set_ylim(min(I_mA) - 1, max(20, min(max(I_mA), 100)))

    st.pyplot(fig)

st.markdown("---")

st.subheader("Qisqacha nazariy izoh")

st.markdown("""
**Diod** — tokni asosan bir yo‘nalishda o‘tkazadigan yarim o‘tkazgichli element.

- **To‘g‘ri ulanishda** diod ochiladi va tok tez ortadi.
- **Teskari ulanishda** juda kichik teskari tok oqadi.
- **Kremniy diod** odatda taxminan **0.7 V** atrofida ochiladi.
- **Germaniy diod** odatda taxminan **0.3 V** atrofida ochiladi.

Bu grafik diodning asosiy VAX xususiyatini tushunishga yordam beradi.
""")