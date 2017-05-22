function imgFeatures = getImageFeatures(imageName)
    
    % Constants
    MIN_IMG_LENGTH = 342; % found empirically, don't touch
    MAX_LAB_A = 98.254;
    MIN_LAB_A = -86.185;
    MAX_LAB_B = 94.482;
    MIN_LAB_B = -107.863;
    
    img = imread(imageName);
    
    % Square center crop
    [size1, ~] = size(img);
    if size1 > MIN_IMG_LENGTH
        w_start = floor((size1 - MIN_IMG_LENGTH)/2) + 1;
        w_stop = w_start + MIN_IMG_LENGTH;
        img = img(w_start:w_stop, :, :);
    end
    
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
        g = zeros(size(r));
        b = zeros(size(r));
        
        l = zeros(size(r));
        a = zeros(size(r));
        lab_b = zeros(size(r));
        
        grayImg = img;
    end
    
    grayMtx = graycomatrix(grayImg);
    f = graycoprops(grayMtx, {'Contrast', 'Homogeneity', 'Correlation', 'Energy'} );
    
    % Get histogram of gradients
    hog = extractHOGFeatures(img);

    r = double(r)./255;
    g = double(g)./255;
    b = double(b)./255;
    
    l = double(l)./100;
    a = double(a)./(MAX_LAB_A - MIN_LAB_A);
    lab_b = double(lab_b)./(MAX_LAB_B - MIN_LAB_B);
    
    imgFeatures = [ r, g, b, l, a, lab_b, f.Contrast, f.Homogeneity, f.Correlation, f.Energy, hog ];
end

