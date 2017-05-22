function predictions = svm(TRAIN_TRUTH_PATH, TRAIN_FEATURES_PATH, TEST_TRUTH_PATH, TEST_FEATURES_PATH)
    %% Perform kNN
    X = importdata(TRAIN_FEATURES_PATH);
    Y = importdata(TRAIN_TRUTH_PATH);

    Mdl = fitcecoc(X, Y);

    %% Predict
    Xnew = importdata(TEST_FEATURES_PATH);
    [predictions, probabilities, ~] = Mdl.predict(Xnew);

    %% Calculate performance
    Ynew = importdata(TEST_TRUTH_PATH);
    
    addpath('..\..\shared\helper_scripts');
    displayPerformance(Ynew, Mdl.ClassNames', probabilities);
end