These are my learnings froma attempting to learn Machine Learning .. 'badamTsss'

Iris.pdf is an example of how a decision tree goes through data


Classifier - we Train this to identify params for us.

#**Types:**
  Artificial Neural Networks
  Support Vector Machine
  Decision Trees

* Features  - usually these are attributes describing an item e.g apple: red, smooth, 110gs

* Lables - Outputs we want from our classified data



# **FEATURES:**
Classifiers only work as good as the Features you collect:

1. Collect more than one set of features
2. Use thought experiments to try and classify the data using the collected features
3. Avoid Using Useless features
4. Use independent features only
5. Remove Highly correlated features
6. Use features that are easy to understand

Ideal Features are. ...


# **Classifiers:**
These will usually have the same interfaces to interact with e.g

* fit() -- use this to train the classifier
* predict() -- use to predict on a dataset


#**Functions**

*f(x)=y*

x being features i.e the input and y being the labels i.e outputs

#**Use Supervised Learning**
we dont want to make the functions for classifying ourselves, much rather have an algorithm learn and train itself using training data.

#**Implementing our Own K Nearest Neighbor**
Check out the Euclidean distance algorithm.
*remember to add interface for fit
*remember to add interface for predict
*predict interface will use whatever function you use to classify


#**Using TensorFlow**
With tensorflow's neural networ you are relying on some heavier training done by google a few months before.
We need to install and run tensorflow locally for training.
