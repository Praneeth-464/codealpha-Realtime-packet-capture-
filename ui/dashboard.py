# ui/dashboard.py

import streamlit as st
import threading
import pandas as pd
import time

from capture.interface_manager import (
    get_available_interfaces
)

from capture.sniffer import (
    start_sniffing
)

from utils.packet_storage import (
    get_packets,
    clear_packets
)

from utils.capture_state import (
    start_capture,
    stop_capture
)


# -----------------------------------------
# PAGE CONFIG
# -----------------------------------------
st.set_page_config(
    page_title="Packet Analyzer",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# -----------------------------------------
# CLEAN UI CSS
# -----------------------------------------
st.markdown(
    """
    <style>

    /* MAIN BACKGROUND */
    .stApp {
        background-color: #0f172a;
    }

    /* REMOVE EXTRA SPACE */
    .block-container {
        padding-top: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    /* HEADERS */
    .main-title {
        font-size: 42px;
        font-weight: bold;
        color: white;
        margin-bottom: 5px;
    }

    .sub-title {
        font-size: 16px;
        color: #cbd5e1;
        margin-bottom: 30px;
    }

    /* GENERAL TEXT */
    h1, h2, h3, h4, h5, p, label {
        color: white !important;
    }

    /* BUTTONS */
    .stButton button {
        background-color: #2563eb !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        height: 45px;
        font-size: 15px;
        font-weight: 600;
        box-shadow: none !important;
    }

    .stButton button:hover {
        background-color: #1d4ed8 !important;
    }

    /* SEARCH INPUT */
    .stTextInput input {
        background-color: #1e293b !important;
        color: white !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
    }

    .stTextInput input::placeholder {
        color: #94a3b8 !important;
    }

    /* NUMBER INPUT */
    .stNumberInput input {
        background-color: #1e293b !important;
        color: white !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
    }

    /* SELECT BOX */
    div[data-baseweb="select"] {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
        min-height: 45px !important;
    }

    /* ---------------------------------- */
/* SELECTED INTERFACE TEXT            */
/* ---------------------------------- */

div[data-baseweb="select"] input {

    color: #0f172a !important;

    font-weight: 500 !important;
}


/* Placeholder text */
div[data-baseweb="select"] input::placeholder {

    color: #64748b !important;
}
    /* DROPDOWN ARROW */
    div[data-baseweb="select"] svg {
        fill: white !important;
    }

    /* MULTISELECT TAGS */
    span[data-baseweb="tag"] {
        background-color: #334155 !important;
        color: white !important;
        border-radius: 8px !important;
    }

    /* DROPDOWN MENU */
    div[role="listbox"] {
        background-color: white !important;
    }

    /* DROPDOWN OPTIONS */
    div[role="option"] {
        background-color: white !important;
        color: black !important;
    }

    div[role="option"]:hover {
        background-color: #dbeafe !important;
        color: black !important;
    }

    /* TABLE */
    .stDataFrame {
        border: 1px solid #334155;
        border-radius: 12px;
        overflow: hidden;
    }

    /* STATUS BOX */
    .status-box {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 14px;
        font-size: 16px;
        font-weight: 600;
        color: white;
        margin-bottom: 20px;
    }

    /* REMOVE GLOW */
    * {
        box-shadow: none !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------------------
# HEADER
# -----------------------------------------
st.markdown(
    """
    <div class="main-title">
        Packet Analyzer
    </div>

    <div class="sub-title">
        Realtime Network Traffic Monitor
    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------------------
# SESSION STATE
# -----------------------------------------
if "capture_started" not in st.session_state:
    st.session_state.capture_started = False


# -----------------------------------------
# FETCH INTERFACES
# -----------------------------------------
interfaces = get_available_interfaces()


# -----------------------------------------
# CREATE INTERFACE LIST
# -----------------------------------------
interface_display_list = []
interface_mapping = {}

for interface in interfaces:

    description = interface.get(
        "description",
        "Unknown Interface"
    )

    device_name = interface.get(
        "name",
        "Unknown"
    )

    active = interface.get(
        "active",
        False
    )

    if active:
        display_name = f"🟢 {description}"
    else:
        display_name = f"⚪ {description}"

    interface_display_list.append(
        display_name
    )

    interface_mapping[
        display_name
    ] = device_name


# -----------------------------------------
# DEFAULT ACTIVE INTERFACE
# -----------------------------------------
default_index = 0

for index, interface in enumerate(interfaces):

    if interface.get("active", False):

        default_index = index
        break


# -----------------------------------------
# INTERFACE SECTION
# -----------------------------------------
st.subheader("Network Interface")

selected_interface_display = st.selectbox(
    "Select Active Interface",
    interface_display_list,
    index=default_index
)


# -----------------------------------------
# SAVE INTERFACE
# -----------------------------------------
actual_interface = None

if selected_interface_display:

    actual_interface = interface_mapping.get(
        selected_interface_display
    )


# -----------------------------------------
# CAPTURE FUNCTION
# -----------------------------------------
def capture_packets(interface):

    try:
        start_sniffing(interface)

    except Exception as e:
        print(f"[ERROR] {e}")


# -----------------------------------------
# BUTTONS
# -----------------------------------------
col1, col2 = st.columns(2)


# START BUTTON
with col1:

    if st.button("Start Packet Capture"):

        if not st.session_state.capture_started:

            st.session_state.capture_started = True

            start_capture()

            clear_packets()

            capture_thread = threading.Thread(
                target=capture_packets,
                args=(actual_interface,),
                daemon=True
            )

            capture_thread.start()


# STOP BUTTON
with col2:

    if st.button("Stop Capture"):

        stop_capture()

        st.session_state.capture_started = False


# -----------------------------------------
# STATUS
# -----------------------------------------
if st.session_state.capture_started:

    st.markdown(
        """
        <div class="status-box">
            🟢 Capture Status: ACTIVE
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        """
        <div class="status-box">
            🔴 Capture Status: STOPPED
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------------------
# SEARCH + FILTERS
# -----------------------------------------
col3, col4 = st.columns(2)

with col3:

    search_query = st.text_input(
        "Search IP / Protocol / Port"
    )

with col4:

    protocol_filter = st.multiselect(
        "Filter Protocols",
        [
            "TCP",
            "UDP",
            "DNS",
            "HTTP",
            "HTTPS",
            "ICMP"
        ],
        default=[]
    )


# -----------------------------------------
# LIVE PACKET FLOW
# -----------------------------------------
st.subheader("Live Packet Flow")

packet_table = st.empty()

packets = get_packets()


if len(packets) > 0:

    MAX_DISPLAY_PACKETS = 200

    latest_packets = packets[
        -MAX_DISPLAY_PACKETS:
    ]

    cleaned_packets = []

    for index, packet in enumerate(latest_packets):

        if not isinstance(packet, dict):
            continue

        cleaned_packet = {}

        cleaned_packet["No"] = index + 1

        cleaned_packet["Time"] = time.strftime(
            "%H:%M:%S"
        )

        for key, value in packet.items():

            try:
                cleaned_packet[key] = str(value)

            except:
                cleaned_packet[key] = "ERROR"

        cleaned_packets.append(
            cleaned_packet
        )

    df = pd.DataFrame(
        cleaned_packets
    )

    # SEARCH FILTER
    if search_query:

        df = df[
            df.astype(str)
            .apply(
                lambda row:
                row.str.contains(
                    search_query,
                    case=False
                ).any(),
                axis=1
            )
        ]

    # PROTOCOL FILTER
    if protocol_filter:

        if "protocol" in df.columns:

            df = df[
                df["protocol"]
                .isin(protocol_filter)
            ]

    # COLUMN ORDER
    preferred_columns = [
        "No",
        "Time",
        "src_ip",
        "dst_ip",
        "src_port",
        "dst_port",
        "protocol",
        "payload"
    ]

    existing_columns = [
        col for col in preferred_columns
        if col in df.columns
    ]

    df = df[
        existing_columns
    ]

    # DISPLAY TABLE
    packet_table.dataframe(
        df,
        width="stretch",
        height=520,
        hide_index=True
    )

else:

    st.info(
        "No Packets Captured Yet"
    )


# -----------------------------------------
# PACKET DETAILS
# -----------------------------------------
st.subheader("Packet Details")

packet_number = st.number_input(
    "Enter Packet Number",
    min_value=1,
    step=1
)

if len(packets) > 0:

    if packet_number <= len(packets):

        selected_packet = packets[
            packet_number - 1
        ]

        st.json(selected_packet)


# AUTO REFRESH
if st.session_state.capture_started:

    time.sleep(1)

    packet_table.dataframe(
        
        width="stretch",
        height=520,
        hide_index=True
    )
    st.rerun()