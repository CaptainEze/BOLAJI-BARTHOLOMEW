## Overview

This repository contains the analytical and computational components of the research topic **Assessing Digital Adoption and Operational Sustainability in Nigeria’s Oil and Gas Well Construction Sector** examining the relationship between digital technology adoption and well construction delivery in the Nigerian oil and gas industry.

The project adopts a data-driven approach, applying quantitative techniques to identify underlying patterns, relationships, and predictive factors that explain the efficiency and sustainability of well construction processes. It integrates exploratory statistics, clustering, classification, and decision-tree methods to derive insights from survey or field data.

---

## Repository Structure

### `analysis/`

This directory contains the notebook that manages the entire data analysis pipeline for the project.
`input.ipynb` performs the following key functions:

- **Data Ingestion & Cleaning:** Loads the main dataset, removes duplicates, handles missing values, and encodes categorical and Likert-scale variables for analysis.
- **Descriptive Analysis & Visualization:** Generates frequency tables, summary statistics (mean, median, mode), and visualizations (bar charts, histograms, pie charts) to explore distributions and relationships among variables.
- **Reliability & Validity Checks:** Calculates Cronbach’s Alpha to assess the internal consistency of questionnaire sections.
- **Factor Analysis & PCA:** Performs exploratory factor analysis to identify latent variables and applies principal component analysis (PCA) for dimensionality reduction and interpretation.
- **Inferential Statistics:** Conducts correlation analysis, t-tests, ANOVA, and multiple regression to examine relationships and group differences relevant to digital technology adoption and well construction delivery.
- **Machine Learning Modelling:** Implements classification, clustering, and decision tree models to predict project performance, segment respondents, and identify decision rules for successful technology adoption. Model evaluation metrics (accuracy, precision, recall, F1) are also computed.

---

### `models/`

This directory contains Python modules that define and execute the computational models used in the analysis. Each file isolates a specific modelling or evaluation function to maintain clarity and separation of analytical stages.

#### `classification.py`

This module implements supervised learning algorithms used to categorize data instances according to predefined classes.
It focuses on statistical and machine learning techniques—such as logistic regression or other classifier types—to model the relationship between predictor variables (technological, organizational, or operational indicators) and categorical outcomes related to well delivery performance.
The outputs of this module include classification labels, probability estimates, and measures of model fit.

#### `clustering.py`

This module contains unsupervised learning procedures used to detect natural groupings or patterns within the dataset.
Through techniques such as K-Means or hierarchical clustering, it identifies segments of observations that share similar attributes.
The purpose of clustering in this context is to reveal underlying behavioural or operational profiles among respondents or well projects without prior knowledge of class labels.

#### `decision_tree.py`

This module provides the implementation of decision tree algorithms for either classification or analysis.
It structures data-driven rules into a hierarchical tree form, making it possible to trace decision pathways that lead to specific outcomes.
Within the research context, this aids interpretability by highlighting the relative importance of technological or organizational factors that most strongly influence well construction delivery.

#### `evaluate.py`

This module encapsulates the procedures for assessing the performance of the models implemented in the other files.
It computes metrics such as accuracy, precision, recall, and F1-score.

---

### `meta/`

This directory contains high-level documentation describing the project’s conceptual and procedural framework.

* **`meta.md`** outlines the research background, motivation, and conceptual scope of the study, situating the analytical work within its disciplinary and industrial context.
* **`workflow.md`** provides a procedural breakdown of the analytical pipeline—from data collection and cleaning to statistical analysis, modelling, and interpretation.
* **`implementation.md`** describes how the computational implementation aligns with the research objectives, specifying the logic of module organization and interdependencies between scripts and notebooks.

---

### `data/`

This folder is reserved for the datasets used in the analysis.
The primary dataset referenced throughout the repository is `dataCombined.csv`, which aggregates variables relevant to digital technology adoption and well construction outcomes.
This dataset serves as the empirical foundation for all subsequent analysis and modelling tasks.

---

### `results/`

This directory stores the outputs generated by the notebooks and models.
It contains subdirectories such as `figs/`, which hold figures, and plots.
These outputs represent visual and numerical evidence supporting the interpretation of model results and descriptive findings.

---


## Conceptual Flow of the Repository

The repository follows a linear analytical structure typical of empirical quantitative research:

1. **Data Acquisition and Preparation** — Conducted in the `analysis/input.ipynb` notebook, where the raw data is cleaned, merged, and formatted for analysis.
2. **Exploratory Analysis** — Summary statistics and visualizations are produced to examine distributions and relationships among variables.
3. **Modelling** — Implemented through the scripts in the `models/` directory.

   * *Clustering* identifies latent structures in the data.
   * *Classification* predicts predefined categories based on independent variables.
   * *Decision Trees* reveal interpretable rules and feature importance.
4. **Evaluation and Validation** — The `evaluate.py` module assesses model performance, quantifying predictive accuracy and internal consistency.
5. **Documentation and Reporting** — Outputs and methodological explanations are consolidated in `results/` and `meta/` respectively.



