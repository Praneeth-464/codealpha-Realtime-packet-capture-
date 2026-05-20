# utils/capture_state.py

# -----------------------------------------
# GLOBAL CAPTURE STATE
# -----------------------------------------

capture_running = False


# -----------------------------------------
# START CAPTURE
# -----------------------------------------
def start_capture():

    global capture_running

    capture_running = True


# -----------------------------------------
# STOP CAPTURE
# -----------------------------------------
def stop_capture():

    global capture_running

    capture_running = False


# -----------------------------------------
# CHECK STATE
# -----------------------------------------
def is_capturing():

    return capture_running