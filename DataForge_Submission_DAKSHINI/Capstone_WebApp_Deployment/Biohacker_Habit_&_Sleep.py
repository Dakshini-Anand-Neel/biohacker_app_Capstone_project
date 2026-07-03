import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import scipy.stats as stats
from datetime import datetime, timedelta
import io
from fpdf import FPDF
import base64
# --- Page Config & Theming ---
st.set_page_config(
    page_title="Clinical Biohacker Dashboard",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# Custom CSS for Premium Clinical-Tech Aesthetic
st.markdown("""
<style>
    :root {
        --bg-color: #f8fafc;
        --panel-bg: #ffffff;
        --accent-blue: #0ea5e9;
        --accent-green: #10b981;
        --accent-red: #ef4444;
        --text-main: #0f172a;
        --text-muted: #64748b;
    }
    
    .stApp {
        background-color: var(--bg-color);
        color: var(--text-main);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Override dark mode default if Streamlit is in dark mode, force light/clinical theme for CSS targets */
    .css-1d391kg, .css-18e3th9 {
        background-color: var(--panel-bg);
    }
    
    h1, h2, h3, h4, h5 {
        color: var(--text-main) !important;
        font-weight: 600;
        letter-spacing: -0.5px;
    }
    
    .stMetric {
        background-color: white;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    .stMetric > div > div > div {
        color: var(--accent-blue) !important;
        font-weight: bold;
    }
    
    hr {
        border-color: #e2e8f0;
    }
    
    .stButton>button {
        background-color: var(--accent-blue);
        color: white;
        border: none;
        border-radius: 6px;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #0284c7;
        color: white;
        box-shadow: 0 4px 6px rgba(14, 165, 233, 0.2);
    }
</style>
""", unsafe_allow_html=True)
# --- Helper Functions ---
@st.cache_data
def generate_mock_data():
    np.random.seed(42)
    dates = [datetime.today() - timedelta(days=x) for x in range(30)]
    
    steps = np.random.normal(7000, 3000, 30).astype(int)
    caffeine = np.random.normal(250, 150, 30).clip(0, 800).astype(int)
    screen_time = np.random.normal(5, 2, 30).clip(0, 14)
    
    deep_sleep = np.clip(3 - (caffeine / 250) - (screen_time / 15) + np.random.normal(0, 0.5, 30), 0, 4)
    readiness = np.clip(50 + (steps / 500) + (deep_sleep * 10) - (caffeine / 15) - (screen_time * 2) + np.random.normal(0, 5, 30), 0, 100).astype(int)
    
    df = pd.DataFrame({
        'Date': dates,
        'Caffeine_mg': caffeine,
        'Screen_Time_Hours': screen_time,
        'Steps': steps,
        'Deep_Sleep_Hours': deep_sleep,
        'Daily_Readiness_Score': readiness
    })
    
    df.loc[3, 'Caffeine_mg'] = np.nan
    df.loc[12, 'Deep_Sleep_Hours'] = np.nan
    df.loc[25, 'Steps'] = 50000 
    
    return df.sort_values('Date').reset_index(drop=True)
@st.cache_data
def clean_data(df):
    df_clean = df.copy()
    if 'Date' in df_clean.columns:
        df_clean.dropna(subset=['Date'], inplace=True)
        df_clean['Date'] = pd.to_datetime(df_clean['Date'])
    
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df_clean[col].isnull().any():
            df_clean[col] = df_clean[col].fillna(df_clean[col].median())
    
    if 'Caffeine_mg' in df_clean.columns: df_clean['Caffeine_mg'] = df_clean['Caffeine_mg'].astype(int)
    if 'Steps' in df_clean.columns: df_clean['Steps'] = df_clean['Steps'].astype(int)
    if 'Daily_Readiness_Score' in df_clean.columns: df_clean['Daily_Readiness_Score'] = df_clean['Daily_Readiness_Score'].astype(int)
    
    outlier_flags = {}
    for col in numeric_cols:
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = (df_clean[col] < lower_bound) | (df_clean[col] > upper_bound)
        if outliers.any():
            outlier_flags[col] = df_clean[outliers].index.tolist()
            
    return df_clean, outlier_flags
@st.cache_data
def calculate_circadian_alignment(df):
    """
    Calculates a proxy score (0-100) for how consistent the user's habits are.
    High variance in sleep and activity usually correlates with poor circadian alignment.
    """
    if len(df) < 5:
        return 0
    cv_sleep = df['Deep_Sleep_Hours'].std() / df['Deep_Sleep_Hours'].mean() if df['Deep_Sleep_Hours'].mean() > 0 else 1
    cv_steps = df['Steps'].std() / df['Steps'].mean() if df['Steps'].mean() > 0 else 1
    
    # Lower Coefficient of Variation (CV) means higher consistency
    alignment = 100 - (cv_sleep * 50) - (cv_steps * 50)
    return np.clip(alignment, 0, 100)
def generate_pdf_report(df, circadian_score, notes):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Clinical Biohacker Summary Report", ln=True, align='C')
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt=f"Generated on: {datetime.now().strftime('%Y-%m-%d')}", ln=True, align='C')
    pdf.ln(10)
    
    if notes:
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(200, 10, txt="Patient Notes:", ln=True)
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 10, txt=notes)
        pdf.ln(5)
        
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Telemetry Averages:", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt=f"- Days Tracked: {len(df)}", ln=True)
    pdf.cell(200, 10, txt=f"- Daily Readiness Score: {df['Daily_Readiness_Score'].mean():.1f}/100", ln=True)
    pdf.cell(200, 10, txt=f"- Deep Sleep: {df['Deep_Sleep_Hours'].mean():.1f} hours", ln=True)
    pdf.cell(200, 10, txt=f"- Caffeine: {df['Caffeine_mg'].mean():.0f} mg", ln=True)
    pdf.cell(200, 10, txt=f"- Screen Time: {df['Screen_Time_Hours'].mean():.1f} hours", ln=True)
    pdf.cell(200, 10, txt=f"- Circadian Alignment Score: {circadian_score:.1f}%", ln=True)
    pdf.ln(5)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Clinical Risk Factors (Statistical Significance):", ln=True)
    pdf.set_font("Arial", size=10)
    
    # Calculate stats for report
    corr, p_value = stats.pearsonr(df['Caffeine_mg'], df['Deep_Sleep_Hours'])
    if p_value < 0.05:
        sig = f"Yes (p={p_value:.3f})"
        insight = "High caffeine intake strongly correlates with reduced deep sleep."
    else:
        sig = "No"
        insight = "Caffeine does not show a statistically significant impact on sleep."
        
    pdf.cell(200, 10, txt=f"Caffeine vs. Deep Sleep: Correlation={corr:.2f}, Significant: {sig}", ln=True)
    pdf.multi_cell(0, 10, txt=f"Insight: {insight}")
    
    return pdf.output(dest='S').encode('latin1')

if 'mock_data' not in st.session_state:
    st.session_state['mock_data'] = True
# --- Sidebar ---
st.sidebar.title("⚕️ Clinical Settings")
st.sidebar.markdown("**Provider:** Antigravity Bio-Optics")
st.sidebar.caption("Sample patient data loads automatically. Optional CSV upload is available for testing.")
st.sidebar.markdown("---")
uploaded_file = st.sidebar.file_uploader("Upload Patient CSV", type=['csv'])
if st.sidebar.button("Load Sample Patient File"):
    st.session_state['mock_data'] = True
    
if uploaded_file is not None:
    raw_df = pd.read_csv(uploaded_file)
    st.session_state['mock_data'] = False
else:
    raw_df = generate_mock_data()
    st.session_state['mock_data'] = True
if raw_df is not None:
    df, outliers = clean_data(raw_df)
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("Clinical Filters")
    min_date = df['Date'].min().date()
    max_date = df['Date'].max().date()
    date_range = st.sidebar.date_input("Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)
    if len(date_range) == 2:
        df = df[(df['Date'].dt.date >= date_range[0]) & (df['Date'].dt.date <= date_range[1])]
    
    # --- Main UI ---
    st.title("Clinical-Grade Bio-Optimization Dashboard")
    
    st.info("🎓 **Capstone Project Completed:** I have successfully completed my capstone project, **The Biohacker Habit & Sleep Optimizer**. I built this clinical-grade dashboard to automate health telemetry analysis. I would love to get your feedback on its features, clinical rigor, and user experience! Please explore the tabs below and let me know your thoughts.")
    
    st.markdown("Advanced statistical telemetry analysis for health professionals and serious biohackers.")
    
    # KPIs
    st.subheader("Patient Vitals & System Overview")
    col1, col2, col3, col4 = st.columns(4)
    avg_sleep = df['Deep_Sleep_Hours'].mean()
    avg_readiness = df['Daily_Readiness_Score'].mean()
    circadian_score = calculate_circadian_alignment(df)
    
    col1.metric("Days Analyzed", len(df))
    col2.metric("Avg Readiness (Score)", f"{avg_readiness:.0f}/100")
    col3.metric("Avg Deep Sleep", f"{avg_sleep:.1f} hrs")
    
    # Circadian Score metric styling
    circ_delta = "Optimal" if circadian_score > 80 else ("Warning" if circadian_score < 50 else "Average")
    col4.metric("Circadian Alignment", f"{circadian_score:.1f}%", circ_delta, delta_color="normal" if circadian_score>50 else "inverse")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Clinical EDA", "📈 Diagnostic Charts", "⚡ Peak/Toxic Engine", "🔮 What-If Simulator", "📄 Export Report"])
    
    # --- TAB 1: EDA Dashboard ---
    with tab1:
        st.markdown("### Exploratory Data Analysis")
        with st.expander("1. Raw Data Preview", expanded=True):
            st.dataframe(df.head(5), use_container_width=True)
        with st.expander("2. Descriptive Statistics"):
            st.dataframe(df.describe().T, use_container_width=True)
        with st.expander("3. Outlier Detection (IQR Method)"):
            if not outliers:
                st.success("No significant outliers detected.")
            else:
                st.warning("Outliers detected in the following features:")
                st.json(outliers)
    # --- TAB 2: Diagnostic Charts ---
    with tab2:
        st.markdown("### Medical-Grade Telemetry")
        
        # Temporal Trend
        fig1 = px.line(df, x='Date', y='Daily_Readiness_Score', markers=True, 
                       title="Daily Readiness Timeline",
                       color_discrete_sequence=['#0ea5e9'])
        # Add clinical baseline
        fig1.add_hline(y=80, line_dash="dash", line_color="green", annotation_text="Optimal Readiness Baseline")
        st.plotly_chart(fig1, use_container_width=True)
        
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            # Caffeine vs Sleep with Stats
            corr, p_value = stats.pearsonr(df['Caffeine_mg'], df['Deep_Sleep_Hours'])
            sig_text = "*(Statistically Significant)*" if p_value < 0.05 else "*(Not Significant)*"
            st.markdown(f"#### Caffeine vs. Deep Sleep<br><small>p-value: {p_value:.4f} {sig_text}</small>", unsafe_allow_html=True)
            
            fig2 = px.scatter(df, x='Caffeine_mg', y='Deep_Sleep_Hours', trendline="ols",
                              color='Daily_Readiness_Score', color_continuous_scale="RdYlBu")
            # FDA recommended caffeine limit
            fig2.add_vline(x=400, line_dash="dash", line_color="red", annotation_text="FDA Max (400mg)")
            # Sleep baseline
            fig2.add_hline(y=1.5, line_dash="dash", line_color="green", annotation_text="Min Deep Sleep (1.5h)")
            st.plotly_chart(fig2, use_container_width=True)
                
        with col_c2:
            st.markdown("#### Habit Correlation Heatmap")
            numeric_df = df.select_dtypes(include=[np.number])
            fig_heat = px.imshow(numeric_df.corr(), text_auto=True, aspect="auto", 
                                 color_continuous_scale='RdBu_r')
            st.plotly_chart(fig_heat, use_container_width=True)
    # --- TAB 3: Peak/Toxic Engine ---
    with tab3:
        st.markdown("### Behavioral Extremes Comparison")
        df_sorted = df.sort_values('Daily_Readiness_Score', ascending=False)
        top_3 = df_sorted.head(3)
        bottom_3 = df_sorted.tail(3)
        
        col_v1, col_v2 = st.columns(2)
        with col_v1:
            st.success("Optimal Performance Window (Top 3 Days)")
            st.dataframe(top_3[['Date', 'Daily_Readiness_Score', 'Deep_Sleep_Hours', 'Steps']], hide_index=True)
        with col_v2:
            st.error("Clinical Risk Window (Bottom 3 Days)")
            st.dataframe(bottom_3[['Date', 'Daily_Readiness_Score', 'Deep_Sleep_Hours', 'Steps']], hide_index=True)
            
        st.markdown("#### Behavioral Signature Radar")
        categories = ['Deep_Sleep_Hours', 'Caffeine_mg', 'Screen_Time_Hours', 'Steps']
        max_vals = df[categories].max()
        
        top_avg_norm = (top_3[categories].mean() / max_vals).tolist()
        bottom_avg_norm = (bottom_3[categories].mean() / max_vals).tolist()
        
        top_avg_norm += top_avg_norm[:1]
        bottom_avg_norm += bottom_avg_norm[:1]
        cat_loop = categories + [categories[0]]
        
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(r=top_avg_norm, theta=cat_loop, fill='toself', name='Peak Days', line_color='#10b981'))
        fig_radar.add_trace(go.Scatterpolar(r=bottom_avg_norm, theta=cat_loop, fill='toself', name='Toxic Days', line_color='#ef4444'))
        fig_radar.update_layout(polar=dict(radialaxis=dict(visible=False, range=[0, 1])))
        st.plotly_chart(fig_radar, use_container_width=True)
    # --- TAB 4: What-If Simulator ---
    with tab4:
        st.markdown("### Predictive Clinical ML Simulator")
        st.markdown("Adjust the theoretical inputs below to model potential clinical outcomes using Linear Regression.")
        features = ['Caffeine_mg', 'Screen_Time_Hours', 'Steps']
        if all(f in df.columns for f in features) and len(df) > 5:
            X = df[features]
            model_readiness = LinearRegression().fit(X, df['Daily_Readiness_Score'])
            model_sleep = LinearRegression().fit(X, df['Deep_Sleep_Hours'])
            
            col_s1, col_s2 = st.columns([1, 2])
            with col_s1:
                sim_caffeine = st.slider("Caffeine (mg)", 0, 800, int(df['Caffeine_mg'].mean()))
                sim_screen = st.slider("Screen Time (hrs)", 0.0, 16.0, float(df['Screen_Time_Hours'].mean()))
                sim_steps = st.slider("Steps", 0, 30000, int(df['Steps'].mean()))
                
            with col_s2:
                pred_input = pd.DataFrame([[sim_caffeine, sim_screen, sim_steps]], columns=features)
                pred_r = np.clip(model_readiness.predict(pred_input)[0], 0, 100)
                pred_s = np.clip(model_sleep.predict(pred_input)[0], 0, 24)
                
                pcol1, pcol2 = st.columns(2)
                pcol1.metric("Predicted Readiness", f"{pred_r:.0f}/100")
                pcol2.metric("Predicted Deep Sleep", f"{pred_s:.1f} hrs")
                
    # --- TAB 5: PDF Export ---
    with tab5:
        st.markdown("### Generate Clinical Report for Physician")
        st.markdown("Create a 1-page PDF summary of this telemetry data to hand directly to your doctor or sleep specialist.")
        
        doctor_notes = st.text_area("Notes / Symptoms for your Doctor (Optional):", height=100)
        
        if st.button("Generate Clinical PDF Report"):
            pdf_bytes = generate_pdf_report(df, circadian_score, doctor_notes)
            st.success("Report generated successfully!")
            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_bytes,
                file_name=f"clinical_bio_report_{datetime.now().strftime('%Y%m%d')}.pdf",
                mime="application/pdf"
            )
else:
    st.title("Clinical-Grade Bio-Optimization Dashboard")
    st.info("👈 Upload your Patient CSV or load the Sample Data from the sidebar to begin analysis.")
