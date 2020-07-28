# Aircraft Classification using PyTorch

The dataset should be downloaded and kept in the following structure for the code to run properly. Use the rename_move.py file to rename all the images and move the images into the desired destination.

```
  -/FGVC-Aircraft/data/
                  └─── images
                          └─── 0034309.jpg
                          └─── 0034958.jpg
                          └─── ...
                  └─── variants.txt
                  └─── images_variant_trainval.txt
                  └─── images_variant_test.txt
```
                 

The concept used behind the methodoly is as follows:
- We first train the model using images_variant_train.txt and variants.txt file. We use CNN to classify the images of the aircrafts into varients. Once the varient for a particular image is recieved we can directly map it to it's family.
- A dictionary is created that stores the family of the aircrafts and their varients in key:value format. We can use this dictionary to get the mapping between the varient and the family which is our final goal. The varient recieved from the above CNN can be used to get the family using this dict.

I have used transfer learning and Inception net for training the neural network. The validation accuracy achieved is 93% using WS-DAN method.

We can improve the performance by increasing the number of epochs and the batch size. The batch size used was 12 on Titan Xp GPU but we can increase the batch size which will further improve the overall performance of the model.
