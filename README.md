# Completed first Home Assignment
This repo represents completed first home assignment dedicated to HDFS and MapReduce implementaton and BigData ML in MADE. 

Under  howework several documents has been changed:
First of all ```docker.yaml``` was changed. 

1. List of CLI command is presented in  ``` CLI commands.txt ``` file

2. Set of screenshots are collected in corresponding folder``` screenshots ```
3. MapReduce source code: ```mapper_mean.py```, ```reducer_mean,py```, ```mapper_var.py```, ```reducer_var.py```. 
4. MapReduce calculation was started as
```
mapred -streaming -input /some_folder/AB_NYC_2019.csv -output /some_folder/meanres -mapper mapper_mean.py \
-reducer reducer_mean.py -file /scrp/mapper_mean.py -file /scrp/reducer_mean.py
```
All result are collected in ```test_pandas.ipynb```

Also I have to use shell script ```install_python.sh``` discused in Discord chanel for automatic python installation on all nodes. Finally, I was able to establish MapReduce on both MacOS and Ubuntu. 


<!-- [![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/big-data-europe/Lobby)

# Changes

Version 2.0.0 introduces uses wait_for_it script for the cluster startup

# Hadoop Docker

## Supported Hadoop Versions
See repository branches for supported hadoop versions

## Quick Start

To deploy an example HDFS cluster, run:
```
  docker-compose up
```

Run example wordcount job:
```
  make wordcount
```

Or deploy in swarm:
```
docker stack deploy -c docker-compose-v3.yml hadoop
```

`docker-compose` creates a docker network that can be found by running `docker network list`, e.g. `dockerhadoop_default`.

Run `docker network inspect` on the network (e.g. `dockerhadoop_default`) to find the IP the hadoop interfaces are published on. Access these interfaces with the following URLs:

* Namenode: http://<dockerhadoop_IP_address>:9870/dfshealth.html#tab-overview
* History server: http://<dockerhadoop_IP_address>:8188/applicationhistory
* Datanode: http://<dockerhadoop_IP_address>:9864/
* Nodemanager: http://<dockerhadoop_IP_address>:8042/node
* Resource manager: http://<dockerhadoop_IP_address>:8088/

## Configure Environment Variables

The configuration parameters can be specified in the hadoop.env file or as environmental variables for specific services (e.g. namenode, datanode etc.):
```
  CORE_CONF_fs_defaultFS=hdfs://namenode:8020
```

CORE_CONF corresponds to core-site.xml. fs_defaultFS=hdfs://namenode:8020 will be transformed into:
```
  <property><name>fs.defaultFS</name><value>hdfs://namenode:8020</value></property>
```
To define dash inside a configuration parameter, use triple underscore, such as YARN_CONF_yarn_log___aggregation___enable=true (yarn-site.xml):
```
  <property><name>yarn.log-aggregation-enable</name><value>true</value></property>
```

The available configurations are:
* /etc/hadoop/core-site.xml CORE_CONF
* /etc/hadoop/hdfs-site.xml HDFS_CONF
* /etc/hadoop/yarn-site.xml YARN_CONF
* /etc/hadoop/httpfs-site.xml HTTPFS_CONF
* /etc/hadoop/kms-site.xml KMS_CONF
* /etc/hadoop/mapred-site.xml  MAPRED_CONF

If you need to extend some other configuration file, refer to base/entrypoint.sh bash script. -->
