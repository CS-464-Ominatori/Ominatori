% X = csvread("clarifai_values.txt");
% X = reshape(X, size(X,1)*size(X,2), 1);
% X(end, :) = [];
% scatter(1:length(X), X, 12, 'MarkerEdgeColor',[0.46 0.316 0.6],...
%              'MarkerFaceColor',[0.92 0.92 1]);
         
% Y = csvread("cutoff files/losses.csv");
% Y = Y(:, 2:end);
% plot(Y(1,:), Y(2, :));
% axis([0.69 1.01 0.67 0.79]);
% xlabel("Clarifai Thresholds");
% ylabel("Cross Validation Losses");

G = importdata("../shared/genres.txt");
Y = csvread("./matlab scripts/mi_results.csv");
Y = Y(:, 1:(end-1));
thresholds = [0 2*10^-8 4*10^-8 6*10^-8 8*10^-8 10^-7 2*10^-7 4*10^-7 6*10^-7 8*10^-7 10^-6 2*10^-6 4*10^-6 6*10^-6 8*10^-6 10^-5 2*10^-5 4*10^-5 6*10^-5 8*10^-5 10^-4 5*10^-4  2*10^-4 4*10^-4 6*10^-4 8*10^-4 10^-3 2*10^-3 4*10^-3 6*10^-3 8*10^-3 10^-2];
figure;
plot(1:length(thresholds), Y);
legend(G);
xlabel("MI Threshold Indices");
ylabel("Cross Validation Losses");