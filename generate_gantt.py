import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

def draw_gantt():
    fig, ax = plt.subplots(figsize=(12, 6))

    tasks = [
        "1. Sprint 1: Architecture & Base de Données (Mois 1)",
        "2. Sprint 2: IA, Data & Algorithme k-NN (Mois 2)",
        "3. Sprint 3: Front-End React & UI/UX (Mois 3)",
        "4. Sprint 4: Tests, QA & Déploiement (Mois 4)"
    ]

    start_date = datetime(2026, 4, 1)
    
    # Define start and durations for each sprint
    starts = [
        start_date,
        start_date + timedelta(days=30),
        start_date + timedelta(days=60),
        start_date + timedelta(days=90)
    ]
    
    ends = [
        start_date + timedelta(days=30),
        start_date + timedelta(days=60),
        start_date + timedelta(days=90),
        start_date + timedelta(days=120)
    ]

    colors = ['#1e293b', '#6f2f9f', '#3b82f6', '#10b981']

    for i in range(len(tasks)):
        ax.barh(tasks[i], (ends[i]-starts[i]).days, left=starts[i], height=0.6, color=colors[i], align='center', alpha=0.9)
        # Add text in the middle
        mid_date = starts[i] + (ends[i]-starts[i])/2
        ax.text(mid_date, i, f"Livrable {i+1}", ha='center', va='center', color='white', fontweight='bold')

    # Formatting axes
    ax.invert_yaxis()  # top-to-bottom
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    
    ax.set_title("Rétroplanning GANTT - Méthodologie Scrum (16 Semaines)", fontsize=16, fontweight='bold', color='#0f172a', pad=20)
    
    ax.grid(True, axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig('gantt_chart.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    draw_gantt()
    print("gantt_chart.png generated!")
