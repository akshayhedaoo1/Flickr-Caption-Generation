# Flickr-Caption-Generation

A new benchmark collection for sentence-based image description and search, consisting of 8,000 images that are each paired with five different captions which provide clear descriptions of the salient entities and events. The images were chosen from five different Flickr groups, and tend not to contain any well-known people or locations, but were manually selected to depict a variety of scenes and situations.

Here we have used Encoder & Decoder technique to extract Captions from Images. The Model used for extracting features of images is ResNet50. 
Here we have used Encoder & Decoder technique to extract Captions from Images. The Model used for extracting features of images is ResNet50.  
Final Model is a combination of Encoder and Decoder which takes combination of X and Y_in as input and Y_out as output where X is Image features, Y_in as encoded captions and Y_out is probability for each encoded captions.
It is trained on 100 epochs with accuracy of 84%.





https://user-images.githubusercontent.com/84308415/145565522-bb5ec523-dab5-4954-9c8d-061eae897911.mp4


