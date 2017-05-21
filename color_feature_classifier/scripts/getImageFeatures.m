function imgFeatures = getImageFeatures(imageName)
    
    img = imread(imageName);
    
    % Resize
    SCALE_FACTOR = 0.1;
    img = imresize(img, SCALE_FACTOR);

    r = reshape(img(:, :, 1).',1,[]);
    if(size(img, 3) > 1)
        g = reshape(img(:, :, 2).',1,[]);
        b = reshape(img(:, :, 3).',1,[]);
        
        labImg = rgb2lab(img); 

        l = reshape(labImg(:, :, 1).',1,[]);
        a = reshape(labImg(:, :, 2).',1,[]);
        lab_b = reshape(labImg(:, :, 3).',1,[]);
        
        grayImg = rgb2gray(img);
        
    else 
        g = 0;
        b = 0;
        
        l = 0;
        a = 0;
        lab_b = 0;
        
        grayImg = img;
    end
    
    entr = entropy(grayImg);

    grayMtx = graycomatrix(grayImg);
    f = graycoprops(grayMtx, {'Contrast', 'Homogeneity', 'Correlation', 'Energy'} );
    
    % Get histogram of gradients
    hog = extractHOGFeatures(img);

    imgFeatures = [ r, g, b, l, a, lab_b, entr, f.Contrast, f.Homogeneity, f.Correlation, f.Energy, hog ];
end

