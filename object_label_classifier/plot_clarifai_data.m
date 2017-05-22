% X = csvread("clarifai_values.txt");
% X = reshape(X, size(X,1)*size(X,2), 1);
% X(end, :) = [];
% scatter(1:length(X), X, 12, 'MarkerEdgeColor',[0.46 0.316 0.6],...
%              'MarkerFaceColor',[0.92 0.92 1]);
         
Y = csvread("cutoff files/losses.csv");
Y = Y(:, 2:end);
plot(Y(1,:), Y(2, :));
axis([0.69 1.01 0.67 0.79]);
xlabel("Clarifai Thresholds");
ylabel("Cross Validation Losses");