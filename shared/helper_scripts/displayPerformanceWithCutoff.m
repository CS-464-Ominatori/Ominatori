function displayPerformanceWithCutoff(test_labels, class_names, probabilities, cutoffs)
cutoff_results = zeros(2, length(cutoffs));
for i=1:length(cutoffs)
    probs_copy = probabilities;
    [Metric1, Metric2] = displayPerformanceWithCutoffFor(test_labels, class_names, probs_copy, cutoffs(i));
    cutoff_results(1, i) = Metric1;
    cutoff_results(2, i) = Metric2;
end
figure;
xlabel("Thresholds for Predictions");
hold on;
plot(cutoffs, cutoff_results(1,:));
plot(cutoffs, cutoff_results(2,:));
legend({'Correctly Associated Movies', 'False Positives'});
hold off;
end


function [Metric1, Metric2]=displayPerformanceWithCutoffFor(test_labels, class_names, probabilities, cutoff)
    fprintf("Cutoff %f prediction\n", cutoff);
    [sorted, ranks] = sort(probabilities, 2, 'descend');

    true_positives = 0; % number of test movie genres that are correctly classified
    false_positives = 0; % number of predictions that are misses
    total_labels = 0; % sum of all genres per test movie
    total_predicted_labels = 0; % number of labels predicted by the model (3 * movie size since 3 predictions / movie)

    true_label = 0; % number of movies where at least one genre was correctly predicted
    total_movies = 0;

    for test_id = 1:size(test_labels, 1)
        classes = find(test_labels(test_id, :) == 1);
        indices =  probabilities(test_id,:) > cutoff;
        predicted_classes = class_names(:, indices);
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
    fprintf("True positives, %d, ", true_positives);
    fprintf("Total labels, %d, ", total_labels);
    fprintf("False positives, %d, ",false_positives);
    fprintf("Total predicted labels, %d\n",total_predicted_labels);
    fprintf("At least one genre true with, %d, ",true_label);
    fprintf("Total movies, %d\n\n", total_movies);
    Metric1 = true_label/total_movies;
    Metric2 = false_positives/total_predicted_labels;
end