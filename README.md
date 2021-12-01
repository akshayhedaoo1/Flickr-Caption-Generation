# Flickr-Caption-Prediction

A new benchmark collection for sentence-based image description and search, consisting of 8,000 images that are each paired with five different captions which provide clear descriptions of the salient entities and events. The images were chosen from five different Flickr groups, and tend not to contain any well-known people or locations, but were manually selected to depict a variety of scenes and situations.

Here we have used Encoder & Decoder technique to extract Captions from Images. The Model used for extracting features of images is ResNet50. 

Steps :
1. Creating a Image Dictionary containing Images and their features. We are taking 2000 Images in this model.
2. Creating a Captions Dictionary from the respective images having Images and their captions.
3. Creating a Vocabulary Dictionary containing tokens and their count.
4. Encoding the Captions using voabulary dictionary.
5. Creating a generator for creating arrays for X which contains Image arrays, Y_in contains encoded sequences and Y_out contains probabilities of encoded sequences which are eventually passed to Model.
6. Model is a combination of Encoder and Decoder which takes combination of X and Y_in as input and Y_out as output.
7. It is trained on 100 epochs with accuracy of 84% .
8. It gives good prediction as shown below:
