%% Perform kNN
TRUTH_PATH = '../../shared/truth_with_genreIDs_split.txt';
FEATURES_PATH = '../color_features_with_split.txt';
NR_TESTS = 0;

X = importdata(FEATURES_PATH);
Y = importdata(TRUTH_PATH);

Mdl = fitcknn(X(1:end-NR_TESTS, :), Y(1:end-NR_TESTS, :));

%% Predict
predictions = Mdl.predict(X(1:end, :));

%% Calculate performance


accuracy = sum(predictions == Y(1:end,:)) / 14119; 
