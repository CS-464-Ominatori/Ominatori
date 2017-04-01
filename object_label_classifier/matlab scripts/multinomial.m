X = importdata("../train_features.txt");
Y = importdata("../train_labels.txt");

test_features = importdata("../test_features.txt");
test_labels = importdata("../test_labels.txt");

Mdl = fitcnb(X,Y,'Distribution','mn');
class_names = Mdl.ClassNames';

[labels, probabilities, ~] = predict(Mdl, test_features);

addpath('..\..\shared\helper_scripts');
displayPerformance(test_features, test_labels, class_names, probabilities);