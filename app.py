import streamlit as st
import urllib.parse

st.set_page_config(page_title="KrishiSutra Desk", page_icon="🌾", layout="centered")

st.title("🌾 KrishiSutra: Farmer Advisory & Diagnostics Desk")
st.write("Log your current crop issue to get immediate digital insights and generate a shareable advice report.")

# --- STEP 1: FARMER DETAILS & PROBLEM INTAKE ---
st.header("📋 1. Farm Case Registration")

# Using columns to organize the form neatly without complex CSS
col1, col2 = st.columns(2)

with col1:
    farmer_name = st.text_input("Farmer Name", placeholder="e.g., Ramesh Kumar")
    crop_type = st.selectbox("Current Crop", ["Rice", "Mango", "Cashew", "Finger Millet (Nachni)", "Other"])
    soil_type = st.selectbox("Soil Type", ["Laterite/Sandy", "Alluvial/Clayey", "Red Soil"])

with col2:
    location = st.text_input("Village / Region", placeholder="e.g., Chiplun, Ratnagiri")
    crop_age = st.text_input("Crop Age (Weeks/Months)", placeholder="e.g., 4 weeks")
    symptom_type = st.multiselect("Visible Symptoms", ["Yellow Leaves", "Wilting/Drying", "White Patches", "Holes/Pest Bites", "Stunted Growth"])

# Open-ended problem description
problem_description = st.text_area("Describe the problem in detail (Optional)", 
                                    placeholder="Describe changes in weather, water logging, or specific pest behaviors seen...")

st.markdown("---")

# --- STEP 2: GENERATE ADVICE & SHARING OPTIONS ---
if st.button("🚀 Submit Case & Generate Advisory Report"):
    
    if not farmer_name or not location:
        st.error("Please enter at least the Farmer Name and Location to generate the report.")
    else:
        st.header("💡 2. KrishiSutra Diagnostic Advisory")
        
        # Part A: Algorithmic Quick Advice (Based on basic conditional logic)
        st.subheader("🤖 Initial System Suggestions")
        
        advice_found = False
        if "Yellow Leaves" in symptom_type or "Wilting/Drying" in symptom_type:
            if crop_type == "Rice":
                st.warning("⚠️ **Potential Issue:** Nitrogen deficiency or Bacterial Blight.")
                st.info("📌 **Action Plan:** Ensure fields are drained adequately. Avoid over-applying nitrogen fertilizers until soil dries.")
                system_advice = "Potential Nitrogen deficiency/Bacterial Blight. Action: Drain field, optimize fertilizer."
                advice_found = True
        
        if not advice_found:
            st.info("📌 **General Recommendation:** Maintain steady irrigation schedules and isolate heavily infected plants to protect adjacent patches.")
            system_advice = "General maintenance advised. Isolate infected crops, monitor irrigation."

        # Part B: Compile the final text report block
        report_text = (
            f"🌾 *KRISHISUTRA ADVISORY REPORT*\n"
            f"👤 *Farmer:* {farmer_name} ({location})\n"
            f"🌱 *Crop:* {crop_type} ({crop_age})\n"
            f"🧪 *Soil:* {soil_type}\n"
            f"🔍 *Symptoms:* {', '.join(symptom_type) if symptom_type else 'None selected'}\n"
            f"📝 *Details:* {problem_description if problem_description else 'None provided'}\n"
            f"💡 *System Suggestion:* {system_advice}"
        )
        
        # Display the compiled report beautifully to the user
        st.subheader("📄 Generated Case File Summary")
        st.text_area("Copyable Summary text:", report_text, height=200)
        
        # Part C: The Sharing Engine
        st.subheader("📲 Share This Report For Expert Solutions")
        
        # Creating a dynamic WhatsApp URL link
        # It takes our text report and converts spaces/symbols into a valid web link format
        encoded_report = urllib.parse.quote(report_text)
        whatsapp_url = f"https://wa.me/?text={encoded_report}"
        
        col_share1, col_share2 = st.columns(2)
        with col_share1:
            # Styled action link that opens WhatsApp directly with the pre-filled message
            st.markdown(f'''
                <a href="{whatsapp_url}" target="_blank">
                    <button style="
                        width:100%; 
                        background-color:#25D366; 
                        color:white; 
                        border:none; 
                        padding:10px; 
                        border-radius:5px; 
                        font-weight:bold; 
                        cursor:pointer;">
                        💬 Share via WhatsApp
                    </button>
                </a>
            ''', unsafe_allow_html=True)
            
        with col_share2:
            # Allows downloading the exact case layout as a plain text file (.txt)
            st.download_button(
                label="📥 Download Report File",
                data=report_text,
                file_name=f"KrishiSutra_{farmer_name.replace(' ', '_')}.txt",
                mime="text/plain"
            )
