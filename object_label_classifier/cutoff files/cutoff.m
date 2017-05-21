function cutoff()
cutoffs = [0.0 0.5 0.6 0.7 0.8 0.9];

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
    if(losses(i) < min_loss)
        min_loss = losses(i);
        min_coff = coff;
    end
end
fprintf("minumum loss at %f\n", min_coff);
disp(losses);
figure;
plot(losses);
title("thresholds vs. kFold losses");
xlabel("cutoff thresholds");
ylabel("kFold losses");

fprintf("Training with best cutoff for Clarifai\n");
X = importdata("./train_features_cutoff_"+min_coff+".txt");
Y = importdata("./train_labels_cutoff_"+min_coff+".txt");

test_features = importdata("./test_features_cutoff_"+min_coff+".txt");
test_labels = importdata("./test_labels_cutoff_"+min_coff+".txt");

Mdl = fitcnb(X,Y,'Distribution','mn');
class_names = Mdl.ClassNames';
[labels, probabilities, ~] = predict(Mdl, test_features);

addpath('..\..\shared\helper_scripts');
displayPerformance(test_labels, class_names, probabilities);
displayPerformanceSingleLabel(test_labels, labels);
for i=1:10
    probsCop = probabilities;
    displayPerformanceCutoff(test_labels, class_names, probsCop, i/19);
end
end