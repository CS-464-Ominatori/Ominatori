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
false_positives = 0;
total_labels = 0;
total_predicted_labels = 0;

true_label = 0;
total_movies = 0;

for test_id = 1:size(test_features, 1)
    classes = find(test_labels(test_id, :) == 1);
    predicted_classes = class_names(:, ranks(test_id, :));
    success = false;
    for i = 1:size(classes, 2)
        if(ismember(classes(i), predicted_classes))
            true_positives = true_positives + 1;
            success = true;
        end
    end
    for i = 1:size(predicted_classes, 2)
        if(~ismember(predicted_classes(i), classes))
            false_positives = false_positives + 1;
        end
    end
    total_labels = total_labels + size(classes, 2);
    total_predicted_labels = total_predicted_labels + size(predicted_classes,2);
    if(success)
        true_label = true_label + 1;
    end
    total_movies = total_movies + 1;
end

disp(true_positives);
disp(total_labels);
disp(false_positives);
disp(total_predicted_labels);
disp(true_label);
disp(total_movies);