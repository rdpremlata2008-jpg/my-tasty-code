import streamlit as st
import pychromecast
import os

# Get devices
def get_devices():

    casts, browser = pychromecast.get_chromecasts()

    return casts


# Open Windows Cast Menu
def mirror_display():

    os.system("start ms-settings-connectabledevices:devicediscovery")


# UI
st.title("Smart Casting Dashboard")

# Mirror button
if st.button("Mirror Display"):

    mirror_display()

    st.success("Opening Windows Cast Menu...")


# Scan devices
if st.button("Scan Devices"):

    casts = get_devices()

    if len(casts) == 0:

        st.error("No devices found")

    else:

        st.success(f"{len(casts)} Device(s) Found")

        for cast in casts:

            st.write("📺", cast.name)
