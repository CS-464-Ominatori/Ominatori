function [ranks] = mi

X = importdata("../train_features.txt");
Y = importdata("../train_labels.txt");

no_of_classes = max(Y);
no_of_features = size(X,2);
no_of_train_data = size(X,1);

mi = zeros(no_of_classes, no_of_features);

N = no_of_train_data;
for c=1:no_of_classes
    for f=1:no_of_features
            N11 = sum(X(Y == c, f));
            N10 = sum(X(Y ~= c,  f));
            N00 = sum(Y ~= c) - N10;
            N01 = sum(Y == c) - N11;

            mi(c, f) = N11/N * log2(N*N11/(N10+N11)/(N01+N11)) + ...
                    N01/N * log2(N*N01/(N00+N01)/(N01+N11)) + ...
                    N10/N * log2(N*N10/(N10+N11)/(N00+N10)) + ...
                    N00/N * log2(N*N00/(N00+N01)/(N00+N10));
    end
end
mi(isnan(mi)) = 0;
[~,ranks] = sort(mi, 2, 'descend');
end