# testing-service
A simple Python Code for Playing with kubernetes and Open Shift

docker build -t secondservice .

docker run -d -v $(pwd):/demo secondservice 

docker run -d -p 9876:9876 -v $(pwd):/demo testing-service
