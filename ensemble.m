function [ensemblePredictions] = ensembleFunction()
    %SVM vector dataSizex9
    %NB vector dataSizex9
    %KNN vector dataSizex9
    %NBObject vector dataSizex9

    averageProbabilities = zeros(dataSize, 9);
    sumProbability = 0;
    for i = 1:dataSize
        for j = 1:9
            averageProbabilities(i, j) = ( SVM(i, j) + NB(i, j) + KNN(i, j) + NBObject(i, j) ) / 4;
        end
    end

    ensemblePredictions = zeros(dataSize, 1);
    for i = 1:dataSize
        [maxValue, indexes] =  averageProbabilities(i, :);
        ensemblePredictions(i) = index;
    end
end
