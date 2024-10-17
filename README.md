# wc
###### Similar to Linux command wc

### This file contains the description of this project
### Created by Toothless7788

## IMPORTANT!!! 
- This programme is designed for ```.txt``` files **only**

### How to run the programme
1. Run default file
```
python ./driver.py
```
2. Run file with specific file name
```
python ./driver.py <file_name>
```

### How to run testing programmes
```
./test/run_test.sh
```

### How to run docker
- Docker Compose
```
# Ensure you have docker engine running
# Go to the root folder
docker-compose up
```
- Build + Run
```
# Ensure you have docker engine running
# Go to the root folder
docker build -t wc_app:v1 ./wc_src
docker run wc_app:v1 
```
