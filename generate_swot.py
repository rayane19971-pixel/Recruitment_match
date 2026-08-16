import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_swot():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Colors based on Nexa Digital School / OL theme
    c_strengths = '#6f2f9f'  # Nexa Purple
    c_weaknesses = '#ef4444' # Red
    c_opportunities = '#10b981' # Green
    c_threats = '#f59e0b' # Amber

    # Draw 4 quadrants
    # Strengths (Top Left)
    rect_s = patches.Rectangle((0.5, 5.5), 4.25, 4, linewidth=2, edgecolor=c_strengths, facecolor='#f8fafc', alpha=0.9)
    ax.add_patch(rect_s)
    ax.text(2.625, 9, 'FORCES (STRENGTHS)', fontsize=16, fontweight='bold', color=c_strengths, ha='center')
    text_s = "- Infrastructure Data existante\n- Algorithme k-NN performant\n- API Opta Premium\n- Soutien d'Eagle Football"
    ax.text(0.8, 7.5, text_s, fontsize=12, color='#334155', va='top', ha='left', linespacing=1.8)

    # Weaknesses (Top Right)
    rect_w = patches.Rectangle((5.25, 5.5), 4.25, 4, linewidth=2, edgecolor=c_weaknesses, facecolor='#f8fafc', alpha=0.9)
    ax.add_patch(rect_w)
    ax.text(7.375, 9, 'FAIBLESSES (WEAKNESSES)', fontsize=16, fontweight='bold', color=c_weaknesses, ha='center')
    text_w = "- Coût initial élevé (CAPEX)\n- Dépendance à l'API externe\n- Courbe d'apprentissage pour\n  les recruteurs non-tech"
    ax.text(5.55, 7.5, text_w, fontsize=12, color='#334155', va='top', ha='left', linespacing=1.8)

    # Opportunities (Bottom Left)
    rect_o = patches.Rectangle((0.5, 1), 4.25, 4, linewidth=2, edgecolor=c_opportunities, facecolor='#f8fafc', alpha=0.9)
    ax.add_patch(rect_o)
    ax.text(2.625, 4.5, 'OPPORTUNITÉS (OPPORTUNITIES)', fontsize=16, fontweight='bold', color=c_opportunities, ha='center')
    text_o = "- Détection de pépites cachées\n- Fortes plus-values à la revente\n- Évitement des flops à 15M€\n- Marchés de niche explorés"
    ax.text(0.8, 3, text_o, fontsize=12, color='#334155', va='top', ha='left', linespacing=1.8)

    # Threats (Bottom Right)
    rect_t = patches.Rectangle((5.25, 1), 4.25, 4, linewidth=2, edgecolor=c_threats, facecolor='#f8fafc', alpha=0.9)
    ax.add_patch(rect_t)
    ax.text(7.375, 4.5, 'MENACES (THREATS)', fontsize=16, fontweight='bold', color=c_threats, ha='center')
    text_t = "- Contraintes DNCG & UEFA\n- Plafond salarial restrictif\n- Clubs concurrents adoptant\n  la même stratégie IA"
    ax.text(5.55, 3, text_t, fontsize=12, color='#334155', va='top', ha='left', linespacing=1.8)

    plt.tight_layout()
    plt.savefig('swot_chart.png', dpi=300, bbox_inches='tight', transparent=True)
    plt.close()

if __name__ == "__main__":
    draw_swot()
    print("swot_chart.png generated!")
