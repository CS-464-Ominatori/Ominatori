function probabilities = test()
    test_features = importdata("../test_features.txt");
    test_labels = importdata("../test_labels.txt");
    load Mdl;
    class_names = Mdl.ClassNames';
    [labels, probabilities, ~] = predict(Mdl, test_features);

    addpath('..\..\shared\helper_scripts');
    displayPerformance(test_labels, class_names, probabilities);
    displayPerformanceSingleLabel(test_labels, labels);
end