from typing import List, Optional
from pydantic import BaseModel, Field


class Task(BaseModel):
    name: str
    status: Optional[str] = Field(None, description="Status of the task, e.g., 'done', 'active', 'crit', 'milestone'")
    id: Optional[str] = Field(None, description="ID of the task")
    start_date: Optional[str] = Field(None, description="Start date of the task in the format specified by dateFormat")
    end_date: Optional[str] = Field(None, description="End date of the task in the format specified by dateFormat")
    duration: Optional[str] = Field(None, description="Duration of the task")
    dependencies: Optional[str] = Field(None, description="Dependencies on other tasks using 'after' keyword")


class Section(BaseModel):
    name: str
    tasks: List[Task]


class GanttChart(BaseModel):
    date_format: str = Field(..., alias='dateFormat', description="Format of the dates used in the Gantt chart")
    title: Optional[str] = Field(None, description="Title of the Gantt chart")
    excludes: Optional[str] = Field(None, description="Dates or days to be excluded, e.g., 'weekends', specific dates")
    sections: List[Section]
    tick_interval: Optional[str] = Field(None, alias='tickInterval', description="Interval for axis ticks")
    weekday: Optional[str] = Field(None, description="Start day of the week for tickInterval")
    axis_format: Optional[str] = Field(None, alias='axisFormat', description="Format of the dates on the axis")


# Example usage
gantt_chart = GanttChart(
    dateFormat="YYYY-MM-DD",
    title="Adding GANTT diagram functionality to mermaid",
    excludes="weekends",
    sections=[
        Section(
            name="A section",
            tasks=[
                Task(name="Completed task", status="done", id="des1", start_date="2014-01-06", end_date="2014-01-08"),
                Task(name="Active task", status="active", id="des2", start_date="2014-01-09", duration="3d"),
                Task(name="Future task", id="des3", duration="5d", dependencies="after des2"),
                Task(name="Future task2", id="des4", duration="5d", dependencies="after des3"),
            ]
        ),
        Section(
            name="Critical tasks",
            tasks=[
                Task(name="Completed task in the critical line", status="crit, done", start_date="2014-01-06",
                     duration="24h"),
                Task(name="Implement parser and jison", status="crit, done", duration="2d", dependencies="after des1"),
                Task(name="Create tests for parser", status="crit, active", duration="3d"),
                Task(name="Future task in critical line", status="crit", duration="5d"),
                Task(name="Create tests for renderer", duration="2d"),
                Task(name="Add to mermaid", dependencies="until isadded"),
                Task(name="Functionality added", status="milestone", id="isadded", start_date="2014-01-25",
                     duration="0d"),
            ]
        ),
        Section(
            name="Documentation",
            tasks=[
                Task(name="Describe gantt syntax", status="active", id="a1", duration="3d", dependencies="after des1"),
                Task(name="Add gantt diagram to demo page", duration="20h", dependencies="after a1"),
                Task(name="Add another diagram to demo page", id="doc1", duration="48h", dependencies="after a1"),
            ]
        ),
        Section(
            name="Last section",
            tasks=[
                Task(name="Describe gantt syntax", duration="3d", dependencies="after doc1"),
                Task(name="Add gantt diagram to demo page", duration="20h"),
                Task(name="Add another diagram to demo page", duration="48h"),
            ]
        )
    ]
)


def main():
    """Main function"""
    from dspygen.utils.dspy_tools import init_ol
    init_ol()
    print(gantt_chart.model_dump_json())


if __name__ == '__main__':
    main()