import matplotlib.pyplot as plt

# Create a blank canvas
fig, ax = plt.subplots(figsize=(16, 10))
ax.axis('off')

# Define table positions (x, y)
positions = {
    "users": (0, 4),
    "data_hub": (3, 6),
    "communications": (3, 4),
    "events": (3, 2),
    "event_attendance": (6, 2),
    "system_features": (0, 6),
    "security_logs": (6, 4),
    "technology_stack": (0, 2),
    "strategic_outcomes": (0, 0),
    "benefits": (3, 0)
}

# Define tables and attributes
tables = {
    "users": ["user_id (PK)", "full_name", "email", "role", "occupation"],
    "data_hub": ["hub_id (PK)", "user_id (FK)", "charms", "insights"],
    "communications": ["message_id (PK)", "user_id (FK)", "method", "content"],
    "events": ["event_id (PK)", "event_type", "title", "event_date"],
    "event_attendance": ["attendance_id (PK)", "event_id (FK)", "user_id (FK)", "attended"],
    "system_features": ["feature_id (PK)", "category", "feature_name"],
    "security_logs": ["log_id (PK)", "user_id (FK)", "event_type", "success"],
    "technology_stack": ["tech_id (PK)", "component", "description"],
    "strategic_outcomes": ["outcome_id (PK)", "category", "detail"],
    "benefits": ["benefit_id (PK)", "description"]
}

# Draw tables
for table, (x, y) in positions.items():
    ax.text(x, y + 0.3, table.upper(), fontsize=10, fontweight='bold', bbox=dict(facecolor='orange', alpha=0.3))
    for i, attr in enumerate(tables[table]):
        ax.text(x, y - 0.2 - i * 0.2, attr, fontsize=9, family='monospace')

# Define relationships
relationships = [
    ("users", "data_hub"),
    ("users", "communications"),
    ("users", "event_attendance"),
    ("users", "security_logs"),
    ("events", "event_attendance")
]

# Draw relationship arrows
for src, dst in relationships:
    x1, y1 = positions[src]
    x2, y2 = positions[dst]
    ax.annotate("",
                xy=(x2 + 0.2, y2), xycoords='data',
                xytext=(x1 + 0.2, y1), textcoords='data',
                arrowprops=dict(arrowstyle="->", color='gray'))

# Title
plt.title("ER Diagram: Digital Platform for Alumni Engagement", fontsize=14, weight='bold')
plt.tight_layout()

# Save the image
plt.savefig("ER_Diagram_Alumni_Engagement.png", dpi=300)
plt.close()
