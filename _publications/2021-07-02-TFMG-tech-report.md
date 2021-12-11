---
title: "An Experience Report on Machine Learning
Reproducibility: Guidance for Practitioners and
TensorFlow Model Garden Contributors"
collection: publications
permalink: /publication/TFMGTechReport
excerpt: 
date: 2021-07-02
venue: 'arXiv'
paperurl: 'https://arxiv.org/pdf/2107.00821.pdf'
citation: 'Jiang, Wenxin. (2021). &quot;PAn Experience Report on Machine Learning
Reproducibility: Guidance for Practitioners and
TensorFlow Model Garden Contributors.&quot; <i>arXiv</i>. 1(1).'
---

[Download](http://academicpages.github.io/files/TFMGTechReport.pdf)

##Abstract
Deep learning techniques are becoming a fundamental tool for scientific and engineering progress. In recent years these techniques have been successfully applied in contexts from spam filtering to astronomy.
However, correctly applying these techniques requires careful engineering.
Much attention has been paid to the technical potential; relatively little attention has been paid to the software engineering process required to bring research-based machine learning techniques into practical utility.
Technology companies have supported the engineering community through machine learning frameworks such as TensorFlow and PyTorch, but the details of how to engineer complex machine learning models in these frameworks have remained hidden.

To promote best practices within the engineering community, academic institutions and Google have partnered to launch a Special Interest Group on Machine Learning Models (SIGMODELS) whose goal is to develop exemplary implementations of major machine learning models in the TensorFlow Model Garden (TFMG).
The purpose of this report is to define a process for reproducing a state-of-the-art machine learning model at a level of quality suitable for inclusion in the TFMG. We define the engineering process and elaborate on each step, from paper analysis to model release. We report on our experiences implementing the YOLO model family with a team of 23 engineers, share the tools we  developed, and describe the lessons we learned along the way.