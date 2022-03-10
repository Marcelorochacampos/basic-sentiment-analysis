# Build the image
````
docker build -t sentiment-analysis .
````

# Run the container
````
docker run --rm --name sentiment-analysis -p 7575:7575 sentiment-analysis
````

# Usage
Just go to
````
http://localhost:7575
````

# Model
For this project it was used a *Logistic Regression* model, trained with a few portuguese datasets containing users reviews on movies and online shopping.