from __future__ import annotations

import matplotlib
from pathlib import Path

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
OUT = ROOT / "output" / "reproduced_figures"


def ensure_output() -> None:
    OUT.mkdir(parents=True, exist_ok=True)


def savefig(name: str) -> None:
    plt.tight_layout()
    plt.savefig(OUT / f"{name}.png", dpi=300)
    plt.close()


def figure_ipr_ranking(df: pd.DataFrame) -> None:
    plot_df = df.sort_values("IPR").copy()
    colors = np.where(plot_df["IPR"] < 1.0, "#C44E52", "#4C8C6B")

    fig, ax = plt.subplots(figsize=(8, 9))
    ax.barh(plot_df["province_name_english"], plot_df["IPR"], color=colors)
    ax.axvline(1.0, color="#333333", linewidth=1, linestyle="--")
    ax.set_xlabel("Inheritor-to-project ratio")
    ax.set_ylabel("")
    ax.set_title("Provincial ICH Inheritor-to-Project Ratio")
    ax.grid(axis="x", alpha=0.2)
    savefig("public_fig_1_ipr_ranking")


def lorenz(values: pd.Series) -> tuple[np.ndarray, np.ndarray]:
    arr = np.sort(values.dropna().to_numpy(dtype=float))
    arr = arr[arr >= 0]
    cumulative = np.insert(np.cumsum(arr), 0, 0.0)
    if cumulative[-1] > 0:
        cumulative = cumulative / cumulative[-1]
    x = np.linspace(0, 1, len(cumulative))
    return x, cumulative


def figure_lorenz(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(6.5, 5.2))
    ax.plot([0, 1], [0, 1], color="#555555", linestyle="--", linewidth=1)
    for column, label, color in [
        ("project_count", "ICH projects", "#4C72B0"),
        ("inheritor_count", "ICH inheritors", "#DD8452"),
        ("five_A_scenic_area_count", "5A scenic areas", "#55A868"),
    ]:
        x, y = lorenz(df[column])
        ax.plot(x, y, label=label, color=color, linewidth=2)
    ax.set_xlabel("Cumulative share of provinces")
    ax.set_ylabel("Cumulative share of total")
    ax.set_title("Concentration of Heritage and Tourism Indicators")
    ax.legend(frameon=False)
    ax.grid(alpha=0.2)
    savefig("public_fig_2_lorenz")


def figure_time_trend(panel: pd.DataFrame) -> None:
    yearly = (
        panel.groupby("year", as_index=False)
        .agg(projects=("project_count", "sum"), inheritors=("inheritor_count", "sum"))
    )
    yearly["national_ipr"] = yearly["inheritors"] / yearly["projects"]

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(yearly["year"], yearly["national_ipr"], color="#2F6F73", linewidth=2.2)
    ax.axhline(1.0, color="#555555", linestyle="--", linewidth=1)
    ax.set_xlabel("Year")
    ax.set_ylabel("National cumulative IPR")
    ax.set_title("National Cumulative IPR Trend")
    ax.grid(alpha=0.2)
    savefig("public_fig_3_time_trend")


def figure_gdp_scatter(fig5: pd.DataFrame) -> None:
    x = fig5["GDP_per_capita"].to_numpy(dtype=float)
    y = fig5["IPR"].to_numpy(dtype=float)
    slope, intercept = np.polyfit(x, y, 1)
    grid = np.linspace(x.min(), x.max(), 200)

    fig, ax = plt.subplots(figsize=(7, 4.8))
    ax.scatter(x, y, color="#2F6F73", edgecolor="white", linewidth=0.6, s=55, alpha=0.9)
    ax.plot(grid, slope * grid + intercept, color="#333333", linewidth=1.5)
    ax.axhline(1.0, color="#777777", linestyle="--", linewidth=1)

    for name in ["Shanghai", "Guangdong", "Jiangsu", "Jilin"]:
        sub = fig5.loc[fig5["province_name_english"] == name]
        if not sub.empty:
            row = sub.iloc[0]
            ax.annotate(
                name,
                (row["GDP_per_capita"], row["IPR"]),
                xytext=(5, 5),
                textcoords="offset points",
                fontsize=9,
            )

    ax.set_xlabel("GDP per capita")
    ax.set_ylabel("Inheritor-to-project ratio")
    ax.set_title("IPR and GDP per Capita")
    ax.grid(axis="y", alpha=0.2)
    savefig("public_fig_4_gdp_scatter")


def main() -> None:
    ensure_output()
    province = pd.read_csv(DATA / "province_ipr_final.csv", encoding="utf-8-sig")
    panel = pd.read_csv(DATA / "province_year_panel.csv", encoding="utf-8-sig")
    fig5 = pd.read_csv(DATA / "fig_5_source_data.csv", encoding="utf-8-sig")

    figure_ipr_ranking(province)
    figure_lorenz(province)
    figure_time_trend(panel)
    figure_gdp_scatter(fig5)

    print(f"Reproduced figures written to: {OUT}")


if __name__ == "__main__":
    main()
