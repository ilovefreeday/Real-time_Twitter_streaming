# Real-time_Twitter_streaming
Real-time tweets analyze using Spark

### Setting up
- Create a segregated development environment in a virtual machine running on Ubuntu 14.04, so it does not interfere with any existing system.
- Install Spark 1.3.0 with its dependencies, namely.
- Install the Anaconda Python 2.7 environment with all the required libraries such as Pandas, Scikit-Learn, Blaze, and Bokeh, and enable PySpark, so it can be accessed through IPython Notebooks.
- Set up the backend or data stores of our environment. We will use MySQL as the relational database, MongoDB as the document store, and Cassandra as the columnar database.

### Deploying on AWS
- Create an AWS EC2 key pair via the AWS console http://aws.amazon.com/
console/.
- Export your key pair to your environment:
       ```export AWS_ACCESS_KEY_ID=accesskeyid```
       ```export AWS_SECRET_ACCESS_KEY=secretaccesskey```
- Launch your cluster:
       ```~$ cd $SPARK_HOME/ec2
       ```ec2$ ./spark-ec2 -k <keypair> -i <key-file> -s <num-slaves> launch <cluster-name>```
- SSH into a cluster to run Spark jobs:
       ```ec2$ ./spark-ec2 -k <keypair> -i <key-file> login <cluster-name>```
- Destroy your cluster after usage:
       ```ec2$ ./spark-ec2 destroy <cluster-name>```

### Getting data
 - Twitter: https://apps.twitter.com/app/new
 - Github: https://developer.github.com/v3/
 - Meetup:  https://secure.meetup. com/meetup_api

### Mongodb
Start Mongodb server
```sudo service mongodb start```
Stop Mongodb server:
```sudo service mongodb stop```
Running mongo in python:
```from pymongo import MongoClient```

### Handle Twitte
- Initialize by instantiating Twitter API with our credentials
- Initialize the logger by providing the log level
- Set the log path and the message format
- Initialize the JSON file persistence instruction
- Initialize the MongoDB database and collection for persistence
- Calling API with the relevant query baed on parameters specified

### Exploring data with Blaze
Blaze is an open source Python library, Blaze extends to out-of-core computing, while Pandas and Numpy are single-core.
- Data: Seamless exchange of data across storages such as CSV, JSON, HDF5, HDFS, and Bcolz files.
- Computation: Using the same query processing against computational backends such as Spark, MongoDB, Pandas, or SQL Alchemy.
- Symbolic expressions: Abstract expressions such as join, group-by, filter, selection, and projection with a syntax similar to Pandas but limited in scope. Implements the split-apply-combine methods pioneered by the R language.

### Two models for processing:
- Processing one record at a time as they come in. We do not buffer the incoming records in a container before processing them. This is the case of Twitter's Storm, Yahoo's S4, and Google's MillWheel.
- Micro-batching or batch computations on small intervals as performed by Spark Streaming and Storm Trident. In this case, we buffer the incoming records in a container according to the time window prescribed in the micro-batching settings.

### Kafka
Apache Kafka is a distributed publish subscribe messaging system rethought as a distributed commit log. The messages are stored by topic.
- High throughput for high volume of events feeds
- Real-time processing of new and derived feeds
- Large data backlogs and persistence for offline consumption
- Low latency as enterprise wide messaging system
- Fault tolerance thanks to its distributed nature

### Python plotting and visualization Libraries
- Matplotlib is the grandfather of the Python plotting libraries. Matplotlib was originally the brainchild of John Hunter who was an open source software proponent and established Matplotlib as one of the most prevalent plotting libraries both in the academic and the data scientific communities. 
- Seaborn, developed by Michael Waskom, is a great library to quickly visualize statistical information. It is built on top of Matplotlib and integrates seamlessly with Pandas and the Python data stack, including Numpy.
- ggplot is relatively new and aims to offer the equivalent of the famous ggplot2 from the R ecosystem for the Python data wranglers. It has the same look and feel of ggplot2 and uses the same grammar of graphics as expounded by Hadley Wickham.
- D3.js is a very popular, JavaScript library developed by Mike Bostock. D3 stands for Data Driven Documents and brings data to life on any modern browser leveraging HTML, SVG, and CSS. It delivers dynamic, powerful, interactive visualizations by manipulating the DOM.
- Bokeh aims to deliver high-performance interactivity over very large or streaming datasets whilst leveraging lot of the concepts of D3.js without the burden of writing some intimidating javascript and css code. Bokeh delivers dynamic visualizations on the browser with or without a server. It integrates seamlessly with Matplotlib, Seaborn and ggplot and renders beautifully in IPython notebooks or Jupyter notebooks.








