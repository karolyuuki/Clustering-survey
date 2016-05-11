University of Tsukuba
Directed Research in compurter Science
Karoline Neves Bernardo

- What is clustering?
  Cluster analysis groups objects based on the data describing the objects or their relationships. The main goal of clustering
  is to group objects that are more similar to each other, and different from objects in other groups. Better clusters are the ones 
  whose objects have more similarities withim themselves and a bigger difference with the others.
  Cluster analysis can be used in a variety of fields, as group related documents for browsing, find areas that are more susceptible to earthquakes, identifiying cancerous data, and many more.
  
- Standardization
  The objects are usually represented as points in a  multi-dimensional space, where each dimension represents an attribute that 
  describes the object.
  But this bring us into a problem. Sometimes the range of the values of different parameters is too different (Ex: one varies between
  0 and 1, and other between 1000 and 10000). So the values need to be standartized, else the attirbute with higher values will have more
  influence than other attributes.
  
  Approaches for stardardization
  
  Considering xi as the ith object, xij as the value of the jth attribute of the ith object and xij' as the standardized attribute 
  value.
  These approaches are executed for each attribute value.
  
  A) xij' = xij/max(i)|xij|
    max(i) is the maximum value that the attribute can get, so all the values become between -1 and 1.
    Caracteristics: - Is sensitive to outliers
                    - May not produce good results if the attributes aren't uniformly distributed
  
  B) xij' = xij - uj/ dj
    uj = The mean
    dj = The standard deviation
    If the data is uniformly distributed, most values will vary between -1 and 1
    Caracteristics: - Is sensitive to outliers
    
  c) xij' = xij - uj/ djA
    djA = Absolute deviation
    Most attribute values will lie between -1 and 1
    Caracteristics: - Is more robust in the presence of outliers
    
  The main difference between the approaches B and C are the use of Standard and Absolute deviation. While  in Standard, the deviation is given by the square root of the total, on the Absolute, the deviation is calculed with absolute value, not considering the minus. So, if there is an outlier, it won't affect the result as much as in the Standard Deviation.
  ![Absolute deviation's Formula](http://mrsgalgebra.pbworks.com/f/1280412776/MAD%20formula.JPG)
  ![Standard Deviation's Formula](http://f.tqn.com/y/statistics/1/S/M/-/-/-/standarddev.GIF)

- Definitions of Cluster
  
  The are different definitions of what a cluster is and they can be choosed based on the application.
  
  1) Well-separated Cluster
    A cluster is a set of point such that any point is closer to every other point in the cluster then to any point out of it.
    * In many sets, a point in the edge is closer to another cluster than to objects of its own.
    
  2) Center-based Cluser
    A object in a cluster is closer to the center of a cluster than to the center of any other cluster.
    
  3) Contiguous Cluster
    A point in a cluster is closer to one or more points in the cluster than to any point not in the cluster.
    
  4) Density-based Cluster
    Is a dense region of points which is separated from other dense region by low density.
    * Used when the clusters are irregular or intertwined and when noise and outliers are present.
    
    The density can be defined as the the number of objects in the neighborhood of the object p, divided by the area of a circle (in a 2d case) with radius  ɛ. The neighborhood of the object(p) are all the other objects contained in a circle of radius  ɛ, with center on p. The status of high or low density will be given after the density for all the points being calculated.
    We could cluster our points by saying that points that are nearby (contained in the same neighborhood) and have similar density value belong to the same cluster.
    
  5) Similarity-based Center
    A set of objects that are "similar" and objects in other clusters are not "similar". 
    Used mostly with more subjective attributes, where the metric is not well-defined.
    

- Requirements on similarity measures

  1)a) For dissimilarity: D(pi,pi)= 0
      A point isn`t different from itself
    b) For similarity : S(pi,pi)> max(pi,pj)
      A point is more similar to itself than to any other point
      
  2)Simmetry
    S(pi,pj)=S(pj,pi)
    
  3)Positivity
    S(pi,pj)>=0 for all pi and pj
    
  4)S(pi,pj)=0 only if pi=pj
  
  5)Triangle Inequality
    S(pi,pk)<= S(pi,pj) + S(pj,pk)


- Common Proximity Measures

  1)Distance measures
    The Minkowski Metric is the most commonly used, mostly of ratio scales.
    (http://www.molmine.com/magma/images/distan6.gif)
    r is the parameter, m is the dimensionality of  the data object, and xi and yi are the ith components of the x and y objects,
    respectively.
    *If r=2, is the Euclidean Distance
    
  2) Ordinal measures
    They attribue a rank based on the similarity between the points. Most used with qualitative scales
    
  3) Similarity measures between binary vectors
    These measures have values between 0 and 1. A value of 1 indicates two vectors that are completely similar, and a value of 0
    indicates two vectors that are not similar at all.
    For comparing two vectors(p and q) we have the following quantities:
    M01 = Number of positions where p was 0 and q was 1
    M10 = Number of positions where p was 1 and q was 0
    M00 = Number of positions where p was 0 and q was 0
    M11 = Number of positions where p was 1 and q was 1
    
    And for measures we will present two: Simple Match Coefficient and Jaccard Coefficient.
    
    SMC  = M11+M00/ (M01+M10+M00+M11)
    
    JC = M11/(M10+M01+M11)
    
    In SMC, all matches are being considered, while in Jaccard only the matches with 1s are being considered.



- Clustering Techniques
  
  1)Center-Based Partitional clustering
  
    This type of techniques are based that a center point can represent a cluster.
    
    A) K-Means
    
      The K-means works with a simple algorithm that can be divided in the following steps:
      1- Select K points as the inicial centroids
      2- Assign all points to the closest centroid
      3- Recompute the centroids for each cluster
      4- Repeat steps 2 and 3 until the centroids didn't change
      
      This process usually converges to a local minimum. And the centroid is not an actual point in most cases, it's mostly
      a mean of a group of points unlikely the K-medoid, who always have an actual point as its centroid.
      
      A problem: If the inicial centroids are poorly chosen the result of the clustering will not be good. And choosing randomly
                can lead to bad inicial centroids choices.
      One solution: Updating centroids incrementally
                    Instead of just updating the centroids after all the points had been assigned, it would update every time
                    a point is assigned to a cluster.
                    Goal: Better accuracy and faster convergence
                    Extra advantage: Doesn`t produces empty clusters.
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
  