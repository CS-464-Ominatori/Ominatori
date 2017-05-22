function probabilities = test()
    test_features = importdata("../test_features.txt");
%    test_labels = importdata("../test_labels.txt");
    load Mdl;
 %   class_names = Mdl.ClassNames';
    [~, probabilities, ~] = predict(Mdl, test_features);
%     addpath('..\..\shared\helper_scripts');
% %     displayPerformance(test_labels, class_names, probabilities);
% %     displayPerformanceSingleLabel(test_labels, labels);
%     cutoffs = 0:10000;
%     cutoffs = cutoffs/10000;
%     displayPerformanceWithCutoff(test_labels, class_names, probabilities, cutoffs);
end