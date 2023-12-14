# dsc_210_course_project

## Dataset:

### ** The main data file used to build all the models cannot be uploaded to Github as the size is greater than 100 MB. **

The Goodreads Book Review Dataset, a valuable resource for understanding reader preferences and interactions, 
encompasses a rich collection of book reviews and user-generated data gathered from the Goodreads website. <br>
This dataset, compiled in late 2017, provides insights into the diverse ways readers engage with books and the 
factors that influence their reading choices.


Source: GoodReads Website

Genre: Comics & Graphic Novels <br>
89,411 books <br>
542,338 detailed reviews <br>

![img.png](images/img.png)

DataFrame is transformed to the User Item Matrix. The User Item Matrix for our problem is sparse as you can see below.

![img_1.png](images/img_1.png)

<hr>

## Approaches utilized:

### SVD:
![img_2.png](images/img_2.png)

### SVD++:
![img_3.png](images/img_3.png)

### Non-Negative Matrix Factorization:
![img_4.png](images/img_4.png)

### Probabilistic Matrix Factorization:
![img_5.png](images/img_5.png)

### GLocal-K:
![img_6.png](images/img_6.png)

### Neural Collaborative Filtering:
![img_7.png](images/img_7.png)

<hr>

## Results:

Sample recommendations:
![img_8.png](images/img_8.png)

Performance Table:
![img_9.png](images/img_9.png)

<hr>

## Acknowledgements:
We are grateful to Prof. Tsui-Wei Weng, Teaching Assistants, Group 2 classmates, Halıcıoğlu Data Science Institute, 
San Diego for their support, encouragement, and willingness to help us throughout this project.