import streamlit as st

st.set_page_config(
    page_title="MathCraft: Greek Letters",
    page_icon="🧮",
    layout="wide"
)

# -------------------------------
# Link to CognitiveCloud.ai
# -------------------------------
st.link_button("CognitiveCloud.ai Math Apps", "https://cognitivecloud-launcher.streamlit.app/#cognitive-cloud-ai-app-launcher")

# -------------------------------
# Header
# -------------------------------
st.title("🎓 MathCraft: Greek Letters in Mathematics")
st.markdown("A legendary guide from the dawn of civilization to modern science.")

# -------------------------------
# Ancient African Mathematics
# -------------------------------
st.header("The Roots of Mathematics in Timbuktu")
st.markdown("""
Long before the European Renaissance, the city of Timbuktu in the Mali Empire was a world-renowned center of learning. Scholars at institutions like the University of Sankore produced vast collections of manuscripts covering a wide range of subjects, including mathematics, astronomy, and philosophy.

These texts, some of which date back to the 13th century, showcase sophisticated knowledge in **algebra**, **geometry**, and **arithmetic**. They were used for practical applications like land measurement, trade calculations, and determining inheritance according to Islamic law. The preservation of these manuscripts highlights a rich intellectual heritage that existed long before the mathematical contributions of the Greeks and other cultures.
""")

# -------------------------------
# Story / Lesson
# -------------------------------
st.header("The Journey of Knowledge")
st.markdown("""
Building upon the foundations of earlier civilizations, the torch of knowledge was passed to the great Greek thinkers. Pythagoras discovered the relationship between the sides of a right triangle. Archimedes laid the groundwork for calculus. Euclid's "Elements" became the bedrock of geometry for centuries.

These thinkers didn't just solve problems; they created a language for the universe. The Greek alphabet, in their hands, transcended its role as a mere writing system. It became a powerful tool to describe abstract concepts, from the ratio of a circle's circumference to its diameter ($π$) to the rate of change of a quantity ($Δ$).

Today, these same Greek letters are used in fields as diverse as physics, engineering, finance, and computer science, proving the timeless nature of their discoveries.
""")

# -------------------------------
# Greek Letter Tutorial
# -------------------------------
st.header("The Greek Alphabet in Mathcraft")
greek_letters = [
    {"name": "Alpha", "symbol": "$α$", "use": "Angles, angular acceleration, coefficient of thermal expansion, particle physics"},
    {"name": "Beta", "symbol": "$β$", "use": "Angles, a type of radiation, statistical coefficients"},
    {"name": "Delta", "symbol": "$Δ$ / $δ$", "use": "Change in quantity, small variations"},
    {"name": "Epsilon", "symbol": "$ε$", "use": "Small positive number in calculus, permittivity"},
    {"name": "Pi", "symbol": "$π$", "use": "Ratio of a circle's circumference to diameter"},
    {"name": "Sigma", "symbol": "$Σ$ / $σ$", "use": "Summation, standard deviation"},
    {"name": "Omega", "symbol": "$Ω$ / $ω$", "use": "Ohms, angular velocity/frequency"},
    {"name": "Gamma", "symbol": "$γ$", "use": "Gamma radiation, Lorentz factor"}
]

for letter in greek_letters:
    st.subheader(f"{letter['name']} ({letter['symbol']})")
    st.write(f"**Used for:** {letter['use']}")

# -------------------------------
# Proficiency Quiz
# -------------------------------
st.header("Proficiency Test")
quiz_questions = [
    {"q":"Which Greek letter is often used to represent angular acceleration?",
      "options":["$π$ (Pi)", "$α$ (Alpha)", "$γ$ (Gamma)", "$ω$ (Omega)"],
      "answer":"$α$ (Alpha)"},
    {"q":"In statistics, which letter is used for a statistical coefficient?",
      "options":["$Δ$ (Delta)", "$β$ (Beta)", "$ε$ (Epsilon)", "$σ$ (Sigma)"],
      "answer":"$β$ (Beta)"},
    {"q":"The symbol $Δ$ is used to represent?",
      "options":["A large change in quantity", "A small positive number", "Angular velocity", "The golden ratio"],
      "answer":"A large change in quantity"},
    {"q":"Which letter is used in calculus to denote an infinitesimally small positive number?",
      "options":["$α$ (Alpha)", "$β$ (Beta)", "$ε$ (Epsilon)", "$π$ (Pi)"],
      "answer":"$ε$ (Epsilon)"},
    {"q":"Which Greek letter is used to represent the ratio of a circle's circumference to its diameter?",
      "options":["$α$ (Alpha)", "$π$ (Pi)", "$δ$ (Delta)", "$σ$ (Sigma)"],
      "answer":"$π$ (Pi)"},
    {"q":"Uppercase $Σ$ represents which mathematical operation?",
      "options":["Change in quantity", "Summation", "Standard deviation", "Angular velocity"],
      "answer":"Summation"},
    {"q":"What does the symbol $ω$ often represent in physics?",
      "options":["Ohms", "Angular velocity/frequency", "Wavelength", "Work function"],
      "answer":"Angular velocity/frequency"},
    {"q":"Which Greek letter is used to represent the Lorentz factor in physics?",
      "options":["$α$ (Alpha)", "$γ$ (Gamma)", "$δ$ (Delta)", "$Ω$ (Omega)"],
      "answer":"$γ$ (Gamma)"}
]

for i, q in enumerate(quiz_questions):
    st.subheader(f"Q{i+1}: {q['q']}")
    choice = st.radio("Select your answer:", q["options"], key=f"q{i}")
    if st.button(f"Check Answer Q{i+1}", key=f"btn{i}"):
        if choice == q["answer"]:
            st.success("Correct! 🎉")
        else:
            st.error(f"Incorrect. The correct answer is {q['answer']}.")

# -------------------------------
# Math Verbs Section
# -------------------------------
st.header("The Greek Letters as 'Math Verbs'")
st.markdown("""
In the world of MathCraft, these symbols aren't just letters; they are commands that tell you to perform a specific action or operation. Think of them as verbs that give a direction to a mathematical concept.
""")

st.subheader("Mathematical Verbs")
st.markdown("""
- **Delta ($Δ$)** — The verb is "**change**". It commands you to calculate the difference between two quantities.
- **Epsilon ($ε$)** — The verb is "**minimize**". It signifies a quantity so small it's approaching zero, a key concept in limits.
- **Pi ($π$)** — The verb is "**relate**". It is the fundamental command to connect a circle's circumference and diameter.
- **Sigma ($Σ$)** — The verb is "**sum**". The uppercase sigma is a direct command to add up all the terms in a series.
- **Omega ($ω$)** — The verb is "**rotate**". It tells you how fast an object is spinning, its angular velocity.
- **Gamma ($γ$)** — The verb is "**adjust**". In physics, it modifies measurements for objects traveling at very high speeds.
""")

st.subheader("Quantitative Finance Verbs (Options Greeks)")
st.markdown("""
In finance, these verbs describe how an option's price reacts to different market variables.

- **Delta ($Δ$)** — The verb is "**react**". It tells you how much the option's price will react to a change in the underlying asset's price.
- **Gamma ($Γ$)** — The verb is "**change the reaction**". It tells you how much Delta itself will change with the asset's price.
- **Theta ($Θ$)** — The verb is "**decay**". It commands you to understand how much value the option loses over time.
- **Vega ($ν$)** — The verb is "**sense**". It tells you how sensitive the option's price is to changes in volatility.
- **Rho ($ρ$)** — The verb is "**respond**". It describes how the option's price will respond to a change in interest rates.
""")

# -------------------------------
# Resources Section
# -------------------------------
st.header("📚 Resources")

st.subheader("1. Quantitative Finance & Options Greeks")
st.markdown("""
- **Delta ($Δ$)** – Sensitivity of option price to underlying asset
- **Gamma ($Γ$)** – Rate of change of Delta
- **Theta ($Θ$)** – Time decay
- **Vega ($ν$)** – Sensitivity to volatility
- **Rho ($ρ$)** – Sensitivity to interest rates

**Links:**
- [Investopedia: Option Greeks](https://www.investopedia.com/trading/options-greeks/)
- [CBOE Options Education](https://www.optionseducation.org/advancedconcepts/understanding-options-greeks)
- [QuantStart: Quantitative Trading](https://www.quantstart.com/articles/)
""")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>Built by Xavier Honablue M.Ed for CognitiveCloud.ai</p>", unsafe_allow_html=True)
