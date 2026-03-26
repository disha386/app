import streamlit as st
import sqlite3
import os
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="MY WEBSITE", layout="wide")
##deploy hide
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
.block-container {
    padding-top: 0rem !important;
    padding-left: 20px !important;
    padding-right: 20px !important;
}

    

</style>
""", unsafe_allow_html=True)

# ================= DATABASE =================
conn = sqlite3.connect("portal.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image BLOB
)
""")
conn.commit()

# ================= INSERT IMAGES (ONLY ONCE) =================
def insert_image(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            cursor.execute("INSERT INTO images (image) VALUES (?)", (f.read(),))
    else:
        st.error(f"❌ Image not found: {path}")

# Insert only if empty
cursor.execute("SELECT COUNT(*) FROM images")
count = cursor.fetchone()[0]

if count == 0:
    insert_image("images/discover-section-img.webp")
    insert_image("images/ISO1.webp")
    insert_image("images/ISO2.webp")
    insert_image("images/ISO-9001-2015.webp")
    conn.commit()

# ================= GET IMAGES =================
def get_images():
    cursor.execute("SELECT image FROM images ORDER BY id ASC")
    return cursor.fetchall()

# ================= NAVBAR =================
# ================= NAVBAR =================
# ================= NAVBAR =================
logo_url = "https://res.cloudinary.com/dnodncslz/image/upload/v1774502957/header-logo_rdttb2.webp"
components.html(f"""
<style>
.navbar {{
        display:flex;
    align-items:center;
    justify-content:space-between;
    background:#f8f8f8;
    padding:6px 20px;
    font-family:sans-serif;
}}

.navbar-left {{
    display:flex;
    align-items:center;
}}

.logo {{
    height:60px;
}}




/* CENTER MENU */
.navbar-center {{
     display:flex;
    gap:12px;
    align-items:center;
}}


/* RIGHT SIDE */
.navbar-right {{
     padding:8px 16px;
    border-radius:6px;
    text-decoration:none;
    font-weight:600;
}}

/* BUTTONS */
.navbar-right a {{
    padding:8px 16px;
    border-radius:6px;
    text-decoration:none;
    font-weight:600;
}}

.login-btn {{
    background:white;
    border:1px solid #ccc;
    color:black;
}}

.contact-btn {{
    background:#ffb900;
    color:white;
}}

/* LOGO */
.logo {{
    height:70px;
    object-fit:contain;
}}

/* ARROW BETWEEN ITEMS */
.arrow {{
    width:6px;
    height:6px;
    border-right:2px solid black;
    border-bottom:2px solid black;
    transform: rotate(45deg);   /* 👈 creates arrow */
    margin: 0 6px;
}}

</style>

<div class="navbar">

    <!-- LOGO LEFT -->
    <div class="navbar-left">
        <img class="logo" src="{logo_url}">
    </div>

    <!-- CENTER MENU -->
    <div class="navbar-center">

    <span>Home</span>
    <span class="arrow"></span>

    <span>About Us</span>
    <span class="arrow"></span>

    <span>Career</span>
    <span class="arrow"></span>

    <span>Resources</span>
    <span class="arrow"></span>

    <span>Blog</span>

</div>

    <!-- RIGHT BUTTONS -->
    <div class="navbar-right">
        <a class="login-btn" href="#">Login</a>
        <a class="contact-btn" href="#">Get in Touch</a>
    </div>

</div>
""", height=90)
######  content
st.markdown("""
<div style="
    margin-top:20px;
    margin-left:0px;
    width:100%;
    font-size:52px;
    font-family: Georgia, serif;
    font-weight:700;
    color:#002366;
    line-height:1.3;
">
    Constructing Certinity with BIM Technology
</div>
""", unsafe_allow_html=True)


















import streamlit as st
import streamlit.components.v1 as components


video_url = "https://res.cloudinary.com/dnodncslz/video/upload/v1774435343/pinnacle-infotech-latest_h3qbk3.mp4"

components.html(f"""
<div style="
    width:100%;
    margin-top:20px;
">

    <video autoplay muted loop playsinline 
        style="
            width:100%;
            height:auto;
            border-radius:12px;
        ">
        <source src="{video_url}" type="video/mp4">
    </video>

</div>
""", height=520)


# ================= IMAGE SECTION =================
# ================= IMAGE SECTION =================
# ================= IMAGE SECTION =================
# ================= IMAGE SECTION =================
def to_base64(img):
    return base64.b64encode(img).decode()

images = get_images()

if len(images) >= 4:
    main_img = to_base64(images[0][0])
    iso1 = to_base64(images[1][0])
    iso2 = to_base64(images[2][0])
    iso3 = to_base64(images[3][0])
html = f"""
<div style='
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:50px;
    margin-top:60px;
    width:100%;
'>

    <!-- LEFT TEXT -->
    <div style='width:45%;'>

        <h2 style='color:#002366; font-size:34px; font-weight:700;'>
            Discover Pinnacle
        </h2>

        <p style='font-size:16px; line-height:1.7;'>
        Pinnacle is your gateway to innovative solutions and transformative experiences.
        We specialize in delivering excellence across technology, design, and strategy.
        </p>

        <a href="#" style="
            display:inline-block;
            background:#002366;
            color:white;
            padding:12px 28px;
            border-radius:8px;
            text-decoration:none;
            margin-top:20px;
        ">
            Know More →
        </a>

    </div>

    <!-- RIGHT IMAGE -->
    <div style='width:55%; position:relative;'>

        <img src='data:image/webp;base64,{main_img}'
             style='width:100%; height:420px; object-fit:cover; border-radius:12px;' />

        <div style='
            position:absolute;
            bottom:70px;
            left:40px;
            background:white;
            padding:15px 25px;
            border-radius:10px;
            display:flex;
            gap:20px;
            box-shadow:0 6px 15px rgba(0,0,0,0.2);
        '>

            <img src='data:image/webp;base64,{iso1}' style='height:60px;'>
            <img src='data:image/webp;base64,{iso2}' style='height:60px;'>
            <img src='data:image/webp;base64,{iso3}' style='height:60px;'>

        </div>

    </div>

</div>
"""

components.html(html, height=520)






























# ================= MOVING IMAGE BAR =================


# ✅ MOVING IMAGE BAR (PUT HERE)
components.html("""
<div style="
    width:100%;
    height:140px;
    background:#e0e0e0;
    border-radius:12px;
    margin:60px 0;
    display:flex;
    align-items:center;
    overflow:hidden;
">

    <div style="
        display:flex;
        align-items:center;
        gap:50px;
        animation: scroll 25s linear infinite;
    ">

        <!-- IMAGES -->
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774440686/ahk_u5d2h6.webp" style="height:60px; transform: translateY(-5px);">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441251/npca_vypoo6.webp" style="height:60px; transform: translateY(-5px);">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441161/buildingsmart_d7yder.webp" style="height:60px; transform: translateY(-5px);">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441027/building_mqyiow.webp" style="height:60px; transform: translateY(-5px);">
        <img src="YOUR_5TH_IMAGE_URL" style="height:60px; transform: translateY(-5px);">

        <!-- repeat -->
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774440686/ahk_u5d2h6.webp" style="height:60px; transform: translateY(-5px);">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441251/npca_vypoo6.webp" style="height:60px; transform: translateY(-5px);">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441161/buildingsmart_d7yder.webp" style="height:60px; transform: translateY(-5px);">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441027/building_mqyiow.webp" style="height:60px; transform: translateY(-5px);">
        <img src="YOUR_5TH_IMAGE_URL" style="height:60px; transform: translateY(-5px);">

    </div>

</div>

<style>
@keyframes scroll {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}
</style>
""", height=160)




















