"""
The functions from this file are reused to show plots in jupyternotebook abstracting code and only displaying
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import plotly.express as px
import os

def plot_radar_chart(df, graph_name):
    # Rename the columns
    df = df.rename(columns={
        'dlr_soft_class': 'DLR Class',
        'howfairis_repository': 'Opensource',
        'howfairis_license': 'License',
        'howfairis_registry': 'Registry',
        'howfairis_citation': 'Citation',
        'howfairis_checklist': 'Checklist'
    })

    # Filter the DataFrame according to 'DLR Class' values
    df = df[df['DLR Class'].isin([0.0, 1.0, 2.0])]

    # Convert 'DLR Class' to integer
    df['DLR Class'] = df['DLR Class'].astype(int)

    # Select the specified columns and group by 'DLR Class'
    columns = ['DLR Class', 'Opensource', 'License', 'Registry', 'Citation', 'Checklist']
    df = df[columns].groupby('DLR Class').mean().round(0).reset_index()  # Round to nearest integer

    # Plotting radar chart
    labels = df.columns[1:]
    num_vars = len(labels)

    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    for i, row in df.iterrows():
        values = row.drop('DLR Class').tolist()
        values += values[:1]
        label = f"{int(row['DLR Class'])}"  # Use class as label
        ax.plot(angles, values, label=label)
        ax.fill(angles, values, alpha=0.25)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    plt.legend(loc='upper right')
    plt.savefig(f'{graph_name}.png')
    plt.show()