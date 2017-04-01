%% Get the names of all movie subdirectories 
DATAPATH = 'D:\CS 464 - Data\Data'; % TODO change this according to your machine
directory = dir(DATAPATH);
idxOfSubdirectories = [directory(:).isdir];
movieNames = {directory(idxOfSubdirectories).name}';
movieNames(ismember(movieNames,{'.','..'})) = []; % Remove parent folder paths

%% Iterate over all poster images and use the getImageFeatures() function
PATH_TEMPLATE = '%s\\%s\\w342.jpg';
FEATURE_VECTOR_LENGTH = 14;
allFeatures = zeros(size(movieNames, 1), FEATURE_VECTOR_LENGTH);
for idx = 1:size(movieNames)
    moviePath = sprintf(PATH_TEMPLATE, DATAPATH, movieNames{idx});
    movieFeatures = getImageFeatures(moviePath);
    allFeatures(idx, :) = movieFeatures;
end

%% Export matrix to space-delimited file
dlmwrite('color_features.txt', allFeatures,' '); 