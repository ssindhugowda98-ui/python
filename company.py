[12:05 pm, 04/06/2026] Soniya VVET: # =========================================
# Company Management App
# company_app.py
# =========================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from datetime import date, datetime
import random

# -----------------------------------------
# Page Config
# -----------------------------------------

st.set_page_config(
    page_title="NexaCorp | Company Portal",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------
# Custom CSS
# -----------------------------------------

st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background: #0f172a;…
[12:09 pm, 04/06/2026] Soniya VVET: # =========================================
# Company Management App
# company_app.py
# =========================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from datetime import date, datetime
import random

# -----------------------------------------
# Page Config
# -----------------------------------------

st.set_page_config(
    page_title="NexaCorp | Company Portal",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------
# Custom CSS
# -----------------------------------------

st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background: #0f172a;
    }
    [data-testid="stSidebar"] * {
        color: #e2e8f0 !important;
    }
    .metric-card {
        background: linear-gradient(135deg, #1e293b, #0f172a);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        color: white;
        margin-bottom: 0.5rem;
    }
    .metric-card h3 {
        font-size: 0.78rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin: 0 0 0.4rem 0;
    }
    .metric-card p {
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
        color: #f1f5f9;
    }
    .metric-card span {
        font-size: 0.8rem;
        color: #4ade80;
    }
    .metric-card span.down {
        color: #f87171;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.2rem;
    }
    .section-sub {
        color: #64748b;
        margin-bottom: 1.5rem;
        font-size: 0.95rem;
    }
    .badge-active {
        background: #dcfce7; color: #16a34a;
        padding: 2px 10px; border-radius: 99px;
        font-size: 0.75rem; font-weight: 600;
    }
    .badge-inactive {
        background: #fee2e2; color: #dc2626;
        padding: 2px 10px; border-radius: 99px;
        font-size: 0.75rem; font-weight: 600;
    }
    .badge-dept {
        background: #eff6ff; color: #2563eb;
        padding: 2px 10px; border-radius: 99px;
        font-size: 0.75rem; font-weight: 500;
    }
    div[data-testid="stForm"] {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------
# Sample Data
# -----------------------------------------

@st.cache_data
def get_employees():
    return pd.DataFrame([
        {"ID": "E001", "Name": "Arjun Mehta",      "Department": "Engineering",  "Role": "Senior Engineer",     "Salary": 95000,  "Status": "Active",   "Joined": "2020-03-15", "City": "Bengaluru"},
        {"ID": "E002", "Name": "Priya Sharma",     "Department": "Marketing",    "Role": "Marketing Lead",      "Salary": 72000,  "Status": "Active",   "Joined": "2019-07-01", "City": "Mumbai"},
        {"ID": "E003", "Name": "Rahul Verma",      "Department": "Sales",        "Role": "Sales Manager",       "Salary": 80000,  "Status": "Active",   "Joined": "2021-01-10", "City": "Delhi"},
        {"ID": "E004", "Name": "Sneha Iyer",       "Department": "HR",           "Role": "HR Manager",          "Salary": 68000,  "Status": "Active",   "Joined": "2018-09-20", "City": "Chennai"},
        {"ID": "E005", "Name": "Kiran Nair",       "Department": "Engineering",  "Role": "Frontend Developer",  "Salary": 78000,  "Status": "Active",   "Joined": "2022-04-05", "City": "Hyderabad"},
        {"ID": "E006", "Name": "Amit Patel",       "Department": "Finance",      "Role": "Finance Analyst",     "Salary": 82000,  "Status": "Inactive", "Joined": "2017-11-30", "City": "Ahmedabad"},
        {"ID": "E007", "Name": "Divya Reddy",      "Department": "Engineering",  "Role": "Backend Developer",   "Salary": 88000,  "Status": "Active",   "Joined": "2021-08-22", "City": "Pune"},
        {"ID": "E008", "Name": "Vijay Kumar",      "Department": "Sales",        "Role": "Sales Executive",     "Salary": 55000,  "Status": "Active",   "Joined": "2023-01-15", "City": "Kolkata"},
        {"ID": "E009", "Name": "Meera Joshi",      "Department": "Marketing",    "Role": "Content Strategist",  "Salary": 60000,  "Status": "Active",   "Joined": "2022-09-01", "City": "Jaipur"},
        {"ID": "E010", "Name": "Suresh Babu",      "Department": "Finance",      "Role": "CFO",                 "Salary": 150000, "Status": "Active",   "Joined": "2015-06-01", "City": "Bengaluru"},
        {"ID": "E011", "Name": "Ananya Singh",     "Department": "HR",           "Role": "Recruiter",           "Salary": 52000,  "Status": "Active",   "Joined": "2023-03-20", "City": "Mumbai"},
        {"ID": "E012", "Name": "Rohan Gupta",      "Department": "Engineering",  "Role": "DevOps Engineer",     "Salary": 92000,  "Status": "Inactive", "Joined": "2019-12-10", "City": "Delhi"},
        {"ID": "E013", "Name": "Lakshmi Priya",    "Department": "Marketing",    "Role": "SEO Specialist",      "Salary": 58000,  "Status": "Active",   "Joined": "2022-06-15", "City": "Bengaluru"},
        {"ID": "E014", "Name": "Nikhil Desai",     "Department": "Sales",        "Role": "Regional Head",       "Salary": 105000, "Status": "Active",   "Joined": "2016-03-01", "City": "Pune"},
        {"ID": "E015", "Name": "Kavitha Nair",     "Department": "Engineering",  "Role": "QA Engineer",         "Salary": 70000,  "Status": "Active",   "Joined": "2021-11-05", "City": "Kochi"},
    ])

@st.cache_data
def get_financials():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    np.random.seed(42)
    revenue    = [1.8, 2.1, 2.4, 2.0, 2.7, 3.1, 2.9, 3.4, 3.2, 3.8, 4.1, 4.5]
    expenses   = [1.2, 1.3, 1.5, 1.4, 1.6, 1.8, 1.7, 1.9, 1.8, 2.1, 2.2, 2.4]
    profit     = [r - e for r, e in zip(revenue, expenses)]
    return pd.DataFrame({"Month": months, "Revenue (₹M)": revenue,
                         "Expenses (₹M)": expenses, "Profit (₹M)": profit})

@st.cache_data
def get_sales():
    quarters = ["Q1 2023", "Q2 2023", "Q3 2023", "Q4 2023",
                "Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"]
    targets  = [50, 55, 60, 70, 65, 75, 80, 90]
    achieved = [47, 58, 55, 72, 68, 71, 85, 88]
    return pd.DataFrame({"Quarter": quarters, "Target (₹M)": targets, "Achieved (₹M)": achieved})

# -----------------------------------------
# Sidebar Navigation
# -----------------------------------------

with st.sidebar:
    st.markdown("## 🏢 NexaCorp")
    st.markdown("---")
    page = st.radio(
        "Navigation",
        ["🏠  Company Overview", "📊  Dashboard", "👥  Employees", "💰  Financials", "📈  Sales"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.markdown("*Quick Stats*")
    df_emp = get_employees()
    st.markdown(f"👤 Total Staff: *{len(df_emp)}*")
    st.markdown(f"✅ Active: *{len(df_emp[df_emp['Status']=='Active'])}*")
    st.markdown(f"🏙️ Cities: *{df_emp['City'].nunique()}*")
    st.markdown("---")
    st.caption("NexaCorp Portal v2.0 · 2024")

# ==========================================
# PAGE 1: COMPANY OVERVIEW
# ==========================================

if page == "🏠  Company Overview":
    st.markdown('<div class="section-header">🏢 Welcome to NexaCorp</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Building the future, one innovation at a time.</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        st.markdown("""
        ### About Us
        NexaCorp is a technology-driven company founded in 2015, headquartered in Bengaluru, India.
        We specialize in enterprise software, cloud infrastructure, and data analytics solutions
        for Fortune 500 companies across Asia and beyond.

        Our mission is to empower businesses with intelligent tools that drive growth,
        efficiency, and lasting impact.
        """)

        st.markdown("### 🎯 Core Values")
        c1, c2, c3 = st.columns(3)
        c1.success("*Innovation First*\nWe challenge the status quo every day.")
        c2.info("*People Driven*\nOur team is our greatest asset.")
        c3.warning("*Customer Obsessed*\nEvery decision starts with the customer.")

    with col2:
        st.markdown("### 📍 Locations")
        for city in ["Bengaluru (HQ)", "Mumbai", "Delhi", "Hyderabad", "Pune", "Chennai"]:
            st.markdown(f"- {city}")

    with col3:
        st.markdown("### 🏆 Awards")
        st.markdown("""
        - 🥇 Best Tech Startup 2022
        - 🌟 Great Place to Work 2023
        - 💡 Innovation Award 2024
        - 📊 Top Analytics Firm 2023
        """)

    st.markdown("---")
    st.markdown("### 🧭 Leadership Team")

    leaders = [
        {"name": "Suresh Babu",   "role": "Chief Financial Officer",  "dept": "Finance"},
        {"name": "Sneha Iyer",    "role": "Head of Human Resources",  "dept": "HR"},
        {"name": "Nikhil Desai",  "role": "Regional Sales Head",      "dept": "Sales"},
        {"name": "Arjun Mehta",   "role": "Lead Engineer",            "dept": "Engineering"},
    ]

    cols = st.columns(4)
    for i, leader in enumerate(leaders):
        with cols[i]:
            st.markdown(f"""
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:1rem; text-align:center;">
                <div style="font-size:2.5rem">👤</div>
                <div style="font-weight:700; font-size:0.95rem">{leader['name']}</div>
                <div style="color:#64748b; font-size:0.8rem">{leader['role']}</div>
                <div style="margin-top:0.5rem"><span class="badge-dept">{leader['dept']}</span></div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📬 Contact Us")
    c1, c2, c3 = st.columns(3)
    c1.info("📧 *Email*\nhello@nexacorp.in")
    c2.info("📞 *Phone*\n+91 80 4567 8900")
    c3.info("🌐 *Website*\nwww.nexacorp.in")

# ==========================================
# PAGE 2: DASHBOARD
# ==========================================

elif page == "📊  Dashboard":
    st.markdown('<div class="section-header">📊 Company Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Real-time overview of company performance.</div>', unsafe_allow_html=True)

    df = get_employees()
    fin = get_financials()

    # Top Metrics
    total_emp    = len(df)
    active_emp   = len(df[df['Status'] == 'Active'])
    total_salary = df['Salary'].sum()
    avg_salary   = df['Salary'].mean()
    annual_rev   = sum(fin['Revenue (₹M)'])
    annual_prof  = sum(fin['Profit (₹M)'])

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""<div class="metric-card"><h3>Total Employees</h3><p>{total_emp}</p><span>↑ 3 this month</span></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="metric-card"><h3>Active Staff</h3><p>{active_emp}</p><span>↑ 93% retention</span></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class="metric-card"><h3>Annual Revenue</h3><p>₹{annual_rev:.1f}M</p><span>↑ 18% YoY</span></div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""<div class="metric-card"><h3>Annual Profit</h3><p>₹{annual_prof:.1f}M</p><span>↑ 22% YoY</span></div>""", unsafe_allow_html=True)

    st.markdown("---")

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("#### Headcount by Department")
        dept_count = df['Department'].value_counts()
        fig, ax = plt.subplots(figsize=(6, 4))
        colors = ['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6']
        dept_count.plot(kind='bar', ax=ax, color=colors[:len(dept_count)])
        ax.set_xlabel("")
        ax.set_ylabel("Employees")
        ax.tick_params(axis='x', rotation=30)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    with col_right:
        st.markdown("#### Revenue vs Expenses (2024)")
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        x = range(len(fin))
        ax2.plot(fin['Month'], fin['Revenue (₹M)'], marker='o', color='#3b82f6', label='Revenue', linewidth=2)
        ax2.plot(fin['Month'], fin['Expenses (₹M)'], marker='s', color='#ef4444', label='Expenses', linewidth=2, linestyle='--')
        ax2.fill_between(fin['Month'], fin['Revenue (₹M)'], fin['Expenses (₹M)'], alpha=0.08, color='#3b82f6')
        ax2.legend()
        ax2.set_ylabel("₹ Million")
        ax2.tick_params(axis='x', rotation=45)
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig2)
        plt.close(fig2)

    st.markdown("---")
    col3, col4 = st.columns(2)

    with col3:
        st.markdown("#### Salary Distribution")
        fig3, ax3 = plt.subplots(figsize=(6, 4))
        ax3.hist(df['Salary'], bins=8, color='#8b5cf6', edgecolor='white')
        ax3.set_xlabel("Annual Salary (₹)")
        ax3.set_ylabel("Employees")
        ax3.spines['top'].set_visible(False)
        ax3.spines['right'].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig3)
        plt.close(fig3)

    with col4:
        st.markdown("#### Department Salary Share")
        dept_salary = df.groupby('Department')['Salary'].sum()
        fig4, ax4 = plt.subplots(figsize=(6, 4))
        ax4.pie(dept_salary, labels=dept_salary.index, autopct='%1.1f%%',
                colors=['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6'],
                startangle=90)
        plt.tight_layout()
        st.pyplot(fig4)
        plt.close(fig4)

# ==========================================
# PAGE 3: EMPLOYEES
# ==========================================

elif page == "👥  Employees":
    st.markdown('<div class="section-header">👥 Employee Management</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">View, search, filter and manage your team.</div>', unsafe_allow_html=True)

    df = get_employees()

    # Filters
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        search = st.text_input("🔍 Search by name", "")
    with col2:
        dept_filter = st.selectbox("Department", ["All"] + sorted(df['Department'].unique().tolist()))
    with col3:
        status_filter = st.selectbox("Status", ["All", "Active", "Inactive"])
    with col4:
        city_filter = st.selectbox("City", ["All"] + sorted(df['City'].unique().tolist()))

    filtered = df.copy()
    if search:
        filtered = filtered[filtered['Name'].str.contains(search, case=False)]
    if dept_filter != "All":
        filtered = filtered[filtered['Department'] == dept_filter]
    if status_filter != "All":
        filtered = filtered[filtered['Status'] == status_filter]
    if city_filter != "All":
        filtered = filtered[filtered['City'] == city_filter]

    st.markdown(f"*{len(filtered)} employee(s) found*")
    st.markdown("---")

    # Employee Cards
    for i in range(0, len(filtered), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(filtered):
                emp = filtered.iloc[i + j]
                badge = f'<span class="badge-active">● Active</span>' if emp['Status'] == 'Active' else f'<span class="badge-inactive">● Inactive</span>'
                with col:
                    st.markdown(f"""
                    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:14px; padding:1.2rem; margin-bottom:1rem; box-shadow:0 1px 4px rgba(0,0,0,0.04);">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.8rem;">
                            <div style="font-weight:700; font-size:1rem;">{emp['Name']}</div>
                            {badge}
                        </div>
                        <div style="color:#64748b; font-size:0.82rem; margin-bottom:0.3rem;">🆔 {emp['ID']}</div>
                        <div style="color:#64748b; font-size:0.82rem; margin-bottom:0.3rem;">💼 {emp['Role']}</div>
                        <div style="color:#64748b; font-size:0.82rem; margin-bottom:0.3rem;"><span class="badge-dept">{emp['Department']}</span></div>
                        <div style="color:#64748b; font-size:0.82rem; margin-bottom:0.3rem;">📍 {emp['City']}</div>
                        <div style="color:#0f172a; font-size:0.9rem; font-weight:600; margin-top:0.5rem;">₹{emp['Salary']:,} / yr</div>
                        <div style="color:#94a3b8; font-size:0.75rem;">Joined: {emp['Joined']}</div>
                    </div>
                    """, unsafe_allow_html=True)

    st.markdown("---")

    # Add Employee Form
    with st.expander("➕ Add New Employee"):
        with st.form("add_employee"):
            c1, c2 = st.columns(2)
            with c1:
                new_name = st.text_input("Full Name")
                new_dept = st.selectbox("Department", ["Engineering", "Marketing", "Sales", "HR", "Finance"])
                new_salary = st.number_input("Annual Salary (₹)", min_value=30000, max_value=500000, step=1000, value=60000)
            with c2:
                new_role = st.text_input("Job Role")
                new_city = st.selectbox("City", ["Bengaluru", "Mumbai", "Delhi", "Hyderabad", "Pune", "Chennai", "Kochi", "Kolkata"])
                new_status = st.selectbox("Status", ["Active", "Inactive"])
            submitted = st.form_submit_button("Add Employee")
            if submitted:
                if new_name and new_role:
                    st.success(f"✅ *{new_name}* added as *{new_role}* in *{new_dept}*!")
                    st.balloons()
                else:
                    st.error("Please fill in all required fields.")

    # Raw Table
    with st.expander("📋 View Raw Data Table"):
        st.dataframe(filtered.reset_index(drop=True), use_container_width=True)

# ==========================================
# PAGE 4: FINANCIALS
# ==========================================

elif page == "💰  Financials":
    st.markdown('<div class="section-header">💰 Financial Overview</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Monthly revenue, expenses, and profit analysis for 2024.</div>', unsafe_allow_html=True)

    fin = get_financials()

    total_rev  = fin['Revenue (₹M)'].sum()
    total_exp  = fin['Expenses (₹M)'].sum()
    total_prof = fin['Profit (₹M)'].sum()
    margin     = (total_prof / total_rev) * 100

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""<div class="metric-card"><h3>Total Revenue</h3><p>₹{total_rev:.1f}M</p><span>↑ 18% vs last year</span></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="metric-card"><h3>Total Expenses</h3><p>₹{total_exp:.1f}M</p><span class="down">↑ 12% vs last year</span></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class="metric-card"><h3>Net Profit</h3><p>₹{total_prof:.1f}M</p><span>↑ 22% vs last year</span></div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""<div class="metric-card"><h3>Profit Margin</h3><p>{margin:.1f}%</p><span>↑ Healthy</span></div>""", unsafe_allow_html=True)

    st.markdown("---")

    # Revenue vs Expenses
    st.markdown("#### Monthly Revenue vs Expenses")
    fig1, ax1 = plt.subplots(figsize=(14, 5))
    x = np.arange(len(fin))
    width = 0.35
    ax1.bar(x - width/2, fin['Revenue (₹M)'], width, label='Revenue', color='#3b82f6')
    ax1.bar(x + width/2, fin['Expenses (₹M)'], width, label='Expenses', color='#ef4444')
    ax1.set_xticks(x)
    ax1.set_xticklabels(fin['Month'])
    ax1.set_ylabel("₹ Million")
    ax1.legend()
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)

    # Profit Trend
    st.markdown("#### Monthly Profit Trend")
    fig2, ax2 = plt.subplots(figsize=(14, 4))
    colors = ['#10b981' if p > 0 else '#ef4444' for p in fin['Profit (₹M)']]
    ax2.bar(fin['Month'], fin['Profit (₹M)'], color=colors)
    ax2.axhline(0, color='#64748b', linewidth=0.8, linestyle='--')
    ax2.set_ylabel("₹ Million")
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)

    st.markdown("---")

    # Expense Breakdown (Pie)
    st.markdown("#### Expense Breakdown by Category")
    categories = ["Salaries", "Infrastructure", "Marketing", "Operations", "R&D"]
    values = [45, 20, 15, 12, 8]
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("\n")
        for cat, val in zip(categories, values):
            st.markdown(f"*{cat}* — {val}%")
    with col2:
        fig3, ax3 = plt.subplots(figsize=(5, 4))
        ax3.pie(values, labels=categories, autopct='%1.0f%%',
                colors=['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6'],
                startangle=140)
        plt.tight_layout()
        st.pyplot(fig3)
        plt.close(fig3)

    st.markdown("---")
    st.markdown("#### Raw Financial Data")
    st.dataframe(fin, use_container_width=True)

# ==========================================
# PAGE 5: SALES
# ==========================================

elif page == "📈  Sales":
    st.markdown('<div class="section-header">📈 Sales Performance</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Quarterly targets vs achieved and team performance.</div>', unsafe_allow_html=True)

    sales = get_sales()

    total_target   = sales['Target (₹M)'].sum()
    total_achieved = sales['Achieved (₹M)'].sum()
    achievement_pct = (total_achieved / total_target) * 100

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""<div class="metric-card"><h3>Total Target</h3><p>₹{total_target}M</p><span>2023–2024</span></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="metric-card"><h3>Total Achieved</h3><p>₹{total_achieved}M</p><span>↑ Strong performance</span></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class="metric-card"><h3>Achievement Rate</h3><p>{achievement_pct:.1f}%</p><span>↑ Above target</span></div>""", unsafe_allow_html=True)

    st.markdown("---")

    # Target vs Achieved
    st.markdown("#### Quarterly Target vs Achieved")
    fig1, ax1 = plt.subplots(figsize=(14, 5))
    x = np.arange(len(sales))
    width = 0.35
    bars1 = ax1.bar(x - width/2, sales['Target (₹M)'], width, label='Target', color='#94a3b8')
    bars2 = ax1.bar(x + width/2, sales['Achieved (₹M)'], width, label='Achieved', color='#3b82f6')
    ax1.set_xticks(x)
    ax1.set_xticklabels(sales['Quarter'], rotation=30)
    ax1.set_ylabel("₹ Million")
    ax1.legend()
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    for bar in bars2:
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                 f"₹{bar.get_height()}M", ha='center', va='bottom', fontsize=8, color='#1e40af')
    plt.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)

    st.markdown("---")

    # Salesperson Performance
    st.markdown("#### Sales Team Performance")
    salespeople = {
        "Rahul Verma":   {"Target": 200, "Achieved": 218, "Deals": 34, "Region": "North"},
        "Nikhil Desai":  {"Target": 250, "Achieved": 271, "Deals": 41, "Region": "West"},
        "Vijay Kumar":   {"Target": 120, "Achieved": 109, "Deals": 19, "Region": "East"},
        "Meera Joshi":   {"Target": 150, "Achieved": 162, "Deals": 26, "Region": "South"},
        "Priya Sharma":  {"Target": 180, "Achieved": 175, "Deals": 29, "Region": "Central"},
    }
    sp_df = pd.DataFrame(salespeople).T.reset_index().rename(columns={"index": "Name"})
    sp_df['Achievement %'] = (sp_df['Achieved'] / sp_df['Target'] * 100).round(1)

    for _, row in sp_df.iterrows():
        pct = row['Achievement %']
        color = "#10b981" if pct >= 100 else "#f59e0b" if pct >= 90 else "#ef4444"
        col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 1, 2])
        col1.markdown(f"*{row['Name']}*  \n<small style='color:#64748b'>{row['Region']} Region</small>", unsafe_allow_html=True)
        col2.markdown(f"Target: ₹{row['Target']}M")
        col3.markdown(f"Achieved: ₹{row['Achieved']}M")
        col4.markdown(f"{row['Deals']} deals")
        col5.markdown(f"<span style='color:{color}; font-weight:700'>{pct}%</span>", unsafe_allow_html=True)
        st.progress(min(pct / 100, 1.0))

    st.markdown("---")

    # Regional Breakdown
    st.markdown("#### Regional Sales Distribution")
    regional = {"North": 218, "West": 271, "East": 109, "South": 162, "Central": 175}
    col1, col2 = st.columns(2)

    with col1:
        fig2, ax2 = plt.subplots(figsize=(5, 4))
        ax2.pie(regional.values(), labels=regional.keys(), autopct='%1.1f%%',
                colors=['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6'],
                startangle=140)
        plt.tight_layout()
        st.pyplot(fig2)
        plt.close(fig2)

    with col2:
        fig3, ax3 = plt.subplots(figsize=(5, 4))
        ax3.barh(list(regional.keys()), list(regional.values()), color='#3b82f6')
        ax3.set_xlabel("₹ Million")
        ax3.spines['top'].set_visible(False)
        ax3.spines['right'].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig3)
        plt.close(fig3)

    st.markdown("---")
    st.markdown("#### Raw Sales Data")
    st.dataframe(sales, use_container_width=True)
