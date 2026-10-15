"""
Project: Project Initialization & Scope Planner
Author: Patricia Fletcher
Description: A Python CLI tool to initialize project phases, objectives, and milestones.
"""

print("=" * 60)
print("         PROJECT INITIALIZATION & SCOPE PLANNER         ")
print("=" * 60 + "\n")

# Project details template (Dictionary)
project_data = {
    "project_name": "",
    "manager": "Patricia Fletcher",
    "phases": ["1. Initiation", "2. Planning", "3. Execution", "4. Closure"],
    "objectives": []
}

# 1. Initialize Project Name
proj_name_input = input("Enter the new project name: ").strip()
if proj_name_input:
    project_data["project_name"] = proj_name_input
else:
    project_data["project_name"] = "Default Remote Tech Project"

print(f"\n[INFO] Initializing project: '{project_data['project_name']}' managed by {project_data['manager']}\n")

# 2. Add Key Objectives using a while loop
print("--- DEFINE PROJECT OBJECTIVES ---")
while True:
    objective = input("Enter a key objective (or type 'done' to finish): ").strip()
    if objective.lower() == 'done':
        break
    if objective:
        project_data["objectives"].append(objective)
        print(f"Added objective: '{objective}'")

# 3. Summary Report Generation
print("\n" + "=" * 60)
print(f"       PROJECT BLUEPRINT SUMMARY: {project_data['project_name'].upper()}       ")
print("=" * 60)
print(f"Project Manager: {project_data['manager']}")
print("\nLifecycle Phases:")
for phase in project_data["phases"]:
    print(f"  - {phase}")

print("\nCore Objectives:")
if project_data["objectives"]:
    for idx, obj in enumerate(project_data["objectives"], 1):
        print(f"  {idx}. {obj}")
else:
    print("  (No specific objectives recorded)")

print("=" * 60)
print("[STATUS] Project successfully initialized and ready for execution!")
print("=" * 60)

input("\nPress Enter to exit the planner...")
