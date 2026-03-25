import streamlit as st
import sqlite3
import os
import streamlit.components.v1 as components

st.set_page_config(page_title="MY WEBSITE", layout="wide")

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
st.markdown("""
<style>
.navbar {
    display:flex;
    justify-content:space-between;
    align-items:center;
    background:#f8f8f8;
    padding:12px 40px;
}
.navbar-left span {
    margin-right:25px;
    font-weight:600;
}
.navbar-right button {
    margin-left:10px;
    padding:8px 18px;
    border-radius:5px;
    border:none;
}
.login-btn {
    background:white;
    border:1px solid #ccc;
}
.contact-btn {
    background:#ffb900;
    color:white;
}
</style>

<div class="navbar">
    <div class="navbar-left">
        <span>Home</span>
        <span>About Us</span>
        <span>Career</span>
        <span>Resources</span>
        <span>Blog</span>
    </div>
    <div class="navbar-right">
        <button class="login-btn">Login</button>
        <button class="contact-btn">Get in Touch</button>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ================= CONTENT =================
st.title("Constructing Certinity with BIM Technology")

import streamlit as st
import streamlit.components.v1 as components


video_url = "https://res.cloudinary.com/dnodncslz/video/upload/v1774435343/pinnacle-infotech-latest_h3qbk3.mp4"

components.html(f"""
<div style="width:100%;">

    <video autoplay muted loop playsinline 
        style="width:100%; height:auto; border-radius:12px;" 
        controls>
        <source src="{video_url}" type="video/mp4">
        Your browser does not support the video tag.
    </video>

</div>
""", height=520)





st.markdown("## Discover Pinnacle")

st.write("""
Pinnacle is your gateway to innovative solutions and transformative experiences.
We specialize in delivering excellence across technology, design, and strategy.
""")

st.markdown("""
<a href="#" style="
display:inline-block;
background:#002366;
color:white;
padding:12px 25px;
border-radius:8px;
text-decoration:none;
margin-top:20px;
">
Know More →
</a>
""", unsafe_allow_html=True)

# ================= IMAGE SECTION =================
# ================= IMAGE SECTION =================
# ================= IMAGE SECTION =================
# ================= IMAGE SECTION =================
import base64

def to_base64(img):
    return base64.b64encode(img).decode()

images = get_images()

st.write("Images loaded:", len(images))  # keep this for debug

if len(images) >= 4:
    main_img = to_base64(images[0][0])
    iso1 = to_base64(images[1][0])
    iso2 = to_base64(images[2][0])
    iso3 = to_base64(images[3][0])

html = f"""
<div style='position:relative; width:100%; margin-top:40px;'>

    <img src='data:image/webp;base64,{main_img}'
         style='width:100%; height:420px; object-fit:cover; border-radius:12px;' />

    <div style='
        position:absolute;
        bottom:80px;
        left:30px;
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
"""

components.html(html, height=500)   




















