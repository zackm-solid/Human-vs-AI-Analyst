"""
Streamlit dashboard replicating the Tableau visualization described in
`cursor/cursor.md`.
"""

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


DATA_PATH = Path(__file__).resolve().parents[1] / "employment_data_final.csv"

df = pd.read_csv(DATA_PATH)

COLUMN_RENAMES = {
    "title": "Title",
    "ai_applicability_score": "AI Applicability Score",
    "Employment Change, 2024-2034 (Thousands)": "Employment Change",
    "Employment Percent Change, 2024-2034": "Employment Percent Change",
    "Median Annual Wage 2024": "Median Annual Wage",
}

df.rename(columns=COLUMN_RENAMES, inplace=True)

analytics_roles_list = sorted(
    df.loc[
        df["Title"].str.contains(
            "Analyst|Data|Specialist|Operations", case=False, na=False
        ),
        "Title",
    ]
    .dropna()
    .unique()
    .tolist()
)


def build_growth_map(data_frame: pd.DataFrame):
    """Create the AI vs Growth Map bubble chart."""
    if data_frame.empty:
        return px.scatter(title="AI vs Growth Map")

    plot_df = data_frame.copy()
    plot_df["Employment Change Magnitude"] = (
        plot_df["Employment Change"].abs().clip(lower=0)
    )

    fig = px.scatter(
        plot_df,
        x="AI Applicability Score",
        y="Employment Percent Change",
        size="Employment Change Magnitude",
        color="Median Annual Wage",
        color_continuous_scale="OrRd",
        hover_name="Title",
        hover_data={"Employment Change": True},
        title="AI vs Growth Map",
        size_max=60,
    )

    x_mean = data_frame["AI Applicability Score"].mean()
    y_mean = data_frame["Employment Percent Change"].mean()

    fig.add_vline(x=x_mean, line_dash="dash", line_color="gray", opacity=0.6)
    fig.add_hline(y=y_mean, line_dash="dash", line_color="gray", opacity=0.6)

    fig.update_layout(margin=dict(l=20, r=20, t=60, b=20))
    return fig


def build_analytics_deep_dive(data_frame: pd.DataFrame, roles_list: list[str]):
    """Horizontal bar chart of analytics roles by AI applicability."""
    filtered = data_frame[data_frame["Title"].isin(roles_list)].copy()
    if filtered.empty:
        return px.bar(title="Analytics Role Deep-Dive")

    filtered.sort_values("AI Applicability Score", ascending=False, inplace=True)

    fig = px.bar(
        filtered,
        x="AI Applicability Score",
        y="Title",
        orientation="h",
        title="Analytics Role Deep-Dive",
    )
    fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
    return fig


def build_analytics_growth(data_frame: pd.DataFrame, roles_list: list[str]):
    """Horizontal bar chart of analytics roles by employment percent change."""
    filtered = data_frame[data_frame["Title"].isin(roles_list)].copy()
    if filtered.empty:
        return px.bar(title="Analytics Role Growth")

    filtered.sort_values("Employment Percent Change", ascending=False, inplace=True)

    fig = px.bar(
        filtered,
        x="Employment Percent Change",
        y="Title",
        orientation="h",
        title="Analytics Role Growth",
    )
    fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
    return fig


def main():
    st.set_page_config(layout="wide")
    st.title("AI, Jobs, and Salary Analysis")

    title_options = sorted(df["Title"].dropna().unique().tolist())
    selected_titles = st.multiselect("Filter by Job Title:", title_options)

    if selected_titles:
        filtered_df = df[df["Title"].isin(selected_titles)].copy()
    else:
        filtered_df = df.copy()

    col1, col2 = st.columns([2, 1])

    col1.plotly_chart(build_growth_map(filtered_df), use_container_width=True)
    col2.plotly_chart(
        build_analytics_deep_dive(filtered_df, analytics_roles_list),
        use_container_width=True,
    )
    col2.plotly_chart(
        build_analytics_growth(filtered_df, analytics_roles_list),
        use_container_width=True,
    )


if __name__ == "__main__":
    main()


