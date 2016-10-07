rm -rf app
#mkdir app
rsync -av --progress ../ ./app --exclude docker
docker build -t tyhuang/linkitgo .
rm -rf app
docker rm -f linkitgo-web
docker run -d -ti --restart=always --name linkitgo-web -p 80:80  tyhuang/linkitgo
