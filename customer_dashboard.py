"""Customer cluster profile dashboard for the P2 Fintech project."""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def create_dashboard(input_csv, output_png):
    customers = pd.read_csv(input_csv)

    if "cluster" not in customers.columns:
        raise ValueError("Input CSV must contain a 'cluster' column.")

    metrics = {
        "Average total spend": "total_spend",
        "Average transaction count": "transaction_count",
        "Average transaction amount": "average_transaction_amount",
        "Average annual income": "annual_income",
        "Average failed attempts": "failed_attempts_total",
        "Average customer tenure (months)": "tenure_months",
    }

    required = ["customer_id", *metrics.values()]
    missing = [column for column in required
               if column not in customers.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    profile = customers.groupby("cluster").agg(
        customer_count=("customer_id", "count"),
        **{
            "avg_" + name: (column, "mean")
            for name, column in metrics.items()
        }
    )

    fig, axes = plt.subplots(2, 3, figsize=(16, 9))
    axes = axes.flatten()

    for ax, (title, column) in zip(axes, metrics.items()):
        values = customers.groupby("cluster")[column].mean()
        bars = ax.bar(values.index.astype(str), values.values)
        ax.set_title(title)
        ax.set_xlabel("Customer cluster")
        ax.set_ylabel("Average value")
        ax.grid(axis="y", alpha=0.25)

        for bar, value in zip(bars, values.values):
            ax.annotate(
                f"{value:,.2f}",
                (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                xytext=(0, 3),
                textcoords="offset points",
                ha="center",
                fontsize=8
            )

    fig.suptitle("Fintech Customer Segmentation Dashboard", fontsize=16)
    fig.tight_layout()

    output_png = Path(output_png)
    output_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_png, dpi=150, bbox_inches="tight")
    plt.close(fig)

    profile.to_csv(
        output_png.with_name("customer_cluster_profiles_from_script.csv")
    )

    print("Dashboard saved to:", output_png)
    print(profile.round(2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="customer_clusters.csv",
        help="Path to the customer cluster CSV"
    )
    parser.add_argument(
        "--output",
        default="customer_segmentation_dashboard.png",
        help="Path for the dashboard image"
    )
    args = parser.parse_args()
    create_dashboard(args.input, args.output)
