function train
X = importdata("../train_features.txt");
Y = importdata("../train_labels.txt");
Mdl = fitcnb(X,Y,'Distribution','mn');
save Mdl;
end