function imgFeatures = getImageFeatures(imageName)
    
    img = imread(imageName);

    avgR = mean(mean(img(:, :, 1)));
    if(size(img, 3) > 1)
        avgG = mean(mean(img(:, :, 2)));
        avgB = mean(mean(img(:, :, 3)));
        
        hsvImg = rgb2hsv(img);

        avgH = mean(mean(hsvImg(:, :, 1)));
        avgS = mean(mean(hsvImg(:, :, 2)));
        avgV = mean(mean(hsvImg(:, :, 3)));
        
        labImg = rgb2lab(img); 

        avgL = mean(mean(labImg(:, :, 1)));
        avgA = mean(mean(labImg(:, :, 2)));
        avgLaB = mean(mean(labImg(:, :, 3)));
        
        grayImg = rgb2gray(img);
        
    else 
        avgG = 0;
        avgB = 0;
        
        avgH = 0;
        avgS = 0;
        avgV = 0;
        
        avgL = 0;
        avgA = 0;
        avgLaB = 0;
        
        grayImg = img;
    end
    
    entr = entropy(grayImg);

    grayMtx = graycomatrix(grayImg);
    f = graycoprops(grayMtx, {'Contrast', 'Homogeneity', 'Correlation', 'Energy'} );

    imgFeatures = [ avgR, avgG, avgB, avgH, avgS, avgV, avgL, avgA, avgLaB, entr, f.Contrast, f.Homogeneity, f.Correlation, f.Energy ];
end

