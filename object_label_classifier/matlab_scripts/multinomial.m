X = importdata("../train_features.txt");
Y = importdata("../train_labels.txt");

test_features = importdata("../test_features.txt");
test_labels = importdata("../test_labels.txt");

Mdl = fitcnb(X,Y,'Distribution','mn');
class_names = Mdl.ClassNames';

[labels, probabilities, ~] = predict(Mdl, test_features);

[~, ranks] = sort(probabilities, 2, 'descend');
ranks = ranks(:, 1:3);

true_positives = 0;
total_labels = 0;

for test_id = 1:size(test_features, 1)
    classes = find(test_labels(test_id, :) == 1);
    predicted_classes = class_names(:, ranks(test_id, :));
    for i = 1:size(classes, 2)
        if(ismember(classes(i), predicted_classes))
            true_positives = true_positives + 1;
        end
    end
    total_labels = total_labels + size(classes, 2);
end

disp(true_positives/total_labels);