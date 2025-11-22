from dataclasses import dataclass
from typing import List


@dataclass
class Employee:
    name: str
    position: str
    completed_tasks: int
    performance: float
    skills: List[str]
    team: str
    experience_years: int

    @classmethod
    def from_csv_row(cls, row):
        return cls(
            name=row["name"],
            position=row["position"],
            completed_tasks=int(row["completed_tasks"]),
            performance=float(row["performance"]),
            skills=[
                skill.strip() for skill in row["skills"].strip('"').split(",")
            ],
            team=row["team"],
            experience_years=int(row["experience_years"]),
        )

    def to_csv_row(self):
        return {
            "name": self.name,
            "position": self.position,
            "completed_tasks": self.completed_tasks,
            "performance": self.performance,
            "skills": '"' + ", ".join(self.skills) + '"',
            "team": self.team,
            "experience_years": self.experience_years,
        }
