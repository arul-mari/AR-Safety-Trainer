import streamlit as st
import uuid

st.set_page_config(
    page_title="AR Safety Trainer",
    page_icon="🦺",
    layout="wide"
)

# ---------------- SESSION ----------------

if "page" not in st.session_state:
    st.session_state.page = "home"

if "score" not in st.session_state:
    st.session_state.score = 0

if "attempt_id" not in st.session_state:
    st.session_state.attempt_id = "AST-" + str(uuid.uuid4())[:5].upper()


def go(page):
    st.session_state.page = page
    st.rerun()


# ---------------- COMMON HEADER ----------------

st.title("🦺 AR SAFETY TRAINER")
st.caption("Smart India Hackathon 2026 • Industrial Safety Training Simulator")

st.divider()


# ==================================================
# HOME
# ==================================================

if st.session_state.page == "home":

    st.header("Industrial Safety Training Simulator")

    st.write(
        "Interactive AR-based safety training for mining "
        "and manufacturing workers."
    )

    st.write(
        "Practice emergency procedures before facing "
        "them in real-world situations."
    )

    st.info(
        "📱 Android 10+   |   🥽 No external headset   |   "
        "💾 Offline-first training"
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("📱 AR Practice")
        st.write(
            "Workers can practice safety scenarios "
            "using an interactive AR environment."
        )

    with col2:
        st.subheader("📝 Assessment")
        st.write(
            "Scenario-based questions test whether "
            "the worker understood the procedure."
        )

    with col3:
        st.subheader("💾 Offline First")
        st.write(
            "Training attempts can be stored locally "
            "and synchronized later."
        )

    st.write("")

    if st.button(
        "🚀 START TRAINING",
        use_container_width=True
    ):
        go("modules")


# ==================================================
# MODULE SELECTION
# ==================================================

elif st.session_state.page == "modules":

    st.header("Select Training Module")

    st.write(
        "Choose a safety scenario to begin your training."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🔥 Fire & Explosion Response")

        st.write(
            "Identify hazards, locate a safe exit, "
            "select the correct emergency action "
            "and follow evacuation procedures."
        )

        st.success("AVAILABLE • PROTOTYPE")

        if st.button(
            "START FIRE MODULE →",
            use_container_width=True
        ):
            go("ar")

    with col2:

        st.subheader("🛡️ Gas Leak & Confined Space")

        st.write(
            "Recognize hazard zones, select PPE "
            "and practice buddy-system procedures."
        )

        st.info("NEXT MODULE")

    st.divider()

    if st.button("← BACK"):
        go("home")


# ==================================================
# AR SIMULATION
# ==================================================

elif st.session_state.page == "ar":

    st.header("🔥 Fire & Explosion Response")

    st.info("AR SIMULATION PREVIEW")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Scenario 01")

        st.write(
            "A fire has been detected in the work area."
        )

        st.write("Your task:")

        st.write(
            "1. Identify the safe exit\n"
            "2. Select the correct emergency action\n"
            "3. Follow the evacuation sequence"
        )

    with col2:

        st.subheader("AR Environment")

        st.write("🔥 Fire Hazard")

        st.write("🚪 Emergency Exit")

        st.write("🧯 Fire Extinguisher")

        st.write("📱 Phone Camera / AR View")

    st.warning(
        "Prototype: the real camera-based AR layer "
        "will be implemented using Unity + AR Foundation + ARCore."
    )

    st.divider()

    if st.button(
        "📝 START ASSESSMENT",
        use_container_width=True
    ):
        go("assessment")

    if st.button("← BACK"):
        go("modules")


# ==================================================
# ASSESSMENT
# ==================================================

elif st.session_state.page == "assessment":

    st.header("📝 Safety Assessment")

    st.write("Question 1 / 1")

    st.subheader(
        "What should you do first when a fire is detected?"
    )

    answer = st.radio(
        "Choose your answer:",
        [
            "A — Ignore the alarm",
            "B — Move toward the hazard",
            "C — Follow the emergency exit",
            "D — Wait for someone else"
        ]
    )

    st.divider()

    if st.button(
        "SUBMIT ANSWER",
        use_container_width=True
    ):

        if answer.startswith("C"):
            st.session_state.score = 100
        else:
            st.session_state.score = 0

        go("result")


# ==================================================
# RESULT
# ==================================================

elif st.session_state.page == "result":

    st.header("🎯 Training Result")

    score = st.session_state.score

    st.metric(
        "Assessment Score",
        f"{score}%"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**MODULE**")
        st.write("Fire & Explosion")

    with col2:
        st.write("**ATTEMPT ID**")
        st.write(st.session_state.attempt_id)

    with col3:

        st.write("**STATUS**")

        if score >= 70:
            st.success("PASSED")
        else:
            st.error("RETRY")

    st.divider()

    if score >= 70:

        st.success(
            "✓ Emergency response identified correctly. "
            "Training attempt recorded."
        )

        if st.button(
            "📄 VIEW COMPLETION RECORD",
            use_container_width=True
        ):
            go("record")

    else:

        st.warning(
            "Review the emergency procedure and try again."
        )

        if st.button(
            "🔄 TRY AGAIN",
            use_container_width=True
        ):
            go("assessment")

    if st.button("← BACK TO MODULES"):
        go("modules")


# ==================================================
# TRAINING RECORD
# ==================================================

elif st.session_state.page == "record":

    st.header("📄 Training Completion Record")

    st.success("✓ TRAINING COMPLETED")

    st.divider()

    st.write("### Training Details")

    st.write(
        "**Module:** Fire & Explosion Response"
    )

    st.write(
        "**Attempt ID:** " +
        st.session_state.attempt_id
    )

    st.write(
        "**Score:** " +
        str(st.session_state.score) +
        "%"
    )

    st.write("**Status:** PASSED")

    st.divider()

    st.subheader("🔐 QR Verification")

    st.info(
        "QR verification will be connected to the "
        "backend certificate system in the full version."
    )

    st.code(
        "VERIFY-" + st.session_state.attempt_id
    )

    st.divider()

    if st.button(
        "🏠 START NEW TRAINING",
        use_container_width=True
    ):
        st.session_state.score = 0
        go("home")