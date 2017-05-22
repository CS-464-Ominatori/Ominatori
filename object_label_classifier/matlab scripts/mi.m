function mi

X = importdata("../train_features.txt");
Y = importdata("../train_labels.txt");

no_of_classes = max(Y);
no_of_features = size(X,2);
[probs, ranks, mi] = calculate_mi(no_of_classes, no_of_features, size(X,1), X, Y);
G = save_to_csv(ranks,probs);

thresholds = [0 2*10^-8 4*10^-8 6*10^-8 8*10^-8 10^-7 2*10^-7 4*10^-7 6*10^-7 8*10^-7 10^-6 2*10^-6 4*10^-6 6*10^-6 8*10^-6 10^-5 2*10^-5 4*10^-5 6*10^-5 8*10^-5 10^-4 5*10^-4  2*10^-4 4*10^-4 6*10^-4 8*10^-4 10^-3 2*10^-3 4*10^-3 6*10^-3 8*10^-3 10^-2];
losses = zeros(no_of_classes, length(thresholds));
fid = fopen('mi_results.csv', 'wt');
for g=1:no_of_classes
    for i=1:length(thresholds)
        Temp_X = X(:, mi(g, :) > thresholds(i));
        Mdl = fitcnb(Temp_X,Y,'Distribution','mn', 'Crossval', 'on');
        losses(g, i) = kfoldLoss(Mdl);
        fprintf("%f, ", losses(g,i));
        fprintf(fid, "%f,", losses(g,i));
    end
    fprintf('\n');
    fprintf(fid, '\n');
end
figure;
plot(1:length(thresholds), losses);
legend(G);
xlabel("MI Thresholds");
ylabel("Cross Validation Losses");
end

function [probs, ranks, return_mi] = calculate_mi(no_of_classes, no_of_features, no_of_train_data, X, Y)
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
return_mi = mi;
[probs,ranks] = sort(mi, 2, 'descend');
end


function G=save_to_csv(ranks, probs)
file = fopen("mutual_info.csv", 'w');
D = importdata("../dictionary.txt");
D = strsplit(D{1}, ',');
G = importdata("../../shared/genres.txt");
for g=1:length(G)
    for i=1:10
        fprintf(file, "%s,%f,", D{ranks(g, i)}, probs(g,i));
    end
    fprintf(file, "\n");
end
end