function displayPerformanceSingleLabel(test_labels, labels)
    fprintf("Single prediction\n");
    true_label = 0; % number of movies where at least one genre was correctly predicted
    total_movies = 0;

    for test_id = 1:size(test_labels, 1)
        classes = find(test_labels(test_id, :) == 1);
        success = ismember(labels(test_id), classes);
        if(success)
            true_label = true_label + 1;
        end
        total_movies = total_movies + 1;
    end
    fprintf("At least one genre true with, %d, ",true_label);
    fprintf("Total movies, %d\n\n\n", total_movies);
end