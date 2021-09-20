# Software_project
Personality Recognition by Handwriting Analysis (Graphology Application)

Graphology is a technique for analyzing an individual’s personality based on the given sample of their handwriting. Graphology considers the fact that the movement of our hand is directly related to the state of our brain.

The objective of this project is to develop a system that takes an image document containing the handwriting of a person and output a few of his/her personality traits based on some selected handwriting features. 

Carefully analyzing all the significant characteristics of a person’s handwriting manually is not only time consuming but prone to errors as well. Automating the analysis on a few selected characteristics of handwriting will speed up the process and reduce the errors.

The proposed methodology extracts seven handwriting features, namely:

1. Top Margin
2. Pen Pressure
3. Baseline Angle
4. Letter Size
5. Line Spacing
6. Word Spacing 
7. Slant Angle

Combinations of these features is used to train eight SVM classifiers to predict eight personality traits of the writer. train_predict.py trains the SVM classifiers and predicts new handwriting samples.
