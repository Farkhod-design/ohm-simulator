import streamlit as st

st.set_page_config(page_title="Ohm qonuni simulyatori", layout="wide")

st.title("Ohm qonuni interaktiv simulyatori")
st.markdown("### V = I × R")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Qiymatlarni o‘zgartiring")

    V = st.slider("Kuchlanish Vs (V)", 1.0, 24.0, 12.0, 0.5)
    R = st.slider("Qarshilik R (Ω)", 1.0, 20.0, 6.0, 0.5)

    I = V / R

    st.markdown("---")
    st.latex(r"V = I \cdot R")
    st.latex(r"I = \frac{V}{R}")
    st.latex(fr"I = \frac{{{V}}}{{{R}}} = {I:.2f}\ A")

    st.success(f"Tok kuchi: I = {I:.2f} A")

with col2:
    st.subheader("Elektr zanjiri")

    speed = min(I * 8, 30)

    circuit_html = f"""
    <div style="
        width: 520px;
        height: 360px;
        border: 2px solid #ddd;
        border-radius: 20px;
        position: relative;
        background: #fafafa;
        margin-top: 20px;
    ">

        <!-- Batareya -->
        <div style="
            position:absolute;
            left:60px;
            top:130px;
            width:70px;
            height:130px;
            border:4px solid #333;
            border-radius:10px;
            background:white;
            text-align:center;
            font-size:28px;
            font-weight:bold;
            line-height:60px;
        ">
            +<br>-
        </div>

        <!-- Simlar -->
        <div style="position:absolute; left:130px; top:155px; width:130px; height:5px; background:#777;"></div>
        <div style="position:absolute; left:360px; top:155px; width:100px; height:5px; background:#777;"></div>
        <div style="position:absolute; left:455px; top:155px; width:5px; height:160px; background:#777;"></div>
        <div style="position:absolute; left:95px; top:315px; width:365px; height:5px; background:#777;"></div>
        <div style="position:absolute; left:95px; top:260px; width:5px; height:60px; background:#777;"></div>

        <!-- Rezistor -->
        <div style="
            position:absolute;
            left:260px;
            top:120px;
            width:100px;
            height:70px;
            border:4px solid #888;
            border-radius:10px;
            background:#eef5fb;
            text-align:center;
            line-height:70px;
            font-size:20px;
        ">
            R
        </div>

        <!-- Tok animatsiyasi -->
        <div class="dot dot1"></div>
        <div class="dot dot2"></div>
        <div class="dot dot3"></div>

        <div style="
            position:absolute;
            left:250px;
            top:55px;
            color:#1e88e5;
            font-size:20px;
            font-weight:bold;
        ">
            I = {I:.2f} A →
        </div>

        <div style="
            position:absolute;
            left:170px;
            top:210px;
            font-size:18px;
            color:#444;
        ">
            Vs = {V:.1f} V
        </div>

        <div style="
            position:absolute;
            left:270px;
            top:205px;
            font-size:18px;
            color:#444;
        ">
            R = {R:.1f} Ω
        </div>
    </div>

    <style>
    .dot {{
        width: 14px;
        height: 14px;
        background: #2196f3;
        border-radius: 50%;
        position: absolute;
        top: 150px;
        animation: moveDot {max(1, 8-speed/5)}s linear infinite;
    }}

    .dot1 {{
        animation-delay: 0s;
    }}

    .dot2 {{
        animation-delay: 0.4s;
    }}

    .dot3 {{
        animation-delay: 0.8s;
    }}

    @keyframes moveDot {{
        0%   {{ left: 130px; top: 150px; }}
        35%  {{ left: 450px; top: 150px; }}
        55%  {{ left: 450px; top: 310px; }}
        85%  {{ left: 95px; top: 310px; }}
        100% {{ left: 95px; top: 250px; }}
    }}
    </style>
    """

    st.components.v1.html(circuit_html, height=420)

st.markdown("---")
st.info("Kuchlanish oshsa tok ortadi. Qarshilik oshsa tok kamayadi.")