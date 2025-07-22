import streamlit as st
import os
from dotenv import load_dotenv
from main import generate_full_company_profile_docx

# Load variabel lingkungan dari .env
load_dotenv()

# Konfigurasi halaman
st.set_page_config(
    page_title="Company Profile Generator",
    page_icon="📄",
    layout="wide"
)

# === HEADER ===
st.markdown("""
    <div style='text-align: center; margin-bottom: 20px;'>
        <h1 style='color:#4B8BBE;'>📄 Company Profile Generator</h1>
        <p style='color:gray;'>Buat dokumen BAB II profil perusahaan resmi secara otomatis</p>
        <hr style='border: 1px solid #ddd;'/>
    </div>
""", unsafe_allow_html=True)

# === SIDEBAR MENU ===
menu = st.sidebar.selectbox("📂 Navigasi", ["Buat Dokumen Bab II", "Tentang Aplikasi"])

# === MENU: BUAT DOKUMEN ===
if menu == "Buat Dokumen Bab II":
    st.subheader("🧾 Formulir Input")

    with st.form("form_input"):
        company_name = st.text_input("Masukkan Nama Perusahaan", placeholder="Contoh: PT Pelabuhan Indonesia (Persero)")

        st.markdown("### 🤖 Pilih Model Gemini")
        model_options = [
            "models/gemini-1.5-flash-latest",
            "models/gemini-1.5-pro-latest",
            "models/gemini-2.5-flash",
            "models/gemini-2.5-pro"
        ]
        selected_model = st.selectbox("Model AI", model_options, index=0)

        st.markdown("### ⚙️ Parameter Gemini")
        temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.05)

        submitted = st.form_submit_button("🚀 Buat Dokumen")

    if submitted and company_name.strip():
        with st.spinner("Sedang membuat dan mengunggah dokumen..."):
            try:
                file_path, drive_url = generate_full_company_profile_docx(
                    company_name=company_name.strip(),
                    temperature=temperature,
                    upload=True,
                    drive_folder_id=os.getenv("GOOGLE_DRIVE_FOLDER_ID"),
                    model_name=selected_model
                )

                with open(file_path, "rb") as f:
                    st.success("✅ Dokumen berhasil dibuat dan diupload ke Google Drive!")
                    st.download_button(
                        label="📥 Download DOCX",
                        data=f,
                        file_name=os.path.basename(file_path),
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                    if drive_url:
                        st.markdown(f"📤 [Lihat file di Google Drive]({drive_url})", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"❌ Terjadi kesalahan: {e}")
    elif submitted:
        st.warning("⚠️ Nama perusahaan tidak boleh kosong.")

# === MENU: TENTANG APLIKASI ===
elif menu == "Tentang Aplikasi":
    st.subheader("ℹ️ Tentang Aplikasi")
    st.markdown("""
    Aplikasi ini dirancang untuk membantu penyusunan dokumen BAB II Profil Perusahaan secara otomatis berdasarkan nama perusahaan yang dimasukkan pengguna.

    ✅ **Fitur Unggulan:**
    - Penyusunan struktur BAB II
    - Konten dihasilkan otomatis menggunakan Gemini (Google AI)
    - Referensi ditampilkan secara eksplisit
    - Dokumen otomatis diupload ke Google Drive
    - Pemilihan model Gemini dan kontrol kreativitas (temperature)

    **Teknologi yang Digunakan:** Streamlit · Gemini API · Python-docx · Google Drive API
    """)

# === FOOTER ===
st.markdown("""
<hr style='border: 0.5px solid #ccc;'/>
<div style='text-align: center; color: gray; font-size: small;'>
    © 2025 Company Profile Generator · Dibuat oleh Tim XXX
</div>
""", unsafe_allow_html=True)
