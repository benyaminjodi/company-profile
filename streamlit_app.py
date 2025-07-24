# streamlit_app.py

import streamlit as st
import os
from dotenv import load_dotenv
from main import generate_bab2_docx, generate_bab3_docx, generate_bab4_docx

# Load env lokal
load_dotenv()

st.set_page_config(
    page_title="Company Profile Generator",
    page_icon="📄",
    layout="wide"
)

st.markdown("""
    <div style='text-align: center; margin-bottom: 20px;'>
        <h1 style='color:#4B8BBE;'>📄 Company Profile Generator</h1>
        <p style='color:gray;'>Buat dokumen BAB II dan BAB III profil perusahaan secara otomatis</p>
        <hr style='border: 1px solid #ddd;'/>
    </div>
""", unsafe_allow_html=True)

menu = st.sidebar.selectbox("📂 Navigasi", ["Buat Dokumen Bab II", "Buat Dokumen Bab III", "Buat Dokumen Bab IV", "Tentang Aplikasi"])

if menu == "Buat Dokumen Bab II":
    st.subheader("🧾 Formulir Input Bab II")

    with st.form("form_input_bab2"):
        company_name = st.text_input("Masukkan Nama Perusahaan", placeholder="Contoh: PT Pelabuhan Indonesia (Persero)")
        model_options = [
            "models/gemini-1.5-flash-latest",
            "models/gemini-1.5-pro-latest",
            "models/gemini-2.5-flash",
            "models/gemini-2.5-pro"
        ]
        selected_model = st.selectbox("Model AI", model_options, index=0)
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.05)
        submitted = st.form_submit_button("🚀 Buat Dokumen Bab II")

    if submitted and company_name.strip():
        with st.spinner("Sedang membuat dokumen Bab II..."):
            try:
                file_path, tokens_in, tokens_out = generate_bab2_docx(
                    company_name=company_name.strip(),
                    temperature=temperature,
                    model_name=selected_model
                )
                with open(file_path, "rb") as f:
                    st.success("✅ Dokumen Bab II berhasil dibuat!")
                    st.download_button("📥 Download DOCX", f, file_name=os.path.basename(file_path), mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
                st.markdown(f"🔢 **Token Input**: `{tokens_in}`")
                st.markdown(f"🧾 **Token Output**: `{tokens_out}`")
            except Exception as e:
                st.error(f"❌ Terjadi kesalahan: {e}")
    elif submitted:
        st.warning("⚠️ Nama perusahaan tidak boleh kosong.")

elif menu == "Buat Dokumen Bab III":
    st.subheader("🧾 Formulir Input Bab III")

    with st.form("form_input_bab3"):
        company_name = st.text_input("Masukkan Nama Perusahaan", placeholder="Contoh: PT Pelabuhan Indonesia (Persero)")
        model_options = [
            "models/gemini-1.5-flash-latest",
            "models/gemini-1.5-pro-latest",
            "models/gemini-2.5-flash",
            "models/gemini-2.5-pro"
        ]
        selected_model = st.selectbox("Model AI", model_options, index=0)
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.05)
        submitted = st.form_submit_button("🚀 Buat Dokumen Bab III")

    if submitted and company_name.strip():
        with st.spinner("Sedang membuat dokumen Bab III..."):
            try:
                file_path, tokens_in, tokens_out = generate_bab3_docx(
                    company_name=company_name.strip(),
                    temperature=temperature,
                    model_name=selected_model
                )
                with open(file_path, "rb") as f:
                    st.success("✅ Dokumen Bab III berhasil dibuat!")
                    st.download_button("📥 Download DOCX", f, file_name=os.path.basename(file_path), mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
                st.markdown(f"🔢 **Token Input**: `{tokens_in}`")
                st.markdown(f"🧾 **Token Output**: `{tokens_out}`")
            except Exception as e:
                st.error(f"❌ Terjadi kesalahan: {e}")
    elif submitted:
        st.warning("⚠️ Nama perusahaan tidak boleh kosong.")

elif menu == "Buat Dokumen Bab IV":
    st.subheader("🧾 Formulir Input Bab IV")

    with st.form("form_input_bab3"):
        company_name = st.text_input("Masukkan Nama Perusahaan", placeholder="Contoh: PT Pelabuhan Indonesia (Persero)")
        model_options = [
            "models/gemini-1.5-flash-latest",
            "models/gemini-1.5-pro-latest",
            "models/gemini-2.5-flash",
            "models/gemini-2.5-pro"
        ]
        selected_model = st.selectbox("Model AI", model_options, index=0)
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.05)
        submitted = st.form_submit_button("🚀 Buat Dokumen Bab IV")

    if submitted and company_name.strip():
        with st.spinner("Sedang membuat dokumen Bab IV..."):
            try:
                file_path, tokens_in, tokens_out = generate_bab4_docx(
                    company_name=company_name.strip(),
                    temperature=temperature,
                    model_name=selected_model
                )
                with open(file_path, "rb") as f:
                    st.success("✅ Dokumen Bab IV berhasil dibuat!")
                    st.download_button("📥 Download DOCX", f, file_name=os.path.basename(file_path), mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
                st.markdown(f"🔢 **Token Input**: `{tokens_in}`")
                st.markdown(f"🧾 **Token Output**: `{tokens_out}`")
            except Exception as e:
                st.error(f"❌ Terjadi kesalahan: {e}")
    elif submitted:
        st.warning("⚠️ Nama perusahaan tidak boleh kosong.")

elif menu == "Tentang Aplikasi":
    st.subheader("ℹ️ Tentang Aplikasi")
    st.markdown("""
    Aplikasi ini membantu menyusun dokumen Bab II dan Bab III profil perusahaan secara otomatis.

    ✅ Fitur:
    - Struktur formal dan profesional
    - AI-powered dengan Gemini
    - Output file `.docx` siap edit
    """)
