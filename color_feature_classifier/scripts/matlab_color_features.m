function matlab_color_features(DATAPATH, outfile_name)
    %% Get the names of all movie subdirectories 
    directory = dir(DATAPATH);
    idxOfSubdirectories = [directory(:).isdir];
    movieNames = {directory(idxOfSubdirectories).name}';
    movieNames(ismember(movieNames,{'.','..'})) = []; % Remove parent folder paths

    %% Iterate over all poster images and use the getImageFeatures() function
    PATH_TEMPLATE = '%s\\%s\\w342.jpg';
    FEATURE_VECTOR_LENGTH = 7678;
    allFeatures = zeros(size(movieNames, 1), FEATURE_VECTOR_LENGTH);
    for idx = 1:size(movieNames)
        moviePath = sprintf(PATH_TEMPLATE, DATAPATH, movieNames{idx});
        movieFeatures = getImageFeatures(moviePath);
        allFeatures(idx, :) = movieFeatures;
    end

    %% Export matrix to space-delimited file
    dlmwrite(outfile_name, allFeatures,' '); 
end