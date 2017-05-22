function probabilities = test()
    test_features = importdata("../test_features.txt");
    test_labels = importdata("../test_labels.txt");
    load Mdl;
    class_names = Mdl.ClassNames';
    [labels, probabilities, ~] = predict(Mdl, test_features);

    addpath('..\..\shared\helper_scripts');
    displayPerformance(test_labels, class_names, probabilities);
    displayPerformanceSingleLabel(test_labels, labels);
    cutoff_results = zeros(2, 100);
    for i=1:100
        probs_copy = probabilities;
        [TP, FP] = displayPerformanceWithCutoff(test_labels, class_names, probs_copy, i/100);
        cutoff_results(1, i) = TP;
        cutoff_results(2, i) = FP;
    end
    X = 1:100;
    X = X/100;
    figure;
    xlabel("Thresholds for Predictions");
    hold on;
    plot(X, cutoff_results(1,:));
    plot(X, cutoff_results(2,:));
    legend({'True Positives', 'False Positives'});
    hold off;
end