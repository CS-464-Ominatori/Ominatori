function mi

X = importdata("../train_features.txt");
Y = importdata("../train_labels.txt");

no_of_classes = max(Y);
no_of_features = size(X,2);
[probs, ranks] = calculate_mi(no_of_classes, no_of_features, no_of_train_data, X, Y);
G = save_to_csv(ranks,probs);

thresholds = [0 150 450 750 1050 1200 1350 1500 1550];
losses = zeros(no_of_classes, length(thresholds));
for g=1:no_of_classes
    Temp_X1 = X(:, ranks(g, :));
    filename = strcat('mi_results_for_genre_',num2str(g),'.txt');
    fid = fopen( filename, 'wt');
    for i=1:length(thresholds)
        Temp_X = Temp_X1(:, 1:(end - thresholds(i)));
        Mdl = fitcnb(Temp_X,Y,'Distribution','mn', 'Crossval', 'on');
        losses(g, i) = kfoldLoss(Mdl);
        fprintf("%f, ", losses(g,i));
        fprintf(fid, "%f\n", losses(g,i));
    end
    fprintf('\n');
    figure;
    plot(thresholds, losses(g,:));
    t = sprintf('Losses for %s' , G{g});
    title(t);
end

end

function [probs, ranks] = calculate_mi(no_of_classes, no_of_features, no_of_train_data, X, Y)
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
[probs,ranks] = sort(mi, 2, 'descend');
end


function G=save_to_csv(ranks, probs)
file = fopen("mutual_info.csv");
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
