"""
The functions from this file are reused to show plots in Jupyter notebook
abstracting code and only displaying plots in the notebook.
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import os


def plot_radar_chart(df, graph_name):
    """
    Plots a radar chart based on the input DataFrame and saves the
    plot as a PNG file.

    Parameters:
    df (pandas.DataFrame): The input DataFrame. It should contain the
    following columns:
        'dlr_soft_class', 'howfairis_repository', 'howfairis_license',
        'howfairis_registry', 'howfairis_citation', 'howfairis_checklist'
    graph_name (str): The name of the output PNG file.

    Returns:
    None. A PNG file is saved in the current working directory.
    """
    # Check if necessary columns exist in the DataFrame
    necessary_columns = [
        'dlr_soft_class', 'howfairis_repository', 'howfairis_license',
        'howfairis_registry', 'howfairis_citation', 'howfairis_checklist'
    ]
    for column in necessary_columns:
        if column not in df.columns:
            print(f"Column '{column}' not found in the DataFrame.")
            return

    # Rename the columns
    df = df.rename(columns={
        'dlr_soft_class': 'DLR Class',
        'howfairis_repository': 'Opensource',
        'howfairis_license': 'License',
        'howfairis_registry': 'Registry',
        'howfairis_citation': 'Citation',
        'howfairis_checklist': 'Checklist'
    })

    # Convert boolean to int
    df[['Opensource', 'License', 'Registry', 'Citation', 'Checklist']] = df[
        ['Opensource', 'License', 'Registry', 'Citation', 'Checklist']
    ].astype(int)

    # Filter the DataFrame according to 'DLR Class' values
    df = df[df['DLR Class'].isin([0.0, 1.0, 2.0])]

    # Convert 'DLR Class' to integer
    df['DLR Class'] = df['DLR Class'].astype(int)

    # Select the specified columns and group by 'DLR Class'
    columns = ['DLR Class', 'Opensource', 'License', 'Registry', 'Citation', 'Checklist']
    df = df[columns].groupby('DLR Class').mean().reset_index()

    # Plotting radar chart
    labels = df.columns[1:]
    num_vars = len(labels)

    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    for i, row in df.iterrows():
        values = row.drop('DLR Class').tolist()
        values += values[:1]
        label = f"Class {int(row['DLR Class'])}"  # Use class as label
        ax.plot(angles, values, label=label)
        ax.fill(angles, values, alpha=0.25)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    plt.legend(loc='upper right')
    plt.savefig(f'{graph_name}.png')
    plt.show()


def plot_documentation(df, file_path):
    """
    Plots a grouped bar chart based on the input
    DataFrame and saves the plot as a PNG file.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.
    It should contain the following columns:
        'dlr_soft_class', 'readme_content',
        'quick_start_guide', 'help_commands'
    file_path (str): The full path of the output PNG file.

    Returns:
    None. A PNG file is saved in the specified path.
    """
    df = df[df['dlr_soft_class'].isin([0, 1, 2])]
    total_counts = df['dlr_soft_class'].value_counts()
    features = ['readme_content', 'quick_start_guide', 'help_commands']
    feature_labels = ['Project Information', 'Installation Instructions',
                      'Usage Guide']
    percentages = [
        [
            (df[(df['dlr_soft_class'] == dlr_class) & (df[feature])].shape[0] /
             total_counts[dlr_class]) * 100 for feature in features
        ]
        for dlr_class in [0, 1, 2]
    ]
    bar_width = 0.2
    r = np.arange(len(features))
    for i in range(3):
        plt.bar(
            r + i * bar_width, percentages[i],
            color=plt.cm.viridis(i / 2.5),
            width=bar_width,
            edgecolor='grey',
            label=f'Class {i}'
        )
    plt.ylabel('Percentage (%)', fontweight='bold')
    plt.xticks([r + bar_width for r in range(len(features))], feature_labels)
    plt.legend()
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    plt.savefig(file_path)
    plt.show()


def plot_stacked_bar_reuse(df, column_name, file_path):
    """
    Plots a stacked bar chart based on the input DataFrame and saves
    the plot as a PNG file.

    Parameters:
    df (pandas.DataFrame): The input DataFrame. It should contain
    the following columns:
        'dlr_soft_class' and the column specified in column_name.
    column_name (str): The name of the column to calculate percentages for.
    file_path (str): The full path of the output PNG file.

    Returns:
    None. A PNG file is saved in the specified path.
    """
    # Calculate percentages of column_name presence for each 'dlr_soft_class'
    percentages = df.groupby('dlr_soft_class')[column_name].value_counts(
        normalize=True).unstack() * 100

    # Plot the stacked bar chart
    percentages.plot(kind='bar', stacked=True, cmap='viridis')

    # Set labels and title
    plt.xlabel('DLR Software Class')
    plt.ylabel('Percentage of Repositories')

    # Move legend outside the plot
    plt.legend(
        title='Explicit requirement', labels=['No', 'Yes'],
        bbox_to_anchor=(1.05, 1), loc='upper left'
    )

    # Save the plot
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    plt.savefig(file_path, bbox_inches='tight')

    # Show the plot
    plt.show()


def plot_continuous_integration(df, file_path):
    """
    Plots a grouped bar chart based on the input DataFrame and saves the plot as a PNG file.

    Parameters:
    df (pandas.DataFrame): The input DataFrame. It should contain the following columns:
        'language', 'dlr_soft_class', 'continuous_integration', 'add_test_rule', 'add_lint_rule'
    file_path (str): The full path of the output PNG file.

    Returns:
    None. A PNG file is saved in the specified path.
    """
    # Filter the DataFrame according to 'language' and 'dlr_soft_class' values
    df = df[df['language'].isin(['C++', 'Python', 'R']) &
            df['dlr_soft_class'].isin([0, 1, 2])]

    # Calculate the total count for each 'dlr_soft_class'
    total_counts = df['dlr_soft_class'].value_counts()

    # Calculate the percentage of True values for each column and 'dlr_soft_class'
    features = ['continuous_integration', 'add_test_rule', 'add_lint_rule']
    percentages = [
        [
            (df[(df['dlr_soft_class'] == dlr_class) & (df[feature])].shape[0] /
             total_counts[dlr_class]) * 100 for feature in features
        ]
        for dlr_class in [0, 1, 2]
    ]

    # Bar width
    bar_width = 0.2

    # Positions of the bars on the x-axis
    r = np.arange(len(features))

    # Create the grouped bar chart
    for i in range(3):
        plt.bar(r + i * bar_width, percentages[i],
                color=plt.cm.viridis(i / 2.5),
                width=bar_width, edgecolor='grey', label=f'Class {i}')

    # Adding labels
    plt.ylabel('Percentage (%)', fontweight='bold')
    updated_labels = ['Continuous Integration', 'Linters in CI', 'Automated Testing']
    plt.xticks([r + bar_width for r in range(len(features))], updated_labels)

    # Adding the legend
    plt.legend()

    # Save the plot
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    plt.savefig(file_path)

    # Show the plot
    plt.show()


def plot_comment_start(df, file_path):
    """
    Plots a stacked bar chart based on the input DataFrame and saves the plot as a PNG file.

    Parameters:
    df (pandas.DataFrame): The input DataFrame. It should contain the following columns:
        'language', 'dlr_soft_class', 'comment_category'
    file_path (str): The full path of the output PNG file.

    Returns:
    None. A PNG file is saved in the specified path.
    """
    # Step 2: Filter Data by Language
    df = df[df['language'].isin(['Python', 'C++', 'R'])]

    # Replace 'none' with 'less' and ensure comment_category is a categorical type with the correct order
    df['comment_category'] = df['comment_category'].replace('none', 'less')
    comment_order = ['less', 'some', 'more', 'most']
    df['comment_category'] = pd.Categorical(df['comment_category'],
                                            categories=comment_order, ordered=True)

    # Step 3: Prepare Data for Visualization
    # Create a pivot table for the stacked bar plot with percentages
    pivot_table = df.pivot_table(index='dlr_soft_class',
                                 columns='comment_category', aggfunc='size', fill_value=0)

    # Calculate the percentage
    pivot_table = pivot_table.div(pivot_table.sum(axis=1), axis=0) * 100

    # Step 4: Create Stacked Bar Plot
    plt.figure(figsize=(10, 6))
    pivot_table.plot(kind='bar', stacked=True, cmap='viridis')
    plt.xlabel('DLR Application Class')
    plt.ylabel('Percentage of Repositories')
    plt.legend(title='Files with comment at start', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    # Save the plot
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    plt.savefig(file_path)

    # Show the plot
    plt.show()
