function cutoff()
cutoffs = 70:1:100;
cutoffs = [0 cutoffs];
cutoffs = cutoffs/100;

file1 = fopen('reductions.csv', 'w');
file2 = fopen('losses.csv', 'w');

losses = zeros(1,length(cutoffs));
min_loss = 1;
min_coff = -1;
for i=1:length(cutoffs)
    coff = cutoffs(i);
    if(exist("./train_features_cutoff_"+coff+".txt", 'file') ~= 2)
        commandStr = ['python cutoff.py ',num2str(coff)];
        fprintf("creating files for cutoff = %f", coff);
        [~, ~] = system(commandStr);
    end
    fprintf("...created files for cutoff = %f\n", coff); 
    X = importdata("./train_features_cutoff_"+coff+".txt");
    Y = importdata("./train_labels_cutoff_"+coff+".txt");
    Mdl = fitcnb(X,Y,'Distribution','mn', 'Crossval', 'on');
    losses(i) = kfoldLoss(Mdl);
    fprintf(file1,"%f,", coff);
    fprintf(file2,"%f,", losses(i));
    if(losses(i) < min_loss)
        min_loss = losses(i);
        min_coff = coff;
    end
end
fprintf("\nminumum loss at %f\n", min_coff);
figure;
plot(losses);
xlabel("Clarifai Thresholds");
ylabel("Cross Validation Losses");

% fprintf("Training with best cutoff for Clarifai\n");
% X = importdata("./train_features_cutoff_"+min_coff+".txt");
% Y = importdata("./train_labels_cutoff_"+min_coff+".txt");
% 
% test_features = importdata("./test_features_cutoff_"+min_coff+".txt");
% test_labels = importdata("./test_labels_cutoff_"+min_coff+".txt");
% 
% Mdl = fitcnb(X,Y,'Distribution','mn');
% class_names = Mdl.ClassNames';
% [labels, probabilities, ~] = predict(Mdl, test_features);
% 
% addpath('..\..\shared\helper_scripts');
% displayPerformance(test_labels, class_names, probabilities);
% displayPerformanceSingleLabel(test_labels, labels);
% for i=1:10
%     probsCop = probabilities;
%     displayPerformanceWithCutoff(test_labels, class_names, probsCop, i/19);
% end
end