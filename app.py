import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# ဒေတာတန်ဖိုးများ သတ်မှတ်ခြင်း
data = {
    "Region": ["AYA", "YGN", "TNTY", "PGU", "MGY", "SGN", "MDY"],
    "Target": [120, 100, 45, 87, 65, 55, 95],
    "Actual": [100, 85, 43, 40, 30, 55, 55]
}

# DataFrame ပြောင်းလဲခြင်း
df = pd.DataFrame(data)

# Achieved (%) တွက်ချက်ခြင်း
# Actual ÷ Target × 100 နဲ့ ရာခိုင်နှုန်းတွက်ပြီး string အဖြစ်ပြောင်း
# ပြီးတော့ '%' ထည့်ပေးတယ်
df['Achieved (%)'] = (df['Actual'] / df['Target'] * 100).round(1).astype(str) + '%'

# Target အတိုင်း စဉ်ခြင်း (ကြီး မှ ငယ်)
df = df.sort_values(by='Target', ascending=False).reset_index(drop=True)

# Streamlit ထဲမှာ ဒေတာဇယား ပြသခြင်း
st.markdown("#### Target and Actual Table")
st.dataframe(df, width=800, hide_index=True)

# Plot စတင်ခြင်း
fig, ax = plt.subplots(figsize=(10, 6))

# bar height ကို သတ်မှတ်
bar_height = 0.4
y = range(len(df))

# Target Bar (နောက်ခံ bar)
ax.barh(y, df['Target'], height=bar_height * 1.15, label='Target', color='lightblue')

# Actual Bar (အပေါ်က layer)
ax.barh(y, df['Actual'], height=bar_height * 1, label='Actual', color='lightgreen')

# %Achieved ကို bar ရဲ့ညာဘက်မှာ ပြသခြင်း
for i, target_value in enumerate(df['Target']):
    achieved_text = df.loc[i, 'Achieved (%)']
    ax.text(
        target_value + 2, i, achieved_text,
        va='center', fontsize=13,
        color='white', fontweight='bold'
    )

# Actual value မှာ Vertical line တစ်ကြောင်းထည့်ခြင်း
for i in y:
    actual = df.loc[i, 'Actual']
    ax.plot([actual, actual], [i - 0.3, i + 0.3], color='green', linewidth=4)

# Y-axis သတ်မှတ်ချက်
ax.set_yticks(y)
ax.set_yticklabels(df['Region'], fontsize=13, color='white')

# y-axis label နဲ့ bar ကြားအကွာအဝေးချဲခြင်း
ax.tick_params(axis='y', pad=15)

# x-axis label color, size, spacing သတ်မှတ်ခြင်း
ax.tick_params(axis='x', pad=15, colors='white', labelsize=12)

# Chart background transparency
ax.set_facecolor('none')
fig.patch.set_facecolor('none')

# Y-axis ကို ထိပ်ဆုံးမှ စအောင် ပြောင်းလဲခြင်း
ax.invert_yaxis()

# Grid မပြစေလိုလို့ ဖျောက်ခြင်း
ax.grid(False)

# Legend သတ်မှတ်ခြင်း
legend = ax.legend(loc='lower right', fontsize=16, frameon=False)
for text in legend.get_texts():
    text.set_color('white')  # Dark mode အတွက် legend text color ပြောင်းခြင်း

# ခေါင်းစဥ် စနစ်တကျရေးခြင်း
ax.set_title(
    'Target vs Actual with Markers',
    fontsize=18,
    pad=15,  # ခေါင်းစဥ်နဲ့ chart ကြားအကွာအဝေး
    loc='center',
    bbox=dict(
        facecolor='lightblue',  # ခေါင်းစဥ်အတွက် background
        edgecolor='none',       # ဘောင်မပါစေဖို့
        boxstyle='round, pad=0.5'  # border style
    )
)

# ဘောင်များဖျောက်ခြင်း
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)

# layout ကို ချောမွေ့အောင်ချိန်ညှိ
plt.tight_layout()

# Streamlit ထဲမှာ blank line နှစ်ကြောင်းထည့်
st.text("")
st.text("")

# အောက်ခြေမှာ ခေါင်းစဥ်တစ်ခုပြသခြင်း
st.markdown("#### Target vs Actual Analysis by Region")
st.info("*Please swith **DARK MODE** at application setting/ ကျေးဇူးပြုပြီး Darkmode setting လေးပြောင်းပြီး ကြည့်ရှုပေးပါခင်ဗျာ*")
st.pyplot(fig)