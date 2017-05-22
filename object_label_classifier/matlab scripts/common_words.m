function common_words
X = importdata("../train_features.txt");
Y = importdata("../train_labels.txt");

sums = sum(X,1);
[~,rank] = sort(sums, 2, 'descend');
X = X(:, rank);
t = 10;
losses = zeros(1,t);
for i=1:t
    Temp_X = X(:, t:end);
    Mdl = fitcnb(Temp_X,Y,'Distribution','mn', 'Crossval', 'on');
    losses(i) = kfoldLoss(Mdl);
    fprintf("%f, ", losses(i));
end
fprintf("\n");

figure;
plot(1:t, losses);
xlabel("Number of Common Words Removed");
ylabel("Cross Validation Losses");
end